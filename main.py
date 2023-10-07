from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

class Abaro(MDApp):

	def build(self):
		mainscreen = ScreenManager()
		mainscreen.add_widget(Builder.load_file("main.kv"))
		mainscreen.add_widget(Builder.load_file("signin.kv"))
		mainscreen.add_widget(Builder.load_file("signup.kv"))

		return mainscreen


if __name__=="__main__":
		Abaro().run()

