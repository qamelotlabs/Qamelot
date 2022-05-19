from WebAPI.project_modules import *
from .image_scraping import *
@shared_task
# some heavy stuff here
def create_Assets():
    print("create task running")
    snav_timetable_url  = "https://api.rarible.org/v0.1/items/all"
    res                 = requests.get(snav_timetable_url).json()
    api_continuation    = APIPaginate.objects.filter(continuation=res['continuation']).exists()

    print(res['continuation'])

    try:
        if api_continuation is False:
            APIPaginate.objects.create(
            total            =   res['total'],
            continuation     =   res['continuation']
            )
        else:
            APIPaginate.objects.filter(continuation=res['continuation']).update(
                total            =   res['total'],
                continuation     =   res['continuation']
            )
    except:
        pass

    for item in res['items']:
        # create objects in database
        getAssetDetail = Assets.objects.filter(id=item['id']).exists()
        if getAssetDetail is False:
            asset_id = Assets.objects.create(
                id              =   item['id'],
                blockchain      =   item['blockchain'],
                collection      =   item['collection'],
                contract        =   item['contract'],
                tokenId         =   item['tokenId'],
                mintedAt        =   item['mintedAt'],
                lastUpdatedAt   =   item['lastUpdatedAt'],
                supply          =   item['contract'],
                deleted         =   item['deleted'],
                auction         =   item['auctions'],
                totalStock      =   item['totalStock'],
                sellers         =   item['sellers'],
                status          =   'ACTIVE',
                platform        =   'rarible'
            )

            print("asset_id: ", asset_id.id)

            creatorsList            = []
            if (len(item['creators']) > 0):
                for usr in item['creators']:
                    creator_id = AssetsUsers.objects.create(
                        user_type   =   'creators',
                        address     =   usr['account'],
                        value       =   usr['value']
                    )
                    creatorsList.append(creator_id.id)
                
                print("creatorsList", creatorsList)

                for c_id in creatorsList:
                    Assets.objects.filter(id__exact=asset_id.id).update(creator_id_id = c_id)

            ownersList              = []
            if (len(item['owners']) > 0):
                for usr in item['owners']:
                    owner_id = AssetsUsers.objects.create(
                        user_type   =   'owners',
                        address     =   item['owners'][0]['account'],
                        value       =   item['owners'][0]['value']
                    )
                    ownersList.append(owner_id.id)

                print("creatorsList", creatorsList)

                for o_id in ownersList:
                    Assets.objects.filter(id__exact=asset_id.id).update(owner_id_id = o_id)

            if 'meta' in item:
                name                = ''
                description         = ''
                restriction         = ''
                meta_name           = item['meta']
                meta_description    = item['meta']
                meta_restriction    = item['meta']

                if 'name' in meta_name:
                    name            =   item['meta']['name']

                if 'description' in meta_description:
                    description     =   item['meta']['description']

                if 'restriction' in meta_restriction:
                    restriction     =   item['meta']['restrictions']

                Assets.objects.filter(id__exact=asset_id.id).update(
                    name            =   name,
                    description     =   description,
                    restriction     =   restriction
                )

                print (item['meta'])

                imglist = []
                meta_content = item['meta']
                if 'content' in meta_content:
                    if len(item['meta']['content']) > 0:
                        for info in item['meta']['content']:

                            if info["url"]:
                                imageSubname = str(asset_id.tokenId) +'_'
                                new_meta_url = uploadFile(info["url"], imageSubname)

                            image_id = AssetsImage.objects.create(
                                type            =   info["@type"],
                                url             =   new_meta_url,
                                representation  =   info["representation"],
                                mimeType        =   info["mimeType"]
                            )
                            imglist.append(image_id.id)
                
                        print("imglist", imglist, info["url"], new_meta_url)

                        for im_id in imglist:
                            Assets.objects.filter(id__exact=asset_id.id).update(image_id_id = im_id)
            else:
                print ("Not present")

        # sleep few seconds to avoid database block
        sleep(5)

    return res['continuation']
