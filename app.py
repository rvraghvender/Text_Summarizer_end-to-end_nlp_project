from fastapi import FastAPI
import uvicorn
import sys 
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from text_summarizer.pipeline.prediction import PredictionPipeline
from text_summarizer.logging.exception import CustomException
from text_summarizer.logging.logger import logging

text: str = "What is Text summarization?"

app = FastAPI()

@app.get('/', tags=['authentication'])
async def index():
    return RedirectResponse(url='/docs')

@app.get('/train')
async def training():
    try:
        os.system('python main.py')
        return Response('Training successful')
    except Exception as e:
        logging.exception(e)
        return Response(f'Error occured! {e}')
    
@app.post('/predict')
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        logging.exception(e)
        raise CustomException(e, sys)
    
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)