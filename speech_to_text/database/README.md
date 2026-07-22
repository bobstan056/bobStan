# Transcription Database

SQLite storage for speech transcription results.

## Functions
- init_db() — create database and table
- save_transcription() — save result with metadata
- get_all() — retrieve full history

## Schema
id | filename | text | words | sentences | date