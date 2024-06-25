Здесь мы попробуем запустить локально S3 `minio`.

В целом, что такое S3 и почему он нам нужен -- информации много всякой в интернетах, но вот например [от Яндекса](https://yandex.cloud/ru/docs/glossary/s3?utm_referrer=https%3A%2F%2Fwww.google.com%2F).

Чтобы поднять `minio` - воспользуемся `Docker` образом.

```
mkdir -p ./minio/data

docker run \
   -p 9000:9000 \
   -p 9001:9001 \
   --user $(id -u):$(id -g) \
   --name minio1 \
   -e "MINIO_ROOT_USER=ROOTUSER" \
   -e "MINIO_ROOT_PASSWORD=CHANGEME123" \
   -v ./minio/data:/data \
   quay.io/minio/minio server /data --console-address ":9001"
```

Если вдруг вы грохнули случайно 
