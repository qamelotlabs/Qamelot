from WebAPI.project_modules import *


def uploadFile(url, imageSubname):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    filename = url.split('/')[::-1][0]
    asset_image_url = url
    req_for_image = requests.get(asset_image_url, stream=True)
    file_object_from_req = req_for_image.raw
    req_data = file_object_from_req.read()

    # Do the actual upload to s3
    s3.Bucket(bucket_name).put_object(Key = 'assets_images/' + filename, Body=req_data)

    new_meta_url = 'https://%s.s3.amazonaws.com/%s' % (settings.AWS_STORAGE_BUCKET_NAME, 'assets_images/' + filename)

    return new_meta_url


datas_collections = Assets.objects.filter(collection__in=['ETHEREUM:0xb66a603f4cfe17e3d27b87a8bfcad319856518b8', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0x652800879f36ff9ed254fc663dfd0fdccc48d1d8', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0x670646a8373886d8c8e0d525bd15f92c6f765fa5', 'ETHEREUM:0x670646a8373886d8c8e0d525bd15f92c6f765fa5', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xb66a603f4cfe17e3d27b87a8bfcad319856518b8', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xb66a603f4cfe17e3d27b87a8bfcad319856518b8', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xb66a603f4cfe17e3d27b87a8bfcad319856518b8', 'ETHEREUM:0xf6793da657495ffeff9ee6350824910abc21356c', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xb66a603f4cfe17e3d27b87a8bfcad319856518b8', 'ETHEREUM:0xb66a603f4cfe17e3d27b87a8bfcad319856518b8', 'ETHEREUM:0xa85cf0d66719be023260c0e7d0304aa66f4e9d2d', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xc9154424b823b10579895ccbe442d41b9abd96ed', 'ETHEREUM:0xf4121a2880c225f90dc3b3466226908c9cb2b085', 'ETHEREUM:0xedc3ad89f7b0963fe23d714b34185713706b815b', 'ETHEREUM:0xdaa7ae5edae17929d2cb06cfc20913097b14e28f'])

collectionsList = []
for cdata in datas_collections:
    print('c_address: ', cdata.id)
    # collectionsList.append(cdata)
    # snav_timetable_url      = "https://api.rarible.org/v0.1/collections/{}".format(cdata.collection)
    # collections_response    = requests.get(snav_timetable_url).json()
    # collectionsList.append(collections_response)

# print('collectionsList: ', collectionsList)
