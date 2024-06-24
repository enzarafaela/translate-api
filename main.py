from fastapi import FastAPI
from pydantic import BaseModel
from deep_translator import GoogleTranslator


app = FastAPI()

class TextToTranslate(BaseModel):
    text: str

@app.post("/translate/")
async def translate_text(item: TextToTranslate):
    tradutor = GoogleTranslator(source= "en", target= "pt")
    traducao = tradutor.translate(item.text)
    return {"translated_text": traducao}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the translation API!"}

