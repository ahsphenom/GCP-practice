from google.cloud import aiplatform
import os

def hello_gcs(event,context):
    print('Running Pipeline')
    PROJECT_ID = 'qp-gcp-training-2021-07' 
    REGION = 'us-central1'                             
    PIPELINE_ROOT = 'gs://demo_pipeline12' 


    # Create a PipelineJob using the compiled pipeline from pipeline_spec_uri
    aiplatform.init(
        project=PROJECT_ID,
        location=REGION,
    )
    job = aiplatform.PipelineJob(
        display_name='demo_pipeline',
        template_path=os.getenv('TEMPLATE_PATH'),
        pipeline_root=PIPELINE_ROOT,
        enable_caching=False,
    )

    # Submit the PipelineJob
    job.submit()
    
    #Deploying cloud function and triggering the pipeline through cloud shell CLI
    gcloud functions deploy hello_gcs --runtime python39 --trigger-resource demo_pipeline12 --trigger-event google.storage.object.finalize 
    --set-env-vars TEMPLATE_PATH='gs://demo_pipeline12/demo_pipeline.json' --service-account 1077505172445-compute@developer.gserviceaccount.com
