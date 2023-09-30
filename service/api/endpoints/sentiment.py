from fastapi import APIRouter
from service.core.logic.onnx_inference import sentiment_analyzer
from service.core.schema.output import APIOutput
from service.core.schema.input import APIInput
import logging
sentiment_router = APIRouter()

@sentiment_router.post('/analyze',response_model=APIOutput)
async def sentiment(input:APIInput):
    try:
        result = sentiment_analyzer(input.text)
        return result
    except Exception as e:
        return logging.exception("error occured from sentiment.py file (w only router)!!! error:")