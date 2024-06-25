from fastapi import FastAPI
from pydantic import BaseModel
from deep_translator import GoogleTranslator


app = FastAPI()

class TextToTranslate(BaseModel):
    text: str
    target_language: str

@app.post("/translate/")
async def translate_text(item: TextToTranslate):
    tradutor = GoogleTranslator(source= "auto", target= item.target_language)
    traducao = tradutor.translate(item.text)
    return {"translated_text": traducao}

@app.get("/translate/{text}/{target_language}")
async def translate_text(text: str, target_language: str):
    tradutor = GoogleTranslator(source= "auto", target= target_language)
    traducao = tradutor.translate(text)
    return {"translated_text": traducao}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the translation API!"}

