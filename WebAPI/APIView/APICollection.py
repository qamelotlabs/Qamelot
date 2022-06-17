from Qamelot.project_modules import *


today = date.today()
yesterday = today - timedelta(days = 1)

class getTopCollections(APIView):

    def get(self, request, format=None):
        timeRange = self.request.query_params.get('timeRange')
        collectionList = []
        if timeRange == '1d':
            dataCollections = NFTCollection.objects.all().order_by('-oneDayChange', '-oneDayAveragePrice')
            for collection in dataCollections:
                
                resData = {
                    'id'                            : collection.id,
                    'collectionAddress'             : collection.collectionAddress,
                    'collectionUrl'                 : collection.collectionUrl,
                    'slug'                          : collection.slug,
                    'collectionType'                : collection.collectionType,
                    'collectionName'                : collection.collectionName,
                    'collectionDescription'         : collection.collectionDescription,
                    'oneDayVolume'                  : collection.oneDayVolume,
                    'oneDayChange'                  : collection.oneDayChange,
                    'oneDaySales'                   : collection.oneDaySales,
                    'oneDayAveragePrice'            : collection.oneDayAveragePrice,
                    'totalVolume'                   : collection.totalVolume,
                    'totalSales'                    : collection.totalSales,
                    'totalSupply'                   : collection.totalSupply,
                    'count'                         : collection.count,
                    'numOwners'                     : collection.numOwners,
                    'averagePrice'                  : collection.averagePrice,
                    'numReports'                    : collection.numReports,
                    'marketCap'                     : collection.marketCap,
                    'floorPrice'                    : collection.floorPrice,
                    'collectionSymbol'              : collection.collectionSymbol,
                    'owner'                         : collection.owner,
                    'externalImageUrl'              : collection.externalImageUrl,
                    'awsBucketImageUrl'             : collection.awsBucketImageUrl,
                    'externalLink'                  : collection.externalLink,
                    'safelistRequestStatus'         : collection.safelistRequestStatus,
                    'twitterUsername'               : collection.twitterUsername,
                    'discordUrl'                    : collection.discordUrl,
                    'createdAt'                     : collection.createdAt,
                    'updatedAt'                     : collection.updatedAt
                }
                
                collectionList.append(resData)
        
        elif timeRange == '7d':
            dataCollections = NFTCollection.objects.all().order_by('-sevenDayChange', '-sevenDayAveragePrice')
            for collection in dataCollections:
                
                resData = {
                    'id'                            : collection.id,
                    'collectionAddress'             : collection.collectionAddress,
                    'collectionUrl'                 : collection.collectionUrl,
                    'slug'                          : collection.slug,
                    'collectionType'                : collection.collectionType,
                    'collectionName'                : collection.collectionName,
                    'collectionDescription'         : collection.collectionDescription,
                    'sevenDayVolume'                : collection.sevenDayVolume,
                    'sevenDayChange'                : collection.sevenDayChange,
                    'sevenDaySales'                 : collection.sevenDaySales,
                    'sevenDayAveragePrice'          : collection.sevenDayAveragePrice,
                    'totalVolume'                   : collection.totalVolume,
                    'totalSales'                    : collection.totalSales,
                    'totalSupply'                   : collection.totalSupply,
                    'count'                         : collection.count,
                    'numOwners'                     : collection.numOwners,
                    'averagePrice'                  : collection.averagePrice,
                    'numReports'                    : collection.numReports,
                    'marketCap'                     : collection.marketCap,
                    'floorPrice'                    : collection.floorPrice,
                    'collectionSymbol'              : collection.collectionSymbol,
                    'owner'                         : collection.owner,
                    'externalImageUrl'              : collection.externalImageUrl,
                    'awsBucketImageUrl'             : collection.awsBucketImageUrl,
                    'externalLink'                  : collection.externalLink,
                    'safelistRequestStatus'         : collection.safelistRequestStatus,
                    'twitterUsername'               : collection.twitterUsername,
                    'discordUrl'                    : collection.discordUrl,
                    'createdAt'                     : collection.createdAt,
                    'updatedAt'                     : collection.updatedAt
                }

                collectionList.append(resData)

        elif timeRange == '30d':
            dataCollections = NFTCollection.objects.all().order_by('-thirtyDayChange','-thirtyDayAveragePrice')
            for collection in dataCollections:
                
                resData = {
                    'id'                            : collection.id,
                    'collectionAddress'             : collection.collectionAddress,
                    'collectionUrl'                 : collection.collectionUrl,
                    'slug'                          : collection.slug,
                    'collectionType'                : collection.collectionType,
                    'collectionName'                : collection.collectionName,
                    'collectionDescription'         : collection.collectionDescription,
                    'thirtyDayVolume'               : collection.thirtyDayVolume,
                    'thirtyDayChange'               : collection.thirtyDayChange,
                    'thirtyDaySales'                : collection.thirtyDaySales,
                    'thirtyDayAveragePrice'         : collection.thirtyDayAveragePrice,
                    'totalVolume'                   : collection.totalVolume,
                    'totalSales'                    : collection.totalSales,
                    'totalSupply'                   : collection.totalSupply,
                    'count'                         : collection.count,
                    'numOwners'                     : collection.numOwners,
                    'averagePrice'                  : collection.averagePrice,
                    'numReports'                    : collection.numReports,
                    'marketCap'                     : collection.marketCap,
                    'floorPrice'                    : collection.floorPrice,
                    'collectionSymbol'              : collection.collectionSymbol,
                    'owner'                         : collection.owner,
                    'externalImageUrl'              : collection.externalImageUrl,
                    'awsBucketImageUrl'             : collection.awsBucketImageUrl,
                    'externalLink'                  : collection.externalLink,
                    'safelistRequestStatus'         : collection.safelistRequestStatus,
                    'twitterUsername'               : collection.twitterUsername,
                    'discordUrl'                    : collection.discordUrl,
                    'createdAt'                     : collection.createdAt,
                    'updatedAt'                     : collection.updatedAt
                }

                collectionList.append(resData)

        else:
            dataCollections = NFTCollection.objects.all().order_by(
                    '-updatedAt',
                    '-oneDayChange', '-oneDayAveragePrice',
                    '-sevenDayChange', '-sevenDayAveragePrice',
                    '-thirtyDayChange','-thirtyDayAveragePrice'
                    )[:100]
            for collection in dataCollections:
                
                resData = {
                    'id'                            : collection.id,
                    'collectionAddress'             : collection.collectionAddress,
                    'collectionUrl'                 : collection.collectionUrl,
                    'slug'                          : collection.slug,
                    'collectionType'                : collection.collectionType,
                    'collectionName'                : collection.collectionName,
                    'collectionDescription'         : collection.collectionDescription,
                    'thirtyDayVolume'               : collection.thirtyDayVolume,
                    'thirtyDayChange'               : collection.thirtyDayChange,
                    'thirtyDaySales'                : collection.thirtyDaySales,
                    'thirtyDayAveragePrice'         : collection.thirtyDayAveragePrice,
                    'totalVolume'                   : collection.totalVolume,
                    'totalSales'                    : collection.totalSales,
                    'totalSupply'                   : collection.totalSupply,
                    'count'                         : collection.count,
                    'numOwners'                     : collection.numOwners,
                    'averagePrice'                  : collection.averagePrice,
                    'numReports'                    : collection.numReports,
                    'marketCap'                     : collection.marketCap,
                    'floorPrice'                    : collection.floorPrice,
                    'collectionSymbol'              : collection.collectionSymbol,
                    'owner'                         : collection.owner,
                    'externalImageUrl'              : collection.externalImageUrl,
                    'awsBucketImageUrl'             : collection.awsBucketImageUrl,
                    'externalLink'                  : collection.externalLink,
                    'safelistRequestStatus'         : collection.safelistRequestStatus,
                    'twitterUsername'               : collection.twitterUsername,
                    'discordUrl'                    : collection.discordUrl,
                    'createdAt'                     : collection.createdAt,
                    'updatedAt'                     : collection.updatedAt
                }

                collectionList.append(resData)

        resContent = {
            'erorr' : False,
            'data'  : collectionList
        }

        return Response(resContent)


# -------------------------------------------------------------------------------------------------- #

# dataCollections = NFTCollection.objects.all().order_by('-oneDayChange', '-oneDayAveragePrice')
# for dat in dataCollections:
#     print(dat.oneDayChange, dat.oneDayAveragePrice)