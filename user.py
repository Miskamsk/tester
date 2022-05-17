from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
import pyspeedtest

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

class LoginScreen(Widget):
    

    email = StringProperty()
    label = ObjectProperty()


    def login(self):
        try:
            test = pyspeedtest.SpeedTest(self.email)
            a = str(round(test.ping()))
            self.label.text = a
        except:
            b = 'Ошибка'
            self.label.text = b


    
    



class UserApp(App):

    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    UserApp().run()