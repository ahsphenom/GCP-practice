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