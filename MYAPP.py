from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Window.clearcolor=(1, 1, 1, 1)

class MYAPP(App): #class name should be same as your project name 
	def build(self):
	  l=BoxLayout(orientation='vertical')
	  l.add_widget(Button(text="touch me"))
	  return l
	  return Label(text="HELLO WORLD\n")
	
	
MYAPP().run()