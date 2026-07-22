# Transcription API

REST API built with FastAPI exposing speech transcription
and text analysis functionality.

## Endpoints

- GET  /              — health check
- POST /analyze-text  — analyze text (words, sentences, top words)
- POST /transcribe    — upload WAV file, transcribe and save to DB
- GET  /history       — retrieve all transcriptions

## Setup

pip install fastapi uvicorn python-multipart

## Run

uvicorn api.main:app --reload

Open http://localhost:8000/docs for interactive documentation.

## Stack
- FastAPI
- Vosk (offline German speech recognition)
- SQLite
- Python