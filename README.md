# GCP-practice
gcloud functions deploy hello_gcs --runtime python39 --trigger-resource demo_pipeline12 --trigger-event google.storage.object.finalize --set-env-vars TEMPLATE_PATH='gs://demo_pipeline12/demo_pipeline.json' --service-account 1077505172445-compute@developer.gserviceaccount.com