'''
App demonstrating a Text input field which accepts Arabic script in kivy

'''


import arabic_reshaper
from bidi.algorithm import get_display
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, NumericProperty, StringProperty


class Ar_text(TextInput):
    max_chars = NumericProperty(20)  # maximum character allowed
    str = StringProperty()

    def __init__(self, **kwargs):
        super(Ar_text, self).__init__(**kwargs)
        self.text = get_display(arabic_reshaper.reshape("اطبع شيئاً"))


    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return
        self.str = self.str+substring
        self.text = get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(Ar_text, self).insert_text(substring, from_undo)

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = get_display(arabic_reshaper.reshape(self.str))


class TestApp(App):

    def build(self):
        return Ar_text()


if __name__ == '__main__':
    TestApp().run()