from Qamelot.project_modules import *


def uploadFile(url, imageSubname):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    filename = url.split('/')[::-1][0]
    filename = imageSubname
    asset_image_url = url
    req_for_image = requests.get(asset_image_url, stream=True)
    file_object_from_req = req_for_image.raw
    req_data = file_object_from_req.read()

    # Do the actual upload to s3
    s3.Bucket(bucket_name).put_object(Key = 'assets_images/' + filename, Body=req_data)

    new_meta_url = 'https://%s.s3.amazonaws.com/%s' % (settings.AWS_STORAGE_BUCKET_NAME, 'assets_images/' + filename)

    return new_meta_url


