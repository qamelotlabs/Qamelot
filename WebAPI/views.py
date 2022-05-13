import requests
snav_timetable_url = "https://api.rarible.org/v0.1/items/all?size=5"
res = requests.get(snav_timetable_url).json()
# print(res['items'][0])

# demolisting = []
# for item in res['items']:
#     if len(item['meta']) > 0:
#         demolistshw = {
#                 'id': item['id'],
#                 'blockchain': item['blockchain'],
#                 'collection': item['collection'],
#                 'contract': item['contract'],
#                 'tokenId': item['tokenId'],
#                 'mintedAt': item['mintedAt'],
#                 'lastUpdatedAt': item['lastUpdatedAt'],
#                 'supply': item['contract'],
#                 'name': item['meta']['name'],
#                 'description': item['meta']['description'],
#                 'restriction': item['meta']['restrictions'],
#                 'deleted': item['deleted'],
#                 'auction': item['auctions'],
#                 'totalStock': item['totalStock'],
#                 'sellers': item['sellers']
#         }
#         demolisting.append(demolistshw)

#         demousrlist = []
#         if (len(item['creators']) > 0):
#             for usr in item['creators']:
#                 demousrlstshw = {
#                     'user_type':'creators',
#                     'address':usr['account'],
#                     'value':usr['value']
#                 }
#                 demousrlist.append(demousrlstshw)

#                 print('data: ', demousrlstshw)

#         print(demousrlist)
                

    # imglist = []
    # if (len(item['meta']['content']) > 0):
    #     for info in item['meta']['content']:
    #         imglstshw = {
    #             "type": info["@type"],
    #             "url": info["url"],
    #             "representation": info["representation"],
    #             "mimeType": info["mimeType"]
    #         }
    #         imglist.append(imglstshw)

            # print('data: ', usrlstshw)

    # print(imglist)


    # print('outside inner loop: ', len(item['creators']), item['creators'])
