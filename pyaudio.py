import pyttsx3


engine = pyttsx3.init()

def say_it(text):
    engine.say(text)
    engine.runAndWait()

if __name__=='__main__':
    msg = '''Hello from espeak'''
    say_it(msg)