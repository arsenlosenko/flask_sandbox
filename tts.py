#!/usr/bin/env python3

from gtts import gTTS


def text_to_speech(text):
    print("Recieved text")
    tts = gTTS(text=text, lang="en")
    tts.save('test.mp3')
    print("TTS audio sample is ready")


if __name__ == "__main__":
    text_to_speech()