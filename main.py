from fastapi import FastAPI
import uvicorn
from nlp_logic.nlp import get_phrases , get_sentiment, analyze_txt_sntmnt
import textblob
from textblob.exceptions import MissingCorpusError

try:
    _ = textblob.TextBlob("test").noun_phrases
except MissingCorpusError:
    import textblob.download_corpora
    textblob.download_corpora.download_all()
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "This is my Wikipedia NLP API!"}

@app.get("/wikiphrases/{name}")
def wikiphrases(name:str):
    print("Creating Phrases for {name}")
    phrases = get_phrases(name)
    return {"Phrases are:": phrases}

@app.get("/sentiment/{name}")
def seniment_analysis(name:str):
    print(f"analyzing sentiment of topic {name}")
    sentiment = get_sentiment(name)
    return {"The sentiment analysis result is:": sentiment}

@app.get("txtSentiment/{txt}")
def text_sentiment(txt:str):
    print("Analyzing your text")
    sentmnt = analyze_txt_sntmnt(txt)
    return {"The sentiment analysis result is:": sentmnt}

if __name__=='__main__':
    uvicorn.run(app,port=10000,host='0.0.0.0')