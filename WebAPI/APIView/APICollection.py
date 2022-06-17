from Qamelot.project_modules import *


today = date.today()
yesterday = today - timedelta(days = 1)

class getTopCollections(APIView):

    def get(self, request, format=None):
        timeRange = self.request.query_params.get('timeRange')
        collectionList = []
        if timeRange == '1d':
            dataCollections = NFTCollection.objects.filter(createdAt__gte=str(today), updatedAt__lte=str(today))
            for collection in dataCollections:
                
                resData = {
                    'id'                        : collection.id,
                    'collectionAddress'           : collectionAddress,
                    'collectionUrl'               : collectionUrl,
                    'slug'                        : slug,
                    'collectionType'              : collectionType,
                    'collectionName'              : collectionName,
                    'collectionDescription'       : collectionDescription,
                    'oneDayVolume'                : oneDayVolume,
                    'oneDayChange'                : oneDayChange,
                    'oneDaySales'                 : oneDaySales,
                    'oneDayAveragePrice'          : oneDayAveragePrice,
                    'totalVolume'                 : totalVolume,
                    'totalSales'                  : totalSales,
                    'totalSupply'                 : totalSupply,
                    'count'                       : count,
                    'numOwners'                   : numOwners,
                    'averagePrice'                : averagePrice,
                    'numReports'                  : umReports,
                    'marketCap'                   : marketCap,
                    'floorPrice'                  : floorPrice,
                    'collectionSymbol'            : collectionSymbol,
                    'owner'                       : owner,
                    'externalImageUrl'            : externalImageUrl,
                    'awsBucketImageUrl'           : awsBucketImageUrl,
                    'externalLink'                : externalLink,
                    'safelistRequestStatus'       : safelistRequestStatus,
                    'twitterUsername'             : twitterUsername,
                    'discordUrl'                  : discordUrl,
                    'createdAt'                   : createdAt,
                    'updatedAt'                   : updatedAt
                }

                collectionList.append(resData)
        
        elif timeRange == '7d':
            dataCollections = NFTCollection.objects.filter(updatedAt__exact=str(today))
            for collection in dataCollections:
                
                resData = {
                    'id'                            : collection.id,
                    'collectionAddress'             : collectionAddress,
                    'collectionUrl'                 : collectionUrl,
                    'slug'                          : slug,
                    'collectionType'                : collectionType,
                    'collectionName'                : collectionName,
                    'collectionDescription'         : collectionDescription,
                    'sevenDayVolume'                : sevenDayVolume,
                    'sevenDayChange'                : sevenDayChange,
                    'sevenDaySales'                 : sevenDaySales,
                    'sevenDayAveragePrice'          : sevenDayAveragePrice,
                    'totalVolume'                   : totalVolume,
                    'totalSales'                    : totalSales,
                    'totalSupply'                   : totalSupply,
                    'count'                         : count,
                    'numOwners'                     : numOwners,
                    'averagePrice'                  : averagePrice,
                    'numReports'                    : umReports,
                    'marketCap'                     : marketCap,
                    'floorPrice'                    : floorPrice,
                    'collectionSymbol'              : collectionSymbol,
                    'owner'                         : owner,
                    'externalImageUrl'              : externalImageUrl,
                    'awsBucketImageUrl'             : awsBucketImageUrl,
                    'externalLink'                  : externalLink,
                    'safelistRequestStatus'         : safelistRequestStatus,
                    'twitterUsername'               : twitterUsername,
                    'discordUrl'                    : discordUrl,
                    'createdAt'                     : createdAt,
                    'updatedAt'                     : updatedAt
                }

                collectionList.append(resData)

        elif timeRange == '30d':
            dataCollections = NFTCollection.objects.filter(updatedAt__exact=str(today))
            for collection in dataCollections:
                
                resData = {
                    'id'                            : collection.id,
                    'collectionAddress'             : collectionAddress,
                    'collectionUrl'                 : collectionUrl,
                    'slug'                          : slug,
                    'collectionType'                : collectionType,
                    'collectionName'                : collectionName,
                    'collectionDescription'         : collectionDescription,
                    'thirtyDayVolume'               : thirtyDayVolume,
                    'thirtyDayChange'               : thirtyDayChange,
                    'thirtyDaySales'                : thirtyDaySales,
                    'thirtyDayAveragePrice'         : thirtyDayAveragePrice,
                    'totalVolume'                   : totalVolume,
                    'totalSales'                    : totalSales,
                    'totalSupply'                   : totalSupply,
                    'count'                         : count,
                    'numOwners'                     : numOwners,
                    'averagePrice'                  : averagePrice,
                    'numReports'                    : umReports,
                    'marketCap'                     : marketCap,
                    'floorPrice'                    : floorPrice,
                    'collectionSymbol'              : collectionSymbol,
                    'owner'                         : owner,
                    'externalImageUrl'              : externalImageUrl,
                    'awsBucketImageUrl'             : awsBucketImageUrl,
                    'externalLink'                  : externalLink,
                    'safelistRequestStatus'         : safelistRequestStatus,
                    'twitterUsername'               : twitterUsername,
                    'discordUrl'                    : discordUrl,
                    'createdAt'                     : createdAt,
                    'updatedAt'                     : updatedAt
                }

                collectionList.append(resData)

        resContent = {
            'erorr' : False,
            'data'  : collectionList
        }

        return Response(resContent)


# -------------------------------------------------------------------------------------------------- #


# dataCollections = NFTCollection.objects.filter(createdAt__gte=str(today), updatedAt__lte=str(today))
# for collection in dataCollections:
#     print(collection)