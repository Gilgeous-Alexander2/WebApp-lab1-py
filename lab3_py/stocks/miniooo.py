from django.conf import settings
from minio import Minio
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.response import *

def process_file_upload(file_object: InMemoryUploadedFile, client, image_name):
    try:
        client.put_object('logo', image_name, file_object, file_object.size)
        return f"http://localhost:9000/logo/{image_name}"
    except Exception as e:
        return {"error": str(e)}

def add_pic(new_stock, pic):
    client = Minio(           
            endpoint='localhost:9000',
           access_key='minioadmin',
           secret_key='minioadmin',
           secure=False
    )
    i = new_stock.id
    img_obj_name = f"{i}.png"

    if not pic:
        return Response({"error": "Нет файла для изображения логотипа."})
    result = process_file_upload(pic, client, img_obj_name)

    if 'error' in result:
        return Response(result)

    new_stock.url = result
    new_stock.save()

    return Response({"message": "success"})