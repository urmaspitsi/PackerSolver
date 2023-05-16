Solver for 3D bin packing problem

to run locally use command:
  uvicorn main:app --reload

google cloud deploy:
  command line inside root directory:
    gcloud app deploy --project packer-331115 -v {version number, integer value}

  reference:
    https://cloud.google.com/sdk/gcloud/reference/app/deploy

  assumes Google Cloud SDK installation:
    https://cloud.google.com/sdk/docs/quickstart


solver algorithm:
  Main algorithm code is taken from: https://github.com/enzoruiz/3dbinpacking
  Original code is slighly modified.