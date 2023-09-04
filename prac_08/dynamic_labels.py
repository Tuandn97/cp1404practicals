"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of dictionary
Dao Ngoc Tuan, first version: 04/10/2023
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):
    """Main program"""

    def __init__(self, **kwargs):
        """Construct  main App"""
        super().__init__(**kwargs)
        self.list_color = ["Absolute Zero", "Acid Green", "AliceBlue", "Aliza-rin crimson", "Amaranth", "Amber",
                           "Amethyst", "AntiqueWhite", "Aqua", "Army Green"]

    def build(self):
        """Build the kivy GUI"""
        self.title = "Dynamic Label"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create Label from data and add them to the GUI"""
        for color in self.list_color:
            temp_label = Label(text=color)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelApp().run()
