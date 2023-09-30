from pydantic import BaseModel
from service.api.api import main_router
from fastapi import FastAPI
import onnxruntime as rt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(main_router)

m = rt.InferenceSession("service/xtremedistill_quantized.onnx", providers=['CPUExecutionProvider'])