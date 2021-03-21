
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStore(S3Boto3Storage):
    bucket_name = 'compfit-profile-pictures'
    # location = 'media'
    # file_overwrite = False
