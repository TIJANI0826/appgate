import kivy
import sqlite3
from kivy.app import App
from kivy.properties import NumericProperty, ObjectProperty
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivymd.theming import ThemeManager
from kivymd.list import MDList, OneLineListItem, \
    OneLineAvatarListItem, OneLineIconListItem, ThreeLineListItem, \
    TwoLineListItem
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.time_picker import MDTimePicker
from kivy.uix.image import Image
from Practice.APPGATE.screens import Mathematics, English, Civic, Islamic, Arabic
from Practice.APPGATE.mathematicsscreen import *
from Practice.APPGATE.englishscreens import *
from Practice.APPGATE.civicscreens import *
from Practice.APPGATE.islamicscreen import *
from Practice.APPGATE.arabicscreens import *
import datetime


class CreateQuestion(StackLayout):
    def __init__(self, characters_dict_list, **kwargs):
        super(CreateQuestion, self).__init__(**kwargs)
        self.characters_dict_list = characters_dict_list
        self.list_widget = self.dict_to_label_list()

    def dict_to_label_list(self):
        list_widget = StackLayout()
        for i in self.characters_dict_list:
            list_widget.add_widget(Label(text=i['name'], size_hint =[1.0,0.1,10]))
            list_widget.add_widget(Image(source=i[img],size_hint=[1.0,0.1,10]))
        return list_widget


class First(Screen):
    pass


class Second(Screen):
    pass


class MainAppScreen(BoxLayout):
    createSub = ObjectProperty(None)
    sub = ObjectProperty(None)


class MainApp(App):
    theme_cls = ThemeManager()
    createSub = ObjectProperty(None)
    sub = ObjectProperty(None)

    def build(self):
        return MainAppScreen()


    # def timekeeper(self):
    #     for x in range(20):
    #         self.root.ids.timed.text = str(x)
    #     return self.root.ids.timed.text
    #


if __name__ == '__main__':
    MainApp().run()
