import boto3


async def upload_file_to_s3(file_name: str):
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://s3.timeweb.com'
    )

    s3.upload_file(f"dist/{file_name}",
                   "3a87f907-6d7e8ead-a933-434d-9de8-4ffe3b37577c", Key=f"mejs-stats/{file_name}")

    return f"https://s3.timeweb.com/3a87f907-6d7e8ead-a933-434d-9de8-4ffe3b37577c/mejs-stats/{file_name}"
