'''
App demonstrating a Text input field which accepts Arabic script in kivy

'''


import arabic_reshaper
from bidi.algorithm import get_display
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, NumericProperty, StringProperty

# You can have KV language in a file named test.kv 
# if your app Name is TestAppand comment line
# `Builder.load_string(KV)` 

KV = """
<Ar_text@TextInput>:
    text: "whatever"
    multiline: 0
    size_hint: 1,1
    font_name: "data/unifont-14.0.02.ttf" # the font you want to use
    font_size: 26
    padding_y: [15,0] # can be changed
    padding_x: [self.size[0]-self._get_text_width(max(self._lines, key=len), self.tab_width, self._label_cached)-10,8]
"""

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
        Builder.load_string(KV)
        return Ar_text()


if __name__ == '__main__':
    TestApp().run()
