# Project Guestbook

## Environment Variables
> [!IMPORTANT]
> Certain environment variables MUST be set for the container to run.
> Environment variables can be supplied when the container runs using a `.env` file or using local environment 
> variables set in the runtime.
> 
> The required variables include:
> 
> * `SECRET_KEY` A random Django secret key. See [Django Documentation: Secret Key](https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-SECRET_KEY)
> * `ENVIRONMENT` Defaults to "development"
> * `ALLOWED_HOSTS` Can be set to `*`

> [!NOTE]
> Optional Environment variables include:
> 
> * `DEBUG`
> * `DATABASE_URL` Complete PostgreSQL connection string
> * `DATA_STORE` Can be set to `S3`, `BLOBSTORAGE`, `AURORA`, `AZURESQL`. 
> 
> If a database is set such as `AURORA` or `AZURESQL` a `DATABASE_URL` variable MUST be set!
> 
> * `AWS_S3_ACCESS_KEY`
> * `AWS_S3_SECRET_KEY`


## Running the container
To run the container locally (assuming you have a `.env` file, run:

`docker run --env-file ./.env -it -p 8000:8000 projectguestbook`
