
from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import StreamingResponse, FileResponse
import uvicorn
import joblib
import numpy as np
from pydantic import BaseModel
import io
import pandas as pd
from io import BytesIO, StringIO


app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="""An API that utilises a Machine Learning model that detects if a credit card transaction is fraudulent or not based on the following features: age, gender, blood pressure, smoke, coughing, allergies, fatigue etc.""",
    version="0.1.0", debug=True)


model = joblib.load('credit_fraud.pkl')

@app.get('/')
def home():
    return {'Title': 'Credit Card Fraud Detection API'}
																	
class fraudDetection(BaseModel):
    step:int
    types:int
    amount:float	
    oldbalanceorig:float	
    newbalanceorig:float	
    oldbalancedest:float	
    newbalancedest:float	
    isflaggedfraud:float


@app.post('/predict')
def predict(data : fraudDetection):
                                                                                                                                                                                                                                
    features = np.array([[data.step, data.types, data.amount, data.oldbalanceorig, data.newbalanceorig, data.oldbalancedest, data.newbalancedest, data.isflaggedfraud]])
    model = joblib.load('credit_fraud.pkl')

    predictions = model.predict(features)
    if predictions == 1:
        return {"fraudulent"}
    elif predictions == 0:
        return {"not fraudulent"}

# @app.post("/upload")
# async def upload(file: UploadFile = File(...)):
#     model = joblib.load('model.pkl')
#     contents = await file.file.read()
#     buffer = BytesIO(contents)
#     df = pd.read_csv(StringIO(str(buffer.file.read(), 'utf-16')), encoding='utf-16')
#     #df1 = df.to_numpy()
#     #predictions = model.predict(df1)
#     #predictions_list = pd.DataFrame(predictions, columns = ["Predictions"])
#     buffer.close()
#     #return predictions_list
    
    
#     return df.to_dict(orient='records')