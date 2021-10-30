import speech_recognition as sr
import sys

def command():
    r = sr.Recognizer()#объект на основе sr

    with sr.Microphone() as source:#слушаем микрофон и сохраняем данные
        print("Можете говорить")
        r.pause_threshold = 1 #ожидание 1 сек
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source) #слушаем

        try:
            com = r.recognize_google(audio).lower()
            print("Вы сказали: " + com)
        except sr.UnknownValueError:
            print("Не удалось распознать, повторите еще раз.")
            com = command()
        return com


def makesmth(com):
    if 'stop' in com:
        print("Да, конечно.Окончание программы.")
        sys.exit()

while True:
    makesmth(command())

