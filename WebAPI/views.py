# import requests
# snav_timetable_url = "https://api.rarible.org/v0.1/items/all?size=5"
# res = requests.get(snav_timetable_url).json()
# print(res['continuation'])

# demolisting = []
# for item in res['items']:


#     if 'meta' in item:
#         print ("Present, value =", item['meta'])
#     else:
#         print ("Not present")

#     demolistshw = {
#         'id': item['id'],
#         'blockchain': item['blockchain'],
#         'collection': item['collection'],
#         'contract': item['contract'],
#         'tokenId': item['tokenId'],
#         'mintedAt': item['mintedAt'],
#         'lastUpdatedAt': item['lastUpdatedAt'],
#         'supply': item['contract'],
#         'deleted': item['deleted'],
#         'auction': item['auctions'],
#         'totalStock': item['totalStock'],
#         'sellers': item['sellers']
#     }
#     demolisting.append(demolistshw)

#     try:
#         if 'meta' in item:
#             detail = {
#                 'name': item['meta']['name'],
#                 'description': item['meta']['description'],
#                 'restriction': item['meta']['restrictions'],
#             }
#             print (detail)
#             imglist = []
#             meta_content = item['meta']
#             if 'content' in meta_content:
#                 if len(item['meta']['content']) > 0:
#                     for info in item['meta']['content']:
#                         imglstshw = {
#                             "type": info["@type"],
#                             "url": info["url"],
#                             "representation": info["representation"],
#                             "mimeType": info["mimeType"]
#                         }
#                         imglist.append(imglstshw)
#                 print('IMAGE DETAIL: ', imglist)

#         else:
#             print ("Not present")

#     except:
#         pass
