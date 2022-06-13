from Qamelot.project_modules import *


today = date.today()
yesterday = today - timedelta(days = 1)

class getTopCollections(APIView):

    def get(self, request, format=None):
        timeRange = self.request.query_params.get('timeRange')
        collectionList = []
        if timeRange == 'day':
            dataCollections = NFTCollection.objects.filter(updated_at__exact=str(today))
            for collection in dataCollections:
                
                resData = {
                    # 'id'                        : collection.id,
                    'collectionUrl'            : collection.collection_url,
                    'slug'                      : collection.slug,
                    'collectionName'             : collection.collection_name,
                    'collectionDescription'    : collection.collection_description,
                    'trades'                    : collection.trades,
                    'volume'                    : collection.volume,
                    'floor'                     : collection.floor,
                    'updated_at'                : collection.updated_at
                }

                collectionList.append(resData)

        resContent = {
            'erorr' : False,
            'data'  : collectionList
        }

        return Response(resContent)