import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# from kivy.uix.image import Image


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        # Grid Layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1

        # Second grid Layout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # Input Box
        self.top_grid.add_widget(Label(
            text="Entrez vos prenoms au format 'prenom1 prenom2 ...': "))
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)
        self.top_grid.add_widget(Label(
            text="Entrez le nom du pere au format 'nom': "))
        self.nameF = TextInput(multiline=False)
        self.top_grid.add_widget(self.nameF)
        self.top_grid.add_widget(Label(
            text="Entrez le nom de la mére au format 'nom': "))
        self.nameM = TextInput(multiline=False)
        self.top_grid.add_widget(self.nameM)
        self.top_grid.add_widget(Label(
            text="Entrez votre date de naissance au format 'JJ.MM.AAAA': "))
        self.bd = TextInput(multiline=False)
        self.top_grid.add_widget(self.bd)

        # Add the top grid to app
        self.add_widget(self.top_grid)

        # Submit Button
        self.submit = Button(text="Submit", font_size=42)
        # Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        nameF = self.nameF.text
        nameM = self.nameM.text
        bd = self.bd.text

        # Clear input box
        self.name.text = ""
        self.nameF.text = ""
        self.nameM.text = ""
        self.bd.text = ""

        # Print value to the screen
        self.add_widget(
            Label(
                text=f'Welcome {name} {nameF, nameM}, you are born the {bd}!'))


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
