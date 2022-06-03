from WebAPI.project_modules import *
from .collection_scraping import *
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
    
    # datas_collections = []
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

            if 'creators' in item:
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

            if 'owners' in item:
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
                                imageSubname        = str(asset_id.tokenId) +'_'
                                new_meta_url        = uploadFile(info["url"], imageSubname)

                            image_id = AssetsImage.objects.create(
                                type                    =   info["@type"],
                                external_image_url      =   info["url"],
                                aws_bucket_image_url    =   new_meta_url,
                                representation          =   info["representation"],
                                mimeType                =   info["mimeType"]
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



@shared_task
# some heavy stuff here
def nft_Assets():
    print("NFT Insert task running")

    datas_collections = [
        '0x160c404b2b49cbc3240055ceaee026df1e8497a0',
        '0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258',
        '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d',
        '0xed5af388653567af2f388e6224dc7c4b3241c544',
        '0x60e4d786628fea6478f785a6d7e704777c86a7c6',
        '0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb',
        '0x5af0d9827e0c53e4799bb226655a1de152a425a5',
        '0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b',
        '0x7cc7add921e2222738561d03c89589929cefcf21',
        '0x248139afb8d3a2e16154fbe4fb528a3a214fd8e7',
        '0x23581767a106ae21c074b2276d25e5c3e136a68b',
        '0x4becbdf97747413a18c5a2a53321d09198d3a100',
        '0xcb2411c2b914b000ad13c86027222a797983ef2d',
        '0xdc0479cc5bba033b3e7de9f178607150b3abce1f',
        '0x95fcb7f46f1e652fdf23db087c0f24011775be00',
        '0x03546f472b320883a368f3247b349597eee4be28',
        '0x4247428bfbaf0aaea4984b2639c2e615a7b02bab'
    ]

    for cdata in datas_collections:
        snav_timetable_url = "https://api.rarible.org/v0.1/items/byCollection?collection=ETHEREUM:{}".format(
                cdata)
        res = requests.get(snav_timetable_url).json()
        # print("collections: ", res)

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
        
        # datas_collections = []
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

                if 'creators' in item:
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

                if 'owners' in item:
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
                                    imageSubname        = str(asset_id.tokenId) +'_'
                                    new_meta_url        = uploadFile(info["url"], imageSubname)

                                image_id = AssetsImage.objects.create(
                                    type                    =   info["@type"],
                                    external_image_url      =   info["url"],
                                    aws_bucket_image_url    =   new_meta_url,
                                    representation          =   info["representation"]
                                )
                                imglist.append(image_id.id)

                                if "mimeType" in info:
                                    AssetsImage.objects.filter(id=image_id.id).update(mimeType=info['mimeType'])
                    
                            print("imglist", imglist, info["url"], new_meta_url)

                            for im_id in imglist:
                                Assets.objects.filter(id__exact=asset_id.id).update(image_id_id = im_id)
                else:
                    print ("Not present")

    collections_list = Assets.objects.order_by().values_list('collection', flat=True).distinct()

    collectionSeeding(list(collections_list))

    # sleep few seconds to avoid database block
    sleep(5)

    return res['continuation']
