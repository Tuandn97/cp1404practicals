"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to km
Name: Dao Ngoc Tuan
ID: 14399066
Started 04/10/2023
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Dao Ngoc Tuan'
MIlES_KM_THRESHOLD = 1.60934


class ConvertMileKmApp(App):
    """ConvertMileKmApp is a Kivy App for converting mile to km """

    def build(self):
        """Build the Kivy app from the kv file"""
        Window.size = (450, 300)
        self.title = "Convert Mile to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """Handle converting (could be button press or other call), output result to label widget """
        value = self.get_valid_input()
        result = value ** MIlES_KM_THRESHOLD
        self.root.ids.output_label.text = str(result)

    def handle_change_value(self, change):
        """Handle the Up and Down button, update the new_value and auto convert """
        value = self.get_valid_input() + change
        self.root.ids.input_number.text = str(value)
        self.handle_convert()

    def get_valid_input(self):
        """Get the valid value, if the value error return the 0 value"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMileKmApp().run()
