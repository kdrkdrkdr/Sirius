import pyaudio
from wave import open as WAVOPEN
from speech_recognition import AudioFile, Recognizer, UnknownValueError
from pyttsx3 import init as TTS
from time import sleep


START_WORDS = ['시리우스']


FORMAT = pyaudio.paInt16

CHANNELS = 1

RATE = 16000

CHUNK = 1024

RECORD_SECONDS = 10

WAVE_OUTPUT_FILENAME = "sirius_cmd.wav"



def MakeAudio():
    
    audio = pyaudio.PyAudio()
    inputDevice = audio.get_default_input_device_info()['name']

    for i in range(audio.get_device_count()):
        infos = audio.get_device_info_by_index(i)
        if infos['name'] == inputDevice:
            devIndex = infos['index']
            break


    stream = audio.open(
        format=pyaudio.paInt16, 
        channels=CHANNELS, 
        rate=RATE, 
        input=True, 
        input_device_index=devIndex,
        frames_per_buffer=CHUNK
    )


    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)


    stream.stop_stream()
    stream.close()
    audio.terminate()


    waveFile = WAVOPEN(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()


def SpeechToText():
    try:
        rec = Recognizer()

        with AudioFile(WAVE_OUTPUT_FILENAME) as AudioSrc:
            content = rec.record(AudioSrc)
        

        text = rec.recognize_google(
            audio_data=content,
            language='ko-KR',
        )

        mainText = str(text)
        print('main-> ', mainText)
        
        return mainText

        # for sW in START_WORDS:
        #     if mainText.startswith(sW):
        #         return mainText.split(sW)[1]
                

    except ( UnknownValueError ):
        print("SPEECH ERROR!")
        return False


def TextSpeech(Text):
    engine = TTS()

    engine.setProperty('rate', 150)
    rate = engine.getProperty('rate')

    engine.setProperty('volume', 0.7)
    volume = engine.getProperty('volume')
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
    engine.say(Text)
    engine.runAndWait()
    engine.stop()
