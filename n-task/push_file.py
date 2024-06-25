import os
from minio import Minio
from minio.error import S3Error

# Настройки MinIO
MINIO_ENDPOINT = "localhost:9000"
MINIO_ACCESS_KEY = "ROOTUSER"
MINIO_SECRET_KEY = "CHANGEME123"
BUCKET_NAME = "my-bucket"
FILE_PATH = "README.md"

# Создаем клиент MinIO
client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

# Создаем bucket, если он еще не существует
try:
    if not client.bucket_exists(BUCKET_NAME):
        client.make_bucket(BUCKET_NAME)
except S3Error as exc:
    print("Ошибка при создании bucket:", exc)
    exit(1)

# Загружаем файл в MinIO
try:
    client.fput_object(
        BUCKET_NAME,
        os.path.basename(FILE_PATH),
        FILE_PATH
    )
    print(f"Файл {FILE_PATH} успешно загружен в MinIO.")
    print(f"Зайди сюда http://172.17.0.2:9001/browser/{BUCKET_NAME}")
except S3Error as exc:
    print("Ошибка при загрузке файла:", exc)
    exit(1)
