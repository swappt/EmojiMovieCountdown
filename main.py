from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.dropdown import DropDown

from time import time

adverts = True
try: #'!!!! this line should be removed upon release !!!!'
  from jnius import autoclass
except ImportError: #'!!!! this line should be removed upon release !!!!'
  adverts = False #'!!!! this line should be removed upon release !!!!'

if adverts: #'!!!! this line should be removed upon release !!!!'
  PythonActivity = autoclass('org.kivy.android.PythonActivity')
  AdBuddiz = autoclass('com.purplebrain.adbuddiz.sdk.AdBuddiz')

class CountryDrop(DropDown):
  pass


class Countdown(Widget):
  caption = ObjectProperty(None)
  selector = ObjectProperty(None)
  dropdown = ObjectProperty(None)

  time = time()
  time_emojimovie = {
    'UK': 1501804800,
    'North America': 1501200000,
    'Australia': 1505347200,
    'France': 1508284800,
    'Deutschland': 1501718400,
    'Sverige': 1502236800,
    'España': 1502409600,
    'Italia': 1511827200
  }
  
  translations = {
    'North America': ' remaining until the emoji movie is officially released in '
    'UK': ' remaining until the emoji movie is officially released in '
    'Australia': ' remaining until the emoji movie is officially released in '
    'France': ' Jusqu\'à ce que le EMOJI MOVIE soit officiellement publié en '
    'Deutschland': ' Bis der EMOJI MOVIE offiziell freigegeben wird '
    'Sverige': ' återstår tills EMOJI MOVIE är officiellt släppt i '
    'España': ' permaneciendo hasta que EMOJI MOVIE sea lanzado oficialmente en '
    'Italia': ' rimanendo fino a quando l\'EMOJI MOVIE è ufficialmente rilasciato '
  }

  country = 'North America'

  time_remaining = time_emojimovie[country] - time
  time_str = StringProperty('%.2f' % time_remaining)
  unit = 0
  units = {
    'North America': ['seconds','minutes','hours','days'],
    'UK': ['seconds','minutes','hours','days'],
    'Australia': ['seconds','minutes','hours','days'],
    'France': ['secondes', 'minutes', 'heures', 'jours'],
    'Deutschland': ['sekunden', 'minuten', 'stunden', 'tage'],
    'Sverige': ['sekunder', 'minuter', 'timmar', 'dagar'],
    'España': ['segundos', 'minutos', 'horas', 'días'],
    'Italia': ['secondi', 'minuti', 'ore', 'giorni']
  }
  def __init__(self, *args, **kwargs):
    super(Countdown,self).__init__(*args,**kwargs)
    Clock.schedule_interval(self.update,0)

  def update(self,t):
    self.time = time()
    self.time_remaining = self.time_emojimovie[self.country] - self.time
    if -86400 < self.time_remaining < 0:
      self.time_str = 'The Emoji Movie comes out today!'
      self.caption.text = ''
    elif self.time_remaining < -86400:
      self.time_str = 'You missed the party...'
      self.caption.text = 'Come back for the sequel'
    else:
      if self.unit == 0:
        self.time_str = '%.2f' % self.time_remaining
      elif self.unit == 1:
        self.time_str = '%.2f' % (self.time_remaining/60)
      elif self.unit == 2:
        self.time_str = '%.2f' % (self.time_remaining/3600)
      else:
        self.time_str = '%.2f' % (self.time_remaining/86400)

    self.caption.text = self.units[self.country[self.unit]] + self.translations[self.country] + self.country
    if self.selector.text != '':
      self.country = self.selector.text


  def change_units(self):
    print('change')
    self.unit += 1
    if self.unit >= 4:
      self.unit = 0


class EmojiApp(App):
  def build(self):
    if adverts:
      AdBuddiz.setPublisherKey('ENTER KEY')
      AdBuddiz.setTestModeActive()
      AdBuddiz.cacheAds(PythonActivity.mActivity)
      AdBuddiz.showAd(PythonActivity.mActivity)

    self.main = Countdown()
    return self.main

emoji = EmojiApp()
emoji.run()
