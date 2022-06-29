from Qamelot.project_modules import *

class NftInfluencersView(APIView):

    def get(self, request, format=None):
        NftInfluencersList = NftInfluencers.objects.all()
        influencerList = []
        for influencer in NftInfluencersList:
            
            resInfluencerData = {
                'id'            : influencer.id,
                'name'          : influencer.name,
                'verified'      : influencer.verified
            }
            influencerList.append(resInfluencerData)

        resContent = {
            'erorr': False,
            'data': influencerList
        }

        return Response(resContent)
        

    def post(self, request, format=None):
        
        try:
            name = request.data['name']

            InfluencersData = NftInfluencers.objects.filter(name__exact = name).exists()

            if InfluencersData is False:
                
                createInfluencer = NftInfluencers.objects.create(
                    name            = name,
                    created_at      = current
                )

                resData = {
                    'id'            : createInfluencer.id,
                    'name'          : createInfluencer.name,
                    'verified'      : createInfluencer.verified,
                    'createdAt'     : createInfluencer.created_at
                }

                resContent = {
                'erorr': False,
                'data': resData
                }

            return Response(resContent)
        except:
            return Response(errorMsg)