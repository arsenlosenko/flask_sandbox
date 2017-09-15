#!/usr/bin/env python3

import random
from gtts import gTTS


def text_to_speech(text):
    print("Recieved text")
    audio_file ='static/audio/audio_{}.mp3'.format(random.randint(1, 200))
    tts = gTTS(text=text, lang="en")
    tts.save(audio_file)
    print("TTS audio sample is ready")
    return audio_file


if __name__ == "__main__":
    text_to_speech()
