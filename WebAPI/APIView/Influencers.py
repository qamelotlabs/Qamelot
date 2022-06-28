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
        
        pass
