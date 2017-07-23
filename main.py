import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

from kivy.lang import Builder



class TeaTimerLayout(FloatLayout):
	pass



class TeaTimerApp(App):
	def build(self):

 		##Window.clearcolor = (1, 1, 1, 1)
		return TeaTimerLayout()

teaApp = TeaTimerApp()
teaApp.run()