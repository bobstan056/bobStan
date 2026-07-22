import shutil
import os
import sys
sys.path.append("../speech-to-text")
from database.database import init_db, save_transcription, get_all
from fastapi import FastAPI, UploadFile
from analyzer import count_words, count_sentences, top_words
from transcriber import transcribe


app = FastAPI()
init_db()


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/analyze-text")
def analyze_text(text: str):
    words = count_words(text)
    sentences = count_sentences(text)
    top_words_result = top_words(text, n=10)
    return {"words": words,
            "sentences": sentences,
            "top_words": top_words_result}


@app.get("/history")
def history():
    rows = get_all()
    result = []
    for row in rows:
        dictionary = {
            "id": row[0],
            "filename": row[1],
            "text": row[2],
            "words": row[3],
            "sentences": row[4],
            "date": row[5]
        }
        result.append(dictionary)
    return result

@app.post("/transcribe")
async def transcribe_audio(file:UploadFile):

    temp_path = f"temp_{file.filename}"
    with open(temp_path,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = transcribe(temp_path)


    words = count_words(text)
    sentences = count_sentences(text)
    save_transcription(file.filename, text, words, sentences)


    os.remove(temp_path)

    return {
       "filename": file.filename,
       "text": text,
       "words": words,
       "sentences": sentences
    }


