from Qamelot.project_modules import *


class getTopCollections(APIView):

    def get(self, request, format=None):
        timeRange = self.request.query_params.get('timeRange')
        collectionList = []
        if timeRange == '1d':
            dataCollections = NFTCollection.objects.all().order_by(
                '-oneDayChange', '-oneDayAveragePrice'
            )[:100]
<<<<<<< HEAD
            for collection in dataCollections:
=======
            statsList = []
            for collection in dataCollections:
                statsData = collectionStat.objects.filter(collectionId_id__exact = collection.id)
                for st in range(len(statsData)):
                    cstats = {
                        'collectionId': statsData[st].collectionId_id,
                        'dateLog': statsData[st].dateLog,
                        'oneDayVolume': round(float(statsData[st].oneDayVolume), 3),
                        'oneDayChange': round(float(statsData[st].oneDayChange), 3),
                        'oneDaySales': statsData[st].oneDaySales,
                        'oneDayAveragePrice': round(float(statsData[st].oneDayAveragePrice), 3),
                        'sevenDayVolume': round(float(statsData[st].sevenDayVolume), 3),
                        'sevenDayChange': round(float(statsData[st].sevenDayChange), 3),
                        'sevenDaySales': statsData[st].sevenDaySales,
                        'sevenDayAveragePrice': round(float(statsData[st].sevenDayAveragePrice), 3),
                        'thirtyDayVolume': round(float(statsData[st].thirtyDayVolume), 3),
                        'thirtyDayChange': round(float(statsData[st].thirtyDayChange), 3),
                        'thirtyDaySales': statsData[st].thirtyDaySales,
                        'thirtyDayAveragePrice': round(float(statsData[st].thirtyDayAveragePrice), 3),
                        'totalVolume': round(float(statsData[st].totalVolume), 3),
                        'totalSales': statsData[st].totalSales,
                        'totalSupply': statsData[st].totalSupply,
                        'count': statsData[st].count,
                        'numOwners': statsData[st].numOwners,
                        'averagePrice': statsData[st].averagePrice,
                        'numReports': statsData[st].numReports,
                        'marketCap': statsData[st].marketCap,
                        'floorPrice': statsData[st].floorPrice,
                    }
>>>>>>> 11683575a94ed835dbf9d5703aa8f1fcae30fe74

                resData = {
                    'id': collection.id,
                    'collectionAddress': collection.collectionAddress,
                    'collectionUrl': collection.collectionUrl,
                    'slug': collection.slug,
                    'collectionType': collection.collectionType,
                    'collectionName': collection.collectionName,
                    'collectionDescription': collection.collectionDescription,
<<<<<<< HEAD
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
=======
                    'stats': cstats,
>>>>>>> 11683575a94ed835dbf9d5703aa8f1fcae30fe74
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
<<<<<<< HEAD

=======
                statsData = collectionStat.objects.filter(collectionId_id__exact = collection.id)
                for st in range(len(statsData)):
                    cstats = {
                        'collectionId': statsData[st].collectionId_id,
                        'dateLog': statsData[st].dateLog,
                        'oneDayVolume': round(float(statsData[st].oneDayVolume), 3),
                        'oneDayChange': round(float(statsData[st].oneDayChange), 3),
                        'oneDaySales': statsData[st].oneDaySales,
                        'oneDayAveragePrice': round(float(statsData[st].oneDayAveragePrice), 3),
                        'sevenDayVolume': round(float(statsData[st].sevenDayVolume), 3),
                        'sevenDayChange': round(float(statsData[st].sevenDayChange), 3),
                        'sevenDaySales': statsData[st].sevenDaySales,
                        'sevenDayAveragePrice': round(float(statsData[st].sevenDayAveragePrice), 3),
                        'thirtyDayVolume': round(float(statsData[st].thirtyDayVolume), 3),
                        'thirtyDayChange': round(float(statsData[st].thirtyDayChange), 3),
                        'thirtyDaySales': statsData[st].thirtyDaySales,
                        'thirtyDayAveragePrice': round(float(statsData[st].thirtyDayAveragePrice), 3),
                        'totalVolume': round(float(statsData[st].totalVolume), 3),
                        'totalSales': statsData[st].totalSales,
                        'totalSupply': statsData[st].totalSupply,
                        'count': statsData[st].count,
                        'numOwners': statsData[st].numOwners,
                        'averagePrice': statsData[st].averagePrice,
                        'numReports': statsData[st].numReports,
                        'marketCap': statsData[st].marketCap,
                        'floorPrice': statsData[st].floorPrice,
                    }
                    
>>>>>>> 11683575a94ed835dbf9d5703aa8f1fcae30fe74
                resData = {
                    'id': collection.id,
                    'collectionAddress': collection.collectionAddress,
                    'collectionUrl': collection.collectionUrl,
                    'slug': collection.slug,
                    'collectionType': collection.collectionType,
                    'collectionName': collection.collectionName,
                    'collectionDescription': collection.collectionDescription,
<<<<<<< HEAD
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
=======
                    'stats': cstats,
>>>>>>> 11683575a94ed835dbf9d5703aa8f1fcae30fe74
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
<<<<<<< HEAD

=======
                statsData = collectionStat.objects.filter(collectionId_id__exact = collection.id)
                for st in range(len(statsData)):
                    cstats = {
                        'collectionId': statsData[st].collectionId_id,
                        'dateLog': statsData[st].dateLog,
                        'oneDayVolume': round(float(statsData[st].oneDayVolume), 3),
                        'oneDayChange': round(float(statsData[st].oneDayChange), 3),
                        'oneDaySales': statsData[st].oneDaySales,
                        'oneDayAveragePrice': round(float(statsData[st].oneDayAveragePrice), 3),
                        'sevenDayVolume': round(float(statsData[st].sevenDayVolume), 3),
                        'sevenDayChange': round(float(statsData[st].sevenDayChange), 3),
                        'sevenDaySales': statsData[st].sevenDaySales,
                        'sevenDayAveragePrice': round(float(statsData[st].sevenDayAveragePrice), 3),
                        'thirtyDayVolume': round(float(statsData[st].thirtyDayVolume), 3),
                        'thirtyDayChange': round(float(statsData[st].thirtyDayChange), 3),
                        'thirtyDaySales': statsData[st].thirtyDaySales,
                        'thirtyDayAveragePrice': round(float(statsData[st].thirtyDayAveragePrice), 3),
                        'totalVolume': round(float(statsData[st].totalVolume), 3),
                        'totalSales': statsData[st].totalSales,
                        'totalSupply': statsData[st].totalSupply,
                        'count': statsData[st].count,
                        'numOwners': statsData[st].numOwners,
                        'averagePrice': statsData[st].averagePrice,
                        'numReports': statsData[st].numReports,
                        'marketCap': statsData[st].marketCap,
                        'floorPrice': statsData[st].floorPrice,
                    }
>>>>>>> 11683575a94ed835dbf9d5703aa8f1fcae30fe74
                resData = {
                    'id': collection.id,
                    'collectionAddress': collection.collectionAddress,
                    'collectionUrl': collection.collectionUrl,
                    'slug': collection.slug,
                    'collectionType': collection.collectionType,
                    'collectionName': collection.collectionName,
                    'collectionDescription': collection.collectionDescription,
<<<<<<< HEAD
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
=======
                    'stats': cstats,
>>>>>>> 11683575a94ed835dbf9d5703aa8f1fcae30fe74
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
<<<<<<< HEAD
                '-updatedAt',
                '-oneDayChange', '-oneDayAveragePrice',
                '-sevenDayChange', '-sevenDayAveragePrice',
                '-thirtyDayChange', '-thirtyDayAveragePrice'
            )[:100]
            for collection in dataCollections:
=======
                '-updatedAt'
            )[:10]

            for collection in dataCollections:
                statsData = collectionStat.objects.filter(collectionId_id__exact = collection.id)
                for st in range(len(statsData)):
                    cstats = {
                        'collectionId': statsData[st].collectionId_id,
                        'dateLog': statsData[st].dateLog,
                        'oneDayVolume': round(float(statsData[st].oneDayVolume), 3),
                        'oneDayChange': round(float(statsData[st].oneDayChange), 3),
                        'oneDaySales': statsData[st].oneDaySales,
                        'oneDayAveragePrice': round(float(statsData[st].oneDayAveragePrice), 3),
                        'sevenDayVolume': round(float(statsData[st].sevenDayVolume), 3),
                        'sevenDayChange': round(float(statsData[st].sevenDayChange), 3),
                        'sevenDaySales': statsData[st].sevenDaySales,
                        'sevenDayAveragePrice': round(float(statsData[st].sevenDayAveragePrice), 3),
                        'thirtyDayVolume': round(float(statsData[st].thirtyDayVolume), 3),
                        'thirtyDayChange': round(float(statsData[st].thirtyDayChange), 3),
                        'thirtyDaySales': statsData[st].thirtyDaySales,
                        'thirtyDayAveragePrice': round(float(statsData[st].thirtyDayAveragePrice), 3),
                        'totalVolume': round(float(statsData[st].totalVolume), 3),
                        'totalSales': statsData[st].totalSales,
                        'totalSupply': statsData[st].totalSupply,
                        'count': statsData[st].count,
                        'numOwners': statsData[st].numOwners,
                        'averagePrice': statsData[st].averagePrice,
                        'numReports': statsData[st].numReports,
                        'marketCap': statsData[st].marketCap,
                        'floorPrice': statsData[st].floorPrice,
                    }
>>>>>>> 11683575a94ed835dbf9d5703aa8f1fcae30fe74

                resData = {
                    'id': collection.id,
                    'collectionAddress': collection.collectionAddress,
                    'collectionUrl': collection.collectionUrl,
                    'slug': collection.slug,
                    'collectionType': collection.collectionType,
                    'collectionName': collection.collectionName,
                    'collectionDescription': collection.collectionDescription,
<<<<<<< HEAD
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
=======
                    'stats': cstats,
>>>>>>> 11683575a94ed835dbf9d5703aa8f1fcae30fe74
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
