#-*- coding:utf-8 -*-

from command import CheckCommand
from speech import MakeAudio, SpeechToText
from os import remove
from os.path import isfile
from keyboard import read_hotkey



if __name__ == "__main__":
    print("음성인식을 하려면 Ctrl+Shift 를 눌러주세요.")
    while True:
        try:
            rk = read_hotkey(suppress=False)
            if rk == 'ctrl+shift':

                print("10초간 인식합니다~")
                MakeAudio()
                print("10초간 인식 완료~")

                text = SpeechToText()
                CheckCommand(Text=text)

        except:
            print("에러 발생~")
            break
        
        finally:
            if isfile('sirius_cmd.wav'):
                remove('sirius_cmd.wav')