import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class TeaTimeGridLayout(GridLayout):
	pass



class TeaTimerApp(App):
	def build(self):
		return TeaTimeGridLayout()

teaApp = TeaTimerApp()
teaApp.run()