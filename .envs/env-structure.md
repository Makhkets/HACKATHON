# Структура .env файлов

## .django

- DB_HOST=db
- DB_PORT=
- DB_PASSWORD=
- DB_USER=
- DB_NAME=
- GMAIL_PASSWORD= Google App Key
- FRONTEND_URL= For example: https://app.wellbe.club
- DEBUG= True / False
- SECRET_KEY= Django Secret Key
- DAILY_CO_TOKEN= Можно получить в личном кабинете Daily
- EMAIL_HOST_USER=example@mail.com
- EMAIL_HOST=smtp.gmail.com
- EMAIL_PORT=587
- SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=
- SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=
- CLOUDPAYMENTS_PUBLIC_KEY=
- CLOUDPAYMENTS_SECRET_KEY=
- TELEGRAM_BOT_TOKEN=
- USE_S3=TRUE
- AWS_ACCESS_KEY_ID=
- AWS_SECRET_ACCESS_KEY=
- AWS_STORAGE_BUCKET_NAME=
- SMS_RU_API_TOKEN=
- SOCIAL_SECRET=
- RABBIT_USER=user
- RABBIT_PASSWORD=password
- CELERY_BROKER_URL=pyamqp://user:password@rabbit:5672

## .postgres

- POSTGRES_HOST=db
- POSTGRES_PORT=5432
- POSTGRES_USER=user
- POSTGRES_PASSWORD=password
- POSTGRES_DB=django_db

## .pgadmin_env

- PGADMIN_DEFAULT_EMAIL=example@mail.com
- PGADMIN_DEFAULT_PASSWORD=password
- PGADMIN_LISTEN_PORT=9090

## cert.pem

## key.pem