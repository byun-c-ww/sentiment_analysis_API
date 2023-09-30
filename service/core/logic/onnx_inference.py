import onnxruntime as rt
import transformers
import numpy as np
import time
import service.app as s
import logging

from transformers import BertTokenizerFast

model_id = "microsoft/xtremedistil-l6-h256-uncased"
tokenizer = BertTokenizerFast.from_pretrained(model_id)

def sentiment_analyzer(text):

    time_init = time.time()

    try:
        inputs = tokenizer(text,padding='max_length',max_length=512,truncation=True,return_tensors="np")
        onnx_pred = s.m.run(["logits"], {'input_ids':inputs['input_ids'],
                                    'token_type_ids':inputs['token_type_ids'],
                                    'attention_mask':inputs['attention_mask']})
        
        if onnx_pred[0][0][1]>onnx_pred[0][0][0]:
            review="positive"
        else:
            review="negative"
        
        time_elapsed = time.time() - time_init
        return {
            "emotion": review,
            "time_elapsed": str(time_elapsed)
        }
    except Exception as e:
        return logging.exception("error occured from onnx_inference.py file (actual logic handling file)!!! error:")

