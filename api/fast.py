from fastapi import FastAPI

import joblib
import pandas as pd
from google.cloud import storage
# from sklearn.externals import joblib

storage_client = storage.Client()
bucket_name='wagon-data-713-velasquez'
model_bucket = 'models/mbti_predictor_first_dataset_v2/model.joblib'
model_local = 'model.joblib'

bucket = storage_client.get_bucket(bucket_name)
#select bucket file
blob = bucket.blob(model_bucket)
#download that file and name it 'local.joblib'
blob.download_to_filename(model_local)
#load that file from local file
pipeline=joblib.load(model_local)
# predict = pipeline.predict(pd.DataFrame({'posts': ['i dont know what to put in']}))
PATH_TO_LOCAL_MODEL = 'model.joblib'

# import ipdb
# ipdb.set_trace()

app = FastAPI()

# define a root `/` endpoint

@app.get("/")
def index():
    return {"greeting": "Hello world"}

@app.get("/predict")
def predict(answers):
    df_test = X_pred_transform(answers)
    print(df_test.shape)
    if "best_estimator_" in dir(pipeline):
        y_pred = pipeline.best_estimator_.predict(df_test)
    else:
        y_pred = pipeline.predict(df_test)
    print(y_pred)
    return {"prediction": str(y_pred[0])}

def X_pred_transform(answers):
    X_pred = pd.DataFrame({'posts': [answers]})
    return X_pred
