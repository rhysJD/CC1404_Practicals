"""
Practical 7 CP1404
Rhys Donaldson
13581558
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.greet.text = "Greetings " + self.root.ids.input_name.text

    def handle_clear(self):
        self.root.ids.greet.text = 'Enter your name'
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
