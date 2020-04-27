import sqlite3

from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang.builder import Builder
import os
from kivymd.theming import ThemeManager


class Mathematics(Screen):
    pass


class English(Screen):
    pass


class Civic(Screen):
    pass


class Islamic(Screen):
    pass


class Arabic(Screen):
    pass


class Setting(Screen):
    pass


list_of_subject = []
with open('subject.txt', 'rt') as f:
    for n in f.readlines():
        list_of_subject.append(n)


class CreateSubject(Screen):
    theme_cls = ThemeManager()
    createSub = ObjectProperty(None)
    sub = ObjectProperty(None)

    def createSubject(self):
        subject = self.sub.text.upper()
        list_of_subject.append(subject)
        subject_file = open('subject.txt', 'at')
        subject_file.write(subject + '\n')
        subject_file.close()
        conn = sqlite3.connect('{}.db'.format(subject))
        c = conn.cursor()
        # creating subject table
        query = """CREATE TABLE SUBJECT (
                   QUESTION VARCHAR NOT NULL(250),
                   QUESTION_NO INT NOT NULL (250),
                   OPTION1 VARCHAR NOT NULL(250),
                   OPTION2 VARCHAR NOT NULL (250),
                   OPTION3 VARCHAR NOT NULL(250),
                   OPTION4 VARCHAR NOT NULL (250),
                   ANSWER VARCHAR NOT NULL (250));"""
        print(query)
        c.execute('''CREATE TABLE SUBJECT(
                   QUESTION VARCHAR NOT NULL(250),
                   QUESTION_NO INT NOT NULL (250),
                   OPTION1 VARCHAR NOT NULL(250),
                   OPTION2 VARCHAR NOT NULL (250),
                   OPTION3 VARCHAR NOT NULL(250),
                   OPTION4 VARCHAR NOT NULL (250),
                   ANSWER VARCHAR NOT NULL(250));''')
        conn.commit()
        l = Label(text=subject)
        r = GridLayout(cols=1, rows=1)
        r.add_widget(l)
        p = Popup(title='SUBJECT', size_hint=(.7, 0.7), background_color=(0, 0, .9, .5), auto_dismiss=True)
        p.add_widget(r)
        p.open()


class CreateQuestion(Screen):
    theme_cls = ThemeManager()
    createSub = ObjectProperty(None)
    sub = ObjectProperty(None)
    drops = ObjectProperty(None)
    menu_but = ObjectProperty(None)
    list_of_subject = []
    with open('subject.txt', 'rt') as f:
        for n in f.readlines():
            list_of_subject.append(n)
    list_subject = tuple(list_of_subject)

    def dropdown(self):
        drops = DropDown()
        for index in list_of_subject:
            btn = Button(text=index)
            btn.bind(on_release=lambda btn: drops.select(btn.text))
            drops.add_widget(btn)
        self.ids.menu_but.bind(on_release=drops.open)

        # self.ids.sub.text = self.ids.menu_but.text
        return drops.open(self)

    def createQuestion(self):
        subject = self.sub.text.upper()
        question = self.ids.question.text
        question_no = self.ids.question_no.text
        option1 = self.ids.option1.text
        option2 = self.ids.option2.text
        option3 = self.ids.option3.text
        option4 = self.ids.option4.text
        answer = self.ids.answer.text
        conn = sqlite3.connect('{}.db'.format(subject))
        c = conn.cursor()
        c.execute('INSERT INTO {}_TABLE(QUESTION,QUESTION_NO,OPTION1,OPTION2,OPTION3,OPTION4,ANSWER) VALUES(?,?,?,?,'
                  '?,?,?,?)'.format(subject), (question, question_no, option1, option2, option3, option4, answer))

        l = Label(text=question + " " + option1)
        p = Popup(title='SUBJECT', size_hint=(.7, 0.7), background_color=(0, 0, .9, .5), auto_dismiss=True)
        p.add_widget(l)
        p.open()


class Register(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""


class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""
