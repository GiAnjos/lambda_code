import boto3
import json

def get_latest_file_with_example(files):
    latest_file = None

# This part of the code finds the lastest files in a folder. One of then has a diffent suffix then the other so thats why it has an "if".    
    for file in files:
        file_path = file['Key']
        file_name = file_path.split('/')[-1]                       
        if 'EXAMPLE' in file_name:
            if latest_file:
                latest_file_date = latest_file['LastModified']
                file_date = file['LastModified']
                if file_date > latest_file_date:
                    latest_file = file
            else:
                latest_file = file

    return latest_file


def get_latest_file_without_example(files):
    latest_file = None

    for file in files:
        file_path = file['Key']
        file_name = file_path.split('/')[-1]
        if 'EXAMPLE' not in file_name:
            if latest_file:
                latest_file_date = latest_file['LastModified']
                file_date = file['LastModified']
                if file_date > latest_file_date:
                    latest_file = file
            else:
                latest_file = file

    return latest_file

def lambda_handler(event, context):
    S3_BUCKET = 's3'
    GLUE_WORKFLOW = 'glue'
    OLD_FOLDER_PATH = 'OLDEST FOLDER' 
    NEW_FOLDER_PATH = 'NEWEST FOLDER'
    GLUE_JOB1_NAME = 'NAME OF THE FIRST JOB OF THE FIST WORKFLOW'
    GLUE_JOB2_NAME = 'NAME OF THE FIRST JOB OF THE SECOND WORKFLOW'

    # Parse bucket name from event
    BUCKET_NAME = event['Records'][0]['s3']['bucket']['name']

    s3_client = boto3.client(S3_BUCKET)
    s3_resource = boto3.resource(S3_BUCKET)
    glue_client = boto3.client(GLUE_WORKFLOW)

#After finding the lastest files the code moves the files to another folder inside of AWS S3. There is no code in the boto3 library that moves the files so we need to copy the files to the new folder and then delete the files from the old folder.  
    
    # Get all files from s3
    response = s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix=OLD_FOLDER_PATH)
    files = response['Contents']

    # With EXAMPLE COPY to new location and DELETE from old location
    with_example = get_latest_file_with_example(files)
    with_example_old_path = with_example['Key']
    with_example_file_name = with_example_old_path.split('/')[-1]
    source = {
        'Bucket': BUCKET_NAME,
        'Key': with_example_old_path
    }
    s3_resource.meta.client.copy(source, bucket_name, new_path + with_example_file_name)
    s3_resource.Object(bucket_name, with_example_old_path).delete()

    # Without EXAMPLE COPY to new location and DELETE from old location
    without_example = get_latest_file_without_example(files)
    without_example_old_path = without_example['Key']
    without_example_file_name = without_example_old_path.split('/')[-1]
    source = {
        'Bucket': BUCKET_NAME,
        'Key': without_example_old_path 
    }
    s3_resource.meta.client.copy(source, bucket_name, new_path + without_example_file_name)
    s3_resource.Object(bucket_name, without_example_old_path).delete()
    
# This part of the code is responsable for the workflows. It starts the workflows inside of the AWS Glue.
    try:
        response = glue_client.start_job_run(JobName=GLUE_JOB1_NAME)
        status = glue.get_job_run(JobName=gluejobname, RunId=response['JobRunId'])
        print("Job Status : ", status['JobRun']['JobRunState'])

        response = glue_client.start_job_run(JobName=GLUE_JOB2_NAME)
        status = glue.get_job_run(JobName=gluejobname, RunId=response['JobRunId'])
        print("Job Status : ", status['JobRun']['JobRunState'])
    except Exception as e:
        print(e)

    return { "statusCode": 200,
             "body": "It works!!"
    }