from Qamelot.project_modules import *


class getTopCollections(APIView):

    def get(self, request, format=None):
        timeRange = self.request.query_params.get('timeRange')
        collectionList = []
        if timeRange == '1d':
            dataCollections = NFTCollection.objects.all().order_by(
                '-oneDayChange', '-oneDayAveragePrice'
            )[:100]
            for collection in dataCollections:

                resData = {
                    'id': collection.id,
                    'collectionAddress': collection.collectionAddress,
                    'collectionUrl': collection.collectionUrl,
                    'slug': collection.slug,
                    'collectionType': collection.collectionType,
                    'collectionName': collection.collectionName,
                    'collectionDescription': collection.collectionDescription,
                    'oneDayVolume': round(float(collection.oneDayVolume), 3),
                    'oneDayChange': round(float(collection.oneDayChange), 3),
                    'oneDaySales': collection.oneDaySales,
                    'oneDayAveragePrice': round(float(collection.oneDayAveragePrice), 3),
                    'totalVolume': round(float(collection.totalVolume), 3),
                    'totalSales': collection.totalSales,
                    'totalSupply': collection.totalSupply,
                    'count': collection.count,
                    'numOwners': collection.numOwners,
                    'averagePrice': collection.averagePrice,
                    'numReports': collection.numReports,
                    'marketCap': collection.marketCap,
                    'floorPrice': collection.floorPrice,
                    'collectionSymbol': collection.collectionSymbol,
                    'owner': collection.owner,
                    'externalImageUrl': collection.externalImageUrl,
                    'awsBucketImageUrl': collection.awsBucketImageUrl,
                    'externalLink': collection.externalLink,
                    'safelistRequestStatus': collection.safelistRequestStatus,
                    'twitterUsername': collection.twitterUsername,
                    'discordUrl': collection.discordUrl,
                    'createdAt': collection.createdAt,
                    'updatedAt': collection.updatedAt
                }

                collectionList.append(resData)

        elif timeRange == '7d':
            dataCollections = NFTCollection.objects.all().order_by(
                '-sevenDayChange', '-sevenDayAveragePrice'
            )[:100]
            for collection in dataCollections:

                resData = {
                    'id': collection.id,
                    'collectionAddress': collection.collectionAddress,
                    'collectionUrl': collection.collectionUrl,
                    'slug': collection.slug,
                    'collectionType': collection.collectionType,
                    'collectionName': collection.collectionName,
                    'collectionDescription': collection.collectionDescription,
                    'sevenDayVolume': round(float(collection.sevenDayVolume), 3),
                    'sevenDayChange': round(float(collection.sevenDayChange), 3),
                    'sevenDaySales': collection.sevenDaySales,
                    'sevenDayAveragePrice': round(float(collection.sevenDayAveragePrice), 3),
                    'totalVolume': round(float(collection.totalVolume), 3),
                    'totalSales': collection.totalSales,
                    'totalSupply': collection.totalSupply,
                    'count': collection.count,
                    'numOwners': collection.numOwners,
                    'averagePrice': collection.averagePrice,
                    'numReports': collection.numReports,
                    'marketCap': collection.marketCap,
                    'floorPrice': collection.floorPrice,
                    'collectionSymbol': collection.collectionSymbol,
                    'owner': collection.owner,
                    'externalImageUrl': collection.externalImageUrl,
                    'awsBucketImageUrl': collection.awsBucketImageUrl,
                    'externalLink': collection.externalLink,
                    'safelistRequestStatus': collection.safelistRequestStatus,
                    'twitterUsername': collection.twitterUsername,
                    'discordUrl': collection.discordUrl,
                    'createdAt': collection.createdAt,
                    'updatedAt': collection.updatedAt
                }

                collectionList.append(resData)

        elif timeRange == '30d':
            dataCollections = NFTCollection.objects.all().order_by(
                '-thirtyDayChange', '-thirtyDayAveragePrice'
            )[:100]
            for collection in dataCollections:

                resData = {
                    'id': collection.id,
                    'collectionAddress': collection.collectionAddress,
                    'collectionUrl': collection.collectionUrl,
                    'slug': collection.slug,
                    'collectionType': collection.collectionType,
                    'collectionName': collection.collectionName,
                    'collectionDescription': collection.collectionDescription,
                    'thirtyDayVolume': round(float(collection.thirtyDayVolume), 3),
                    'thirtyDayChange': round(float(collection.thirtyDayChange), 3),
                    'thirtyDaySales': collection.thirtyDaySales,
                    'thirtyDayAveragePrice': round(float(collection.thirtyDayAveragePrice), 3),
                    'totalVolume': round(float(collection.totalVolume), 3),
                    'totalSales': collection.totalSales,
                    'totalSupply': collection.totalSupply,
                    'count': collection.count,
                    'numOwners': collection.numOwners,
                    'averagePrice': collection.averagePrice,
                    'numReports': collection.numReports,
                    'marketCap': collection.marketCap,
                    'floorPrice': collection.floorPrice,
                    'collectionSymbol': collection.collectionSymbol,
                    'owner': collection.owner,
                    'externalImageUrl': collection.externalImageUrl,
                    'awsBucketImageUrl': collection.awsBucketImageUrl,
                    'externalLink': collection.externalLink,
                    'safelistRequestStatus': collection.safelistRequestStatus,
                    'twitterUsername': collection.twitterUsername,
                    'discordUrl': collection.discordUrl,
                    'createdAt': collection.createdAt,
                    'updatedAt': collection.updatedAt
                }

                collectionList.append(resData)

        else:
            dataCollections = NFTCollection.objects.all().order_by(
                '-updatedAt',
                '-oneDayChange', '-oneDayAveragePrice',
                '-sevenDayChange', '-sevenDayAveragePrice',
                '-thirtyDayChange', '-thirtyDayAveragePrice'
            )[:100]
            for collection in dataCollections:

                resData = {
                    'id': collection.id,
                    'collectionAddress': collection.collectionAddress,
                    'collectionUrl': collection.collectionUrl,
                    'slug': collection.slug,
                    'collectionType': collection.collectionType,
                    'collectionName': collection.collectionName,
                    'collectionDescription': collection.collectionDescription,
                    'oneDayVolume': round(float(collection.oneDayVolume), 3),
                    'oneDayChange': round(float(collection.oneDayChange), 3),
                    'oneDaySales': collection.oneDaySales,
                    'oneDayAveragePrice': round(float(collection.oneDayAveragePrice), 3),
                    'sevenDayVolume': round(float(collection.sevenDayVolume), 3),
                    'sevenDayChange': round(float(collection.sevenDayChange), 3),
                    'sevenDaySales': collection.sevenDaySales,
                    'sevenDayAveragePrice': round(float(collection.sevenDayAveragePrice), 3),
                    'thirtyDayVolume': round(float(collection.thirtyDayVolume), 3),
                    'thirtyDayChange': round(float(collection.thirtyDayChange), 3),
                    'thirtyDaySales': collection.thirtyDaySales,
                    'thirtyDayAveragePrice': round(float(collection.thirtyDayAveragePrice), 3),
                    'totalVolume': round(float(collection.totalVolume), 3),
                    'totalSales': collection.totalSales,
                    'totalSupply': collection.totalSupply,
                    'count': collection.count,
                    'numOwners': collection.numOwners,
                    'averagePrice': collection.averagePrice,
                    'numReports': collection.numReports,
                    'marketCap': collection.marketCap,
                    'floorPrice': collection.floorPrice,
                    'collectionSymbol': collection.collectionSymbol,
                    'owner': collection.owner,
                    'externalImageUrl': collection.externalImageUrl,
                    'awsBucketImageUrl': collection.awsBucketImageUrl,
                    'externalLink': collection.externalLink,
                    'safelistRequestStatus': collection.safelistRequestStatus,
                    'twitterUsername': collection.twitterUsername,
                    'discordUrl': collection.discordUrl,
                    'createdAt': collection.createdAt,
                    'updatedAt': collection.updatedAt
                }

                collectionList.append(resData)

        resContent = {
            'erorr': False,
            'data': collectionList
        }

        return Response(resContent)
