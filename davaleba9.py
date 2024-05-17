from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class TabularForm(GridLayout):
    def __init__(self, **kwargs):
        super(TabularForm, self).__init__(**kwargs)

        # Define the number of columns
        self.cols = 2

        # Labels and TextInputs
        labels_texts = ['Name:', 'Age:', 'Gender:']
        for label_text in labels_texts:
            self.add_widget(Label(text=label_text))
            self.add_widget(TextInput())


        


class TabularFormApp(App):
    def build(self):
        return TabularForm()


if __name__ == '__main__':
    TabularFormApp().run()
