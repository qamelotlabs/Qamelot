from time import sleep
from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from WebAPI.models import *
import requests

@shared_task
# some heavy stuff here
def create_Assets():
    snav_timetable_url = "https://api.rarible.org/v0.1/items/all?size=5"
    # snav_timetable_url = "https://api.rarible.org/v0.1/items/byCollection?collection=ETHEREUM:0x5351105753bdbc3baa908a0c04f1468535749c3d&size=2"
    res = requests.get(snav_timetable_url).json()
    creatorsList = []
    ownersList = []
    for item in res['items']:
        # create objects in database
        getAssetDetail = Assets.objects.filter(id=item['id']).exists()
        if getAssetDetail is False:
            if len(item['meta']) > 0:
                asset_id = Assets.objects.create(
                        id              =   item['id'],
                        blockchain      =   item['blockchain'],
                        collection      =   item['collection'],
                        contract        =   item['contract'],
                        tokenId         =   item['tokenId'],
                        mintedAt        =   item['mintedAt'],
                        lastUpdatedAt   =   item['lastUpdatedAt'],
                        supply          =   item['contract'],
                        name            =   item['meta']['name'],
                        description     =   item['meta']['description'],
                        restriction     =   item['meta']['restrictions'],
                        deleted         =   item['deleted'],
                        auction         =   item['auctions'],
                        totalStock      =   item['totalStock'],
                        sellers         =   item['sellers'],
                        status          =   'ACTIVE',
                        platform        =   'rarible'
                )

                print("asset_id: ", asset_id)

                if (len(item['creators']) > 0):
                    for usr in item['creators']:
                        creator_id = AssetsUsers.objects.create(
                            user_type   =   'creators',
                            address     =   usr['account'],
                            value       =   usr['value']
                        )
                        creatorsList.append(creator_id)
                    
                    print("creatorsList", creatorsList)

                    for c_id in creatorsList:
                        Assets.objects.filter(id__exact=asset_id).update(creator_id_id = c_id)

                if (len(item['owners']) > 0):
                    for usr in item['owners']:
                        owner_id = AssetsUsers.objects.create(
                            user_type   =   'owners',
                            address     =   item['owners'][0]['account'],
                            value       =   item['owners'][0]['value']
                        )
                        ownersList.append(owner_id)

                    print("creatorsList", creatorsList)

                    for o_id in ownersList:
                        Assets.objects.filter(id__exact=asset_id).update(owner_id_id = o_id)

                imglist = []
                if (len(item['meta']['content']) > 0):
                    for info in item['meta']['content']:
                        image_id = AssetsImage.objects.create(
                            type            =   info["@type"],
                            url             =   info["url"],
                            representation  =   info["representation"],
                            mimeType        =   info["mimeType"]
                        )
                        imglist.append(image_id)

                    print("imglist", imglist)

                    for im_id in imglist:
                        Assets.objects.filter(id__exact=asset_id).update(image_id_id = im_id)

        # sleep few seconds to avoid database block
        sleep(5)


# after completing full code after that uncommit this functions
create_Assets()
