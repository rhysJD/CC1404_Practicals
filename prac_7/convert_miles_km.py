"""
Practical 7 CP1404
Rhys Donaldson
13581558
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
MILES_TO_KMS = 1.6091

class DistanceConvert(App):
    """Converts a distance im miles to kilometres"""
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        Window.size = (500, 300)
        return self.root

    def conversion(self, input_numb):
        if input_numb.isnumeric():
            self.root.ids.output_label.text = str(float(input_numb) * MILES_TO_KMS)
        else:
            self.root.ids.output_label.text = '0.0'

    def change_numb(self, input_numb, incremant):
        """increments the number input by one"""

        if input_numb == '':
            self.root.ids.input_numb.text = str(0 + incremant)
        else:
            self.root.ids.input_numb.text = str(int(input_numb) + incremant)


DistanceConvert().run()
