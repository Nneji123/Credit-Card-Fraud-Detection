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


model = joblib.load('model.pkl')

@app.get('/')
def home():
    return {'Title': 'Credit Card Fraud Detection API'}
																	
class fraudDetection(BaseModel):
    LIMIT_BAL:float	
    SEX	:float
    EDUCATION:float	
    MARRIAGE:float	
    AGE:float	
    PAY_0:float	
    PAY_2:float	
    PAY_3:float	
    PAY_4:float
    PAY_5:float
    PAY_6:float	
    BILL_AMT1:float	
    PAY_AMT1:float	
    PAY_AMT2:float	
    PAY_AMT3:float
    PAY_AMT4:float
    PAY_AMT5:float
    PAY_AMT6:float

@app.post('/predict')
def predict(data : fraudDetection):
                                                                                                                                                                                                                                
    features = np.array([[data.LIMIT_BAL, data.SEX, data.EDUCATION, data.MARRIAGE, data.AGE, data.PAY_0, data.PAY_2, data.PAY_3, data.PAY_4, data.PAY_5, data.PAY_6, data.BILL_AMT1, data.PAY_AMT1, data.PAY_AMT2, data.PAY_AMT3, data.PAY_AMT4, data.PAY_AMT5, data.PAY_AMT6]])
    model = joblib.load('model.pkl')

    predictions = model.predict(features)
    if predictions == 1:
        return {"This Person committing fraudulent credit card transactions."}
    elif predictions == 0:
        return {"This person is not committing fraudulent transactions."}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    model = joblib.load('model.pkl')
    contents = await file.file.read()
    buffer = BytesIO(contents)
    df = pd.read_csv(StringIO(str(buffer.file.read(), 'utf-16')), encoding='utf-16')
    #df1 = df.to_numpy()
    #predictions = model.predict(df1)
    #predictions_list = pd.DataFrame(predictions, columns = ["Predictions"])
    buffer.close()
    #return predictions_list
    
    
    return df.to_dict(orient='records')