from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty

adverts = True
try: #'!!!! this line should be removed upon release !!!!'
  from jnius import autoclass
except ImportError: #'!!!! this line should be removed upon release !!!!'
  adverts = False #'!!!! this line should be removed upon release !!!!'

if adverts: #'!!!! this line should be removed upon release !!!!'
  PythonActivity = autoclass('org.kivy.android.PythonActivity')
  AdBuddiz = autoclass('com.purplebrain.adbuddiz.sdk.AdBuddiz')

class EmojiApp(App)
  def build(self):
    if adverts:
      AdBuddiz.setPublisherKey('ENTER KEY')
      AdBuddiz.setTestModeActive()
      AdBuddiz.cacheAds(PythonActivity.mActivity)
      AdBuddiz.showAd(PythonActivity.mActivity)

    self.m = Manager()
    return m

emoji = EmojiApp()
emoji.run()
