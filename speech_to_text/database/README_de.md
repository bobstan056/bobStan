# Transkriptions-Datenbank

SQLite-Speicher für Sprachtranskriptionsergebnisse.

## Funktionen
- init_db() — Datenbank und Tabelle erstellen
- save_transcription() — Ergebnis mit Metadaten speichern
- get_all() — gesamte Historie abrufen

## Datenbankstruktur
id | filename | text | words | sentences | date