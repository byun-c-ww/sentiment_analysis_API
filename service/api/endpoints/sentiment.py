from fastapi import APIRouter
from service.core.logic.onnx_inference import sentiment_analyzer
from service.core.schema.output import APIOutput
from service.core.schema.input import APIInput
sentiment_router = APIRouter()

@sentiment_router.post('/analyze',response_model=APIOutput)
async def sentiment(input:APIInput):
    return sentiment_analyzer(input.text)