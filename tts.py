#!/usr/bin/env python3

from gtts import gTTS


def text_to_speech_demo():
    tts = gTTS(text="Hello", lang="en")
    tts.save('hello.mp3')


if __name__ == "__main__":
    text_to_speech_demo()