from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
import json
from datetime import datetime

KV = '''
ScreenManager:
    MainScreen:
    CallScreen:

<MainScreen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        MDTopAppBar:
            title: "Dating & Call App"
            elevation: 4

        MDCard:
            orientation: 'vertical'
            padding: 15
            size_hint: 1, None
            height: "100dp"
            md_bg_color: 0.9, 0.9, 1, 1

            MDLabel:
                text: "Saldo Koin Anda:"
                font_style: "Subtitle2"
            MDLabel:
                id: coin_label
                text: "75 Koin"
                font_style: "H4"
                bold: True

        MDLabel:
            text: "Pilih Host / Penerima Telepon:"
            font_style: "H6"

        MDScrollView:
            MDGridLayout:
                id: hosts_grid
                cols: 1
                spacing: 10
                size_hint_y: None
                height: self.minimum_height
                padding: 10

        MDSeparator:

        MDLabel:
            text: "Top Up Koin Hemat (Murah):"
            font_style: "Subtitle1"

        MDGridLayout:
            cols: 2
            spacing: 10
            size_hint: 1, None
            height: "120dp"

            MDRectangleFlatIconButton:
                icon: "cash"
                text: "Rp2.000 (30 Koin)"
                on_release: app.buy_coins(2000, 30)

            MDRectangleFlatIconButton:
                icon: "cash"
                text: "Rp5.000 (75 Koin)"
                on_release: app.buy_coins(5000, 75)

<CallScreen>:
    name: 'call'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20

        MDTopAppBar:
            title: "Panggilan Berjalan"
            elevation: 4

        MDCard:
            orientation: 'vertical'
            padding: 20
            size_hint: 1, None
            height: "150dp"
            md_bg_color: 0.2, 0.6, 0.8, 1

            MDLabel:
                text: "Terhubung dengan:"
                font_style: "Subtitle2"
                color: 1, 1, 1, 1
            MDLabel:
                id: host_name
                text: "Host Name"
                font_style: "H4"
                bold: True
                color: 1, 1, 1, 1

            MDLabel:
                id: call_timer
                text: "00:00"
                font_style: "H5"
                color: 1, 1, 1, 1
                halign: "center"

            MDLabel:
                id: cost_label
                text: "Biaya: 0 Koin"
                font_style: "Subtitle1"
                color: 1, 1, 1, 1

        MDBoxLayout:
            size_hint_y: None
            height: "50dp"
            spacing: 10

            MDRaisedButton:
                text: "Akhiri Panggilan"
                on_release: app.end_call()

<HostCard>:
    orientation: 'horizontal'
    size_hint_y: None
    height: "80dp"
    padding: 10
    spacing: 10

    MDBoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.7

        MDLabel:
            text: root.host_name
            font_style: "Subtitle1"
            bold: True
        MDLabel:
            text: root.host_rate + "/Min"
            font_style: "Body2"

    MDRaisedButton:
        text: "Mulai VC"
        size_hint_x: 0.3
        on_release: app.start_call(root.host_name, root.host_rate_value)
'''

class HostCard(MDBoxLayout):
    def __init__(self, host_name, host_rate, host_rate_value, **kwargs):
        super().__init__(**kwargs)
        self.host_name = host_name
        self.host_rate = host_rate
        self.host_rate_value = host_rate_value

class MainScreen(MDScreen):
    def on_enter(self):
        self.refresh_hosts()
        self.update_coin_display()

    def refresh_hosts(self):
        self.ids.hosts_grid.clear_widgets()
        hosts = self.manager.app.get_hosts()
        for host in hosts:
            card = HostCard(
                host['name'],
                f"Rp{host['rate_per_min']}",
                host['rate_per_min']
            )
            self.ids.hosts_grid.add_widget(card)

    def update_coin_display(self):
        coins = self.manager.app.get_user_coins()
        self.ids.coin_label.text = f"{coins} Koin"

class CallScreen(MDScreen):
    def on_enter(self):
        self.call_start_time = datetime.now()
        self.call_rate = 0
        self.update_timer()

    def update_timer(self):
        if self.manager.current == 'call':
            elapsed = (datetime.now() - self.call_start_time).total_seconds()
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            self.ids.call_timer.text = f"{minutes:02d}:{seconds:02d}"
            
            cost = (elapsed / 60) * self.call_rate
            self.ids.cost_label.text = f"Biaya: {int(cost)} Koin"
            
            Clock.schedule_once(lambda dt: self.update_timer(), 1)

class DatingCallApp(MDApp):
    dialog = None
    user_coins = 75
    call_active = False
    current_call_host = None
    current_call_rate = 0

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_string(KV)

    def get_hosts(self):
        """Fetch available hosts - replace with API call later"""
        return [
            {'name': 'Siska', 'rate_per_min': 20},
            {'name': 'Diana', 'rate_per_min': 25},
            {'name': 'Sarah', 'rate_per_min': 15},
        ]

    def get_user_coins(self):
        return self.user_coins

    def buy_coins(self, amount, coins):
        """Process coin purchase"""
        self.user_coins += coins
        self.show_dialog(
            f"Pembelian {coins} koin seharga Rp{amount:,} berhasil!",
            f"Total Koin: {self.user_coins}"
        )
        # Update display
        if self.root.current == 'main':
            main_screen = self.root.get_screen('main')
            main_screen.update_coin_display()

    def start_call(self, host_name, rate_per_min):
        """Start a call with selected host"""
        if self.user_coins < rate_per_min:
            self.show_dialog("Koin Tidak Cukup", f"Anda membutuhkan minimal {rate_per_min} koin untuk panggilan ini")
            return
        
        self.call_active = True
        self.current_call_host = host_name
        self.current_call_rate = rate_per_min
        
        call_screen = self.root.get_screen('call')
        call_screen.ids.host_name.text = host_name
        call_screen.call_rate = rate_per_min
        call_screen.call_start_time = datetime.now()
        
        self.root.current = 'call'

    def end_call(self):
        """End the active call and charge coins"""
        if not self.call_active:
            return
        
        call_screen = self.root.get_screen('call')
        elapsed = (datetime.now() - call_screen.call_start_time).total_seconds()
        minutes = elapsed / 60
        
        cost = int(minutes * self.current_call_rate)
        
        self.user_coins -= cost
        self.call_active = False
        
        self.show_dialog(
            "Panggilan Berakhir",
            f"Durasi: {int(minutes)} menit\nBiaya: {cost} Koin\nSaldo Tersisa: {self.user_coins} Koin"
        )
        
        self.root.current = 'main'

    def show_dialog(self, title, message):
        """Show a dialog with message"""
        if not self.dialog:
            self.dialog = MDDialog(
                title=title,
                text=message,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=lambda x: self.dialog.dismiss()
                    )
                ],
            )
        else:
            self.dialog.title = title
            self.dialog.text = message
        self.dialog.open()

if __name__ == '__main__':
    DatingCallApp().run()
          
