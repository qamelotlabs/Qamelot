from Qamelot.project_modules import *


class getAllCollectionStats(APIView):
    
    def get(self, request, format=None):
        try:
            collectionStatsList = collectionStat.objects.all().order_by('collectionId_id', '-oneDayChange', '-oneDayAveragePrice')
            statList = []
            for statsData in collectionStatsList:
                
                resData = {
                    'dateLog'                   : statsData.dateLog,
                    'collectionId'              : statsData.collectionId_id,
                    'oneDayVolume'              : statsData.oneDayVolume,
                    'oneDayChange'              : statsData.oneDayChange,
                    'oneDaySales'               : statsData.oneDaySales,
                    'oneDayAveragePrice'        : statsData.oneDayAveragePrice,
                    'sevenDayVolume'            : statsData.sevenDayVolume,
                    'sevenDayChange'            : statsData.sevenDayChange,
                    'sevenDaySales'             : statsData.sevenDaySales,
                    'sevenDayAveragePrice'      : statsData.sevenDayAveragePrice,
                    'thirtyDayVolume'           : statsData.thirtyDayVolume,
                    'thirtyDayChange'           : statsData.thirtyDayChange,
                    'thirtyDaySales'            : statsData.thirtyDaySales,
                    'thirtyDayAveragePrice'     : statsData.thirtyDayAveragePrice,
                    'totalVolume'               : statsData.totalVolume,
                    'totalSales'                : statsData.totalSales,
                    'totalSupply'               : statsData.totalSupply,
                    'count'                     : statsData.count,
                    'numOwners'                 : statsData.numOwners,
                    'averagePrice'              : statsData.averagePrice,
                    'numReports'                : statsData.numReports,
                    'marketCap'                 : statsData.marketCap,
                    'floorPrice'                : statsData.floorPrice,
                }
                statList.append(resData)
                
            resContent = {
            'erorr': False,
            'data': statList
            }    
            return Response(resContent)
        except:
            return Response(errorMsg)

