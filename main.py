from kivy.app import App
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.video import Video
from kivy.core.window import Window
import time
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import label
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, NumericProperty
from datetime import date, datetime
from kivy.uix.button import Button

# pip install pillow
# pip install ffpyplayer
screen_helper = """ 
FloatLayout:
    Video:
        source : 'CardBackground.mp4'
        state : 'play'
        options : {'eos':'loop'}
        allow_stretch:True
    Image:
        source : 'goobertest3.png' 
        size_hint: {0.55,0.235}
        pos_hint:{'center_x': 0.225, 'center_y': 0.546}
    Image:
        source : 'landing.png'  
        size_hint: {1,10001} 
        pos_hint:{'center_x': 0.5, 'center_y': 0.9365}
    Image:
        source : 'Qrcode.png' 
        size_hint: {0.15001,0.15}
        pos_hint:{'center_x': 0.17, 'center_y': 0.185}
    Image:
        source : 'barcode7.png' 
        size_hint: {1.8,0.94650000001}
        pos_hint:{'center_x': 0.5, 'center_y': 0.08}
    Label:
        text: 'Santiago'
        font_size: 30
        font_name:'Time'
        color: (0,0,0,1)
        pos_hint:{'center_x': 0.72, 'center_y': 0.62}
    Label:
        text: 'Magana'
        font_size: 28
        font_name:'Time'
        color: (0,0,0,1)
        pos_hint:{'center_x': 0.72, 'center_y': 0.57}
    Label:
        text: 'Student'
        font_size: 25
        font_name:'Time'
        color: (0,0,0,1)
        pos_hint:{'center_x': 0.72, 'center_y': 0.505} 
    Label:
        text: '10'
        font_size: 19
        font_name:'Time'
        color: (0,0,0,1)
        pos_hint:{'center_x': 0.715, 'center_y': 0.455}
    Label:
        text: app.datenum
        font_name:'Time'
        color: (0,0,0,1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.35}
        font_size: 42
        outline_width: 8 
        outline_color: (1,1,1,1)
    Label:
        text: app.timenum
        font_name:'Time'
        color: (0,0,0,1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.28}
        font_size: 34
        outline_width: 8
        outline_color: (1,1,1,1)
    Image:
        source : 'homebackbutton2.png' 
        size_hint: {0.378,0.3800001}
        pos_hint:{'center_x': 0.193, 'center_y': 0.835}   
    Label: 
        text: app.clocknum
        color: (1,1,1,1) 
        pos_hint:{'center_x': 0.07, 'center_y': 0.9685}
        font_size: 10
    MDRectangleFlatButton:
        opacity: 0
        pos_hint: {'center_x': .18, 'center_y': .19}
        size_hint: {0.032001,0.071}
        on_release: app.show_qr()
    MDRectangleFlatButton:
        opacity: 0
        pos_hint: {'center_x': .5, 'center_y': .077}
        size_hint: {0.9501,0.091}
        on_release: app.show_qr()
    Image:
        text: app.opacity
        opacity: self.text 
        source : 'backgrounddark2.png' 
        size_hint: {1,1.0000001}
        pos_hint:{'center_x': 0.5, 'center_y': 0.45}
    Image:
        text: app.opacity
        opacity: self.text 
        source : 'PopupCode5.png' 
        size_hint: {0.96,0.93}
        pos_hint:{'center_x': 0.5, 'center_y': 0.45}        
    Image:
        text: app.opacity
        opacity: self.text 
        source : 'backbutton4.png' 
        size_hint: {0.26001,0.55}
        pos_hint:{'center_x': 0.137, 'center_y': 0.842}
    MDRectangleFlatButton:
        opacity: 0
        size_hint: {0.20501,0.00002}
        pos_hint:{'center_x': 0.13, 'center_y': 0.84}
        on_press:app.button_act()
    Image:
        text: app.opacity
        opacity: self.text 
        source : 'barcode12.png' 
        size_hint: {2.35,0.84} 
        pos_hint:{'center_x': 0.5, 'center_y': 0.265}
    Image:
        text: app.opacity
        opacity: self.text 
        source : 'fillerspace2.png'  
        size_hint: {2,1.0000} 
        pos_hint:{'center_x': 0.5, 'center_y': 0.18}     
    Image:
        text: app.opacity
        opacity: self.text 
        source : 'fillerspace2.png'  
        size_hint: {0.8,0.80001} 
        pos_hint:{'center_x': 0.38, 'center_y': 0.798}    
    Image:
        source : 'blackfiller.png'  
        size_hint: {0.8,5.0001} 
        pos_hint:{'center_x': 0.12, 'center_y': 0.97}    
    Image:
        source : 'blackfiller.png'  
        size_hint: {0.8,5.0001} 
        pos_hint:{'center_x': 0.17, 'center_y': 0.97}    
    Image:
        source : 'blackfiller.png'  
        size_hint: {0.8,8.0001} 
        pos_hint:{'center_x': 0.27, 'center_y': 0.97}    
    Image:
        source : 'blackfiller.png'  
        size_hint: {0.8,8.0001} 
        pos_hint:{'center_x': 0.77, 'center_y': 0.97}    
    Image:
        source : 'blackfiller.png'  
        size_hint: {0.8,8.0001} 
        pos_hint:{'center_x': 0.9, 'center_y': 0.97}
    Label:
        opacity: app.num_opacity
        text: '610075434' 
        font_size: 15
        color: (0,0,0,1)
        pos_hint:{'center_x': 0.5, 'center_y': 0.19} 








"""


class VideoWindow(MDApp):
    opacity = NumericProperty()
    num_opacity = NumericProperty()
    timenum = StringProperty()
    datenum = StringProperty()
    clocknum = StringProperty()
    month = StringProperty()

    def timevalue(self):
        val = "gay"  # StringProperty(self.TimeValue)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        LabelBase.register(name='Time', fn_regular='TitilliumWeb-Black.ttf')
        LabelBase.register(name='Number', fn_regular='NotoSansDisplay-Regular.ttf')
        screen = Builder.load_string(screen_helper)
        return screen

    def on_start(self):
        # crudeclock = IncrediblyCrudeClock()
        Clock.schedule_interval(self.update_date, 1)
        Clock.schedule_interval(self.update_time, 1)
        Clock.schedule_interval(self.update_clocktime, 1)
        from firebase import firebase
        firebase = firebase.FirebaseApplication('https://animschoolcard-default-rtdb.firebaseio.com/', None)
        data = {'Usercode': '',
                'Password': ''}
        firebase.post('https://animschoolcard-default-rtdb.firebaseio.com/-Users', data)
        self.root.current = 'home'
        # return crudeclock

    # class IncrediblyCrudeClock(Label):
    def update_clocktime(self, *args):
        h = time.strftime("%H")
        m = time.strftime("%M")
        self.clocknum = h + ":" + m

    def update_time(self, *args):
        h = time.strftime("%H")
        m = time.strftime("%M")
        s = time.strftime("%S")
        # self.text = h+":"+m+":"+s
        self.timenum = h + ":" + m + ":" + s

    def update_date(self, *args):
        Y = time.strftime("%Y")
        M = time.strftime("%m")
        D = time.strftime("%d")
        # self.datenum = time.asctime()
        # self.datenum = str(datetime.)
        if M == '01':
            self.month = 'Jan  '
        if M == '02':
            self.month = 'Feb '
        if M == '03':
            self.month = 'Mar '
        if M == '04':
            self.month = 'Apr '
        if M == '05':
            self.month = 'May '
        if M == '06':
            self.month = 'Jun '
        if M == '07':
            self.month = 'Jul '
        if M == '08':
            self.month = 'Aug '
        if M == '09':
            self.month = 'Sep '
        if M == '10':
            self.month = 'Oct '
        if M == '11':
            self.month = 'Nov '
        if M == '12':
            self.month = 'Dec '
        self.datenum = self.month + "" + D + "," + Y

    def show_qr(self):
        self.opacity = 100
        self.num_opacity = 1

    def button_act(self):
        self.opacity = 0
        self.num_opacity = 0



root = VideoWindow()
root.run()
# if __name__ == "__main__":
#   VideoWindow().run()

