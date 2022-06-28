from Qamelot.project_modules import *

class UserSimRegistrationPostView(APIView):
    # authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, address, format=None):
        # try:
        try:
            firstname = request.data['firstname']
            lastname = request.data['lastname']
        except:
            firstname = ''
            lastname = ''
        try:
            email = request.data['email']
        except:
            email = ''
        try:
            userImageUrl = request.FILES['userImageUrl']
        except:
            userImageUrl = ''
        try:
            influencers = request.data['influencers']
        except:
            influencers = []

        current = datetime.now().date()

        UserDetailData = UserDetail.objects.filter(address__exact = address).exists()

        if UserDetailData is False:
            userData = UserDetail.objects.create(
                address             = address,
                firstname           = firstname,
                lastname            = lastname,
                email               = email,
                createdAt           = current,
                updatedAt           = current
            )

            if userImageUrl:
                fs = FileSystemStorage()
                filename = fs.save(userImageUrl.name, userImageUrl)
                uploaded_file_path = fs.path(filename)
                backetname = settings.AWS_STORAGE_BUCKET_NAME
                filePath = uploaded_file_path
                foldername = 'Users'
                deletefilename = filePath.split(os.sep)[-1]
                filename = address
                s3.meta.client.upload_file(filePath, backetname, str(foldername) + "/" + filename)
                newImageUrl = "https://{0}.s3.{1}.amazonaws.com/{2}/{3}".format(backetname, settings.AWS_S3_REGION, foldername, filename)
                
                UserDetail.objects.filter(address__exact = address).update(
                    userImageUrl            = newImageUrl,
                    updatedAt               = current
                )

                if newImageUrl:
                    removeFileFromFolder(deletefilename)

            if len(influencers) > 0:
                influencers = [int(x) for x in influencers.split(',')]
                for influencer in range(len(influencers)):
                    userData.influencers.add(influencer)
            else:
                pass
            
            resContent = {
                'erorr': False,
                'data': 'Data Created'
            }


        else:

            UserDetail.objects.filter(address__exact = address).update(
                firstname           = firstname,
                lastname            = lastname,
                email               = email,
                updatedAt           = current
            )

            if userImageUrl:
                fs = FileSystemStorage()
                filename = fs.save(userImageUrl.name, userImageUrl)
                uploaded_file_path = fs.path(filename)
                backetname = settings.AWS_STORAGE_BUCKET_NAME
                filePath = uploaded_file_path
                foldername = 'Users'
                deletefilename = filePath.split(os.sep)[-1]
                filename = address
                s3.meta.client.upload_file(filePath, backetname, str(foldername) + "/" + filename)
                newImageUrl = "https://{0}.s3.{1}.amazonaws.com/{2}/{3}".format(backetname, settings.AWS_S3_REGION, foldername, filename)
                
                UserDetail.objects.filter(address__exact = address).update(
                    userImageUrl            = newImageUrl,
                    updatedAt               = current
                )

                if newImageUrl:
                    removeFileFromFolder(deletefilename)

            if len(influencers) != 0:
                influencers = [int(x) for x in influencers.split(',')]

                for influen in range(len(influencers)):
                    updateInfluencers = UserDetail.objects.get(address = address)
                    updateInfluencers.influencers.clear()
                    updateInfluencers.influencers.add(int(influen))
                    updateInfluencers.save()


            
            resContent = {
                'erorr': False,
                'data': 'Data Updated'
            }

        return Response(resContent)
        # except:
        #     return Response(errorMsg)

    def get(self, request, address, format=None):

        userInfo = UserDetail.objects.get(address = address)
        print(userInfo.id)
        
        userData = {
            'id'                    : userInfo.id,
            'address'               : userInfo.address,
            'firstname'             : userInfo.firstname,
            'lastname'              : userInfo.lastname,
            'email'                 : userInfo.email,
            'userImageUrl'          : userInfo.userImageUrl,
            'influencers'           : userInfo.influencers,
            'createdAt'             : userInfo.createdAt,
            'updatedAt'             : userInfo.updatedAt,
        }



# userInfo = UserDetail.objects.get(address = '0x1fcd481f8a9e927a6f4ea12364c7a82db222a3ed')
# print(userInfo.influencers.id)