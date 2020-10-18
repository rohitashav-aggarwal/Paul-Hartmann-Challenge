from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy_garden.mapview import MapView
from kivy.clock import Clock

import sqlite3

import googlemaps
from datetime import datetime


gmaps = googlemaps.Client(key='AIzaSyDJ7X3ASt6OYsTaI8-STefczKFmf2A7_HQ')


class LoginScreen(Screen):
    pass


class PatientsScreen(Screen):
    pass


class VitalsScreen(Screen):
    pass


class MapScreen(Screen):
    getting_patients_timer = None

    #def start_getting_patients_in_fov(self):
        #After one second get patients in field of view.
        #try:
            #self.getting_patients_timer.cancel()
        #except:
            #pass

        #self.getting_patients_timer = Clock.schedule_once(self.get_patients_in_fov, 1)

    #def get_patients_in_fov(self, *args):
        #print(self.get_bbox())

class WindowManager(ScreenManager):
    pass


class curaeDomo(MDApp):
    connection = None
    cursor = None

    def __init__(self, **kwargs):
        self.title = "Curae Domo"
        self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)

    #def on_start(self):
        #Init GPS

        #Connect to DB

        #self.connection = sqlite3.connect("pharmacies.db")
        #self.cursor = self.connection.cursor()

    def build(self):
        self.root = Builder.load_file("main.kv")


if __name__ == "__main__":
    curaeDomo().run()
