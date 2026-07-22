# Transkriptions-API

REST-API mit FastAPI für Sprachtranskription und Textanalyse.

## Endpunkte

- GET  /              — Status prüfen
- POST /analyze-text  — Text analysieren (Wörter, Sätze, Top-Wörter)
- POST /transcribe    — WAV-Datei hochladen, transkribieren und speichern
- GET  /history       — Alle Transkriptionen abrufen

## Installation

pip install fastapi uvicorn python-multipart

## Starten

uvicorn api.main:app --reload

Dokumentation: http://localhost:8000/docs

## Stack
- FastAPI
- Vosk (offline deutsches Sprachmodell)
- SQLite
- Python