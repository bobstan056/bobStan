# German Speech-to-Text Analyzer

A Python application that performs **offline German speech recognition** and automatically analyzes the transcribed text.

The application converts spoken German from a `.wav` audio file into text and then provides useful text statistics.

---

## Features

- Offline German speech recognition
- WAV audio support
- Automatic text analysis
- Word count
- Sentence count
- Top 5 most frequent words
- Fast and lightweight Vosk model

---

## Technologies

- Python 3.11
- Vosk
- Wave
- JSON
- Regular Expressions (re)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your_username/speech_to_text.git
cd speech_to_text
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Download the Vosk model

The speech recognition model is **not included** in this repository because of its size.

Download it here:

https://alphacephei.com/vosk/models/vosk-model-small-de-0.15.zip

Extract the archive into the project folder so that the structure looks like this:

```
speech_to_text/
│
├── model/
│   └── vosk-model-small-de-0.15/
├── transcriber.py
├── analyzer.py
└── testSpeech.wav
```

---

## Usage

Run:

```bash
python transcriber.py
```

The application will:

1. Transcribe the speech from the audio file.
2. Count words.
3. Count sentences.
4. Display the five most frequent words.

---

## Project Structure

```
speech_to_text/
│
├── transcriber.py      # Speech recognition
├── analyzer.py         # Text analysis
├── testSpeech.wav      # Sample audio
├── model/              # Download separately
├── requirements.txt
└── README.md
```

---

## Example Output

```text
Transcription:

guten tag ich heiße thomas ich wohne in zürich heute ist das wetter sehr schön ich lerne deutsch und programmiere in python

Words: 16
Sentences: 2

Top words:
ich: 2
guten: 1
tag: 1
heute: 1
deutsch: 1
```

---

## Notes

- Only `.wav` audio files are supported.
- The Vosk model must be downloaded manually before running the project.
- The `model` directory is excluded from the repository because of its size.