from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from gtts import gTTS
import os
import uuid
from db import saveVoice
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_ORIGIN")]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str
    
@app.post("/text-to-speech/")
async def text_to_speech(request: TextRequest, background_tasks: BackgroundTasks):
    text = request.text
    print("passé")
    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    filename = f"{uuid.uuid4()}.mp3"

    tts = gTTS(text=text, lang='fr')
    tts.save(filename)

    response = FileResponse(filename, media_type="audio/mpeg")
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    
    background_tasks.add_task(cleanup, filename)

    saveVoice.rendeur_de_requetes(text, filename)
    return response

def cleanup(filename: str):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} a été supprimé.")
    else:
        print(f"{filename} n'existe pas.")
