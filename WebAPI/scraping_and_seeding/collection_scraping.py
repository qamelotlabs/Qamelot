from WebAPI.project_modules import *
from .image_scraping import *


def collectionSeeding(datas_collections):
    
    datas_collections = Assets.objects.filter(collection__in=datas_collections)
    # collectionsList = []
    for cdata in datas_collections:
        # print('c_address: ', cdata.id)
        # collectionsList.append(cdata)
        snav_timetable_url      = "https://api.rarible.org/v0.1/collections/{}".format(cdata.collection)
        collections_response    = requests.get(snav_timetable_url).json()
        # print('collectionsList: ', collections_response['id'])

        getCollectionDetail = AssetsCollection.objects.filter(collection_id=collections_response['id']).exists()
        if getCollectionDetail is False:
            c_id = AssetsCollection.objects.create(
                collection_id = collections_response['id'],
                blockchain = collections_response['blockchain'],
                colletion_type = collections_response['type'],
            )
            print('collection id: ', c_id)
            if 'owner' in collections_response:            
                owner   = collections_response['owner'],
                AssetsCollection.objects.filter(id__exact=c_id.id).update(
                    owner              =   owner
                )

            if 'symbol' in collections_response:            
                symbol  = collections_response['symbol']
                AssetsCollection.objects.filter(id__exact=c_id.id).update(
                    symbol              =   symbol
                )


            if 'meta' in collections_response:
                name                    = ''
                description             = ''
                external_link           = ''
                fee_recipient           = ''
                seller_fee_basis_point    = ''
                meta_name           = collections_response['meta']
                meta_description    = collections_response['meta']
                if 'name' in meta_name:
                    name                    =   collections_response['meta']['name']
                    # print(name)
                if 'description' in meta_description:
                    description             =   collections_response['meta']['description']
                    # print(description)
                if 'externalLink' in meta_description:
                    external_link           =   collections_response['meta']['externalLink']
                if 'feeRecipient' in meta_description:
                    fee_recipient           =   collections_response['meta']['feeRecipient']
                if 'sellerFeeBasisPoints' in meta_description:
                    seller_fee_basis_point    =   collections_response['meta']['sellerFeeBasisPoints']

                AssetsCollection.objects.filter(id__exact=c_id.id).update(
                    name            =   name,
                    description     =   description,
                    external_link   = external_link,
                    fee_recipient   = fee_recipient,
                    seller_fee_basis_point = seller_fee_basis_point
                )

                imglist = []
                meta_content = collections_response['meta']
                if 'content' in meta_content:
                    if len(collections_response['meta']['content']) > 0:
                        for info in collections_response['meta']['content']:

                            if info["url"]:
                                imageSubname        = str(c_id) +'_'
                                new_meta_url        = uploadFile(info["url"], imageSubname)

                            image_id = AssetsImage.objects.create(
                                type                    =   info["@type"],
                                external_image_url      =   info["url"],
                                aws_bucket_image_url    =   new_meta_url,
                                representation          =   info["representation"],
                                mimeType                =   ''
                            )
                            imglist.append(image_id.id)
                
                        # print("imglist", imglist, info["url"], new_meta_url)

                        for im_id in imglist:
                            AssetsCollection.objects.filter(id__exact=c_id.id).update(collection_image_id = im_id)

            Assets.objects.filter(collection__exact=cdata.id).update(asset_collection_id=c_id)


datas_collections = Assets.objects.order_by().values_list('collection', flat=True).distinct()

# print(list(datas_collections))

# collectionSeeding(list(datas_collections))