"""
Practical 7 CP1404
Rhys Donaldson
13581558
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_list = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Walter White", "Jesse Pinkman", "Arya Starkk"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_label()
        return self.root

    def create_label(self):
        for name in self.name_list:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabels().run()
