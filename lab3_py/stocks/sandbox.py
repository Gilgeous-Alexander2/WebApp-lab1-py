from minio import Minio
# from minio.error import ResponseError
# Initialize MinIO client
minio_client = Minio(
    endpoint="192.168.0.101:9000",
    access_key='minioadmin',
    secret_key='minioadmin',
    secure=False)
# Create a new bucket
bucket_name = "logo"
# try:
minio_client.make_bucket(bucket_name)
print(f"Bucket '{bucket_name}' created successfully.")
# except ResponseError as err:
#     print(err)