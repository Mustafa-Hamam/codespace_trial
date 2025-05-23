from fastapi import FastAPI
import uvicorn
from nlp_logic.nlp import get_phrases
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "This is my Wikipedia NLP API!"}

@app.get("/wikiphrases/{name}")
async def wikiphrases(name:str):
    print("Creating Phrases for {name}")
    phrases = get_phrases(name)
    return {"Phrases are:": phrases}
if __name__=='__main__':
    uvicorn.run(app,port=10000,host='0.0.0.0')