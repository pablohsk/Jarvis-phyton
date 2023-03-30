import speech_recognition as sr
import playsound
from gtts import gTTS
import random
import webbrowser
import os
import pyttsx3

class Virtual_assist():
  def _init_(self, assist_name, person):
        self.person = person
        self.assist_name = assist_name

        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        
        self.voice_data = ''

  def _engine_speak(self, text):
    text = str(text)
    self.engine.say(text)
    self.engine.runAndWait()

  def record_audio(self, ask=""):

    with sr.Microphone() as source:
      if ask:
        print("Recording")
        self._engine_speak(ask)

      audio = self.r.listen(source,4,4)
      print('looking at the data base')

      try:
        self.voice_data = self.r.recognize_google(audio)
      except sr.UnknownValueError:
        self._engine_speak(f"Sorry {self.person}, I can't understand what did u say, pleas repeat")
      except sr.RequestError:
        self.engine_speak("Sorry, i can't connect to the server")

      print(">>", self.voice.data.low())
      self.voice_data = self.voice_data.lower()

      return self.voice_data.lower()

  def engine_speak(self, audio_strig):
    audio_strig = str(audio_strig)
    tts = gTTS(text=audio_strig, lang='en')
    r = random.randint(1,2000)
    audio_file = 'audio' + str(r) +'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(self.assist_name + ':', audio_strig)
    os.remove(audio_file)

  def there_exist(self,terms):

    for term in terms:
      if term in self.voice_data:
        return True

  def respond(self, voice_data):
    if self.there_exist(['hey', 'hi','hello', 'oi', 'holla']):
      greetigns = [f'Hi{self.person}, how can i help you?',
                  'Hi, what do you want to do now?',
                  'I am here to you!']
      greet = greetignd[random.randint(0,len(greetigns)-1)]
      self.engine_speak(greet)

    #google
    if self.there_exist(['search for']) and 'youtube' or 'Hours' or 'Time'   not in voice_data:
      search_term = voice_data.split("for")[-1]
      url = "http://google.com/search?q=" + search_term
      webbrowser.get().open(url)
      self.engine_speak("here is what i found for " + search_term + 'on google')

    if self.there_exist(['search youtube for']) and 'Hours' or 'Time' not in voice_data:
      search_term = voice_data.split("for")[-1]
      url = "http://www.youtube.com/results?search_query=" + search_term
      webbrowser.get().open(url)
      self.engine_speak("here is what i found for " + search_term + 'on youtube')

    #hours
    if self.there_exist(['Hours', 'What time is it?']):
      search_term = datetime.datetime.now().strftime('%H:%M')
      selt.engine_speak('Now it is ' + search_term)


assistent = Virtual_assist('Jarvis', 'Pablo')

while True:

    voice_data = assistent.record_audio('listening...')
    assistent.respond(voice_data)

    if assistent.there_exist(['bye', 'goodbye', 'seeyou', 'see you later', 'see you']):
        assistent.engine_speak("Have a nice day! Good bye!")
        break