from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Mengatur ukuran jendela simulasi tampilan HP
Window.size = (360, 640)

class HomeScreen(Screen):
    """Halaman Utama / Beranda"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Layout utama berorientasi vertikal
        layout = BoxLayout(
            orientation='vertical',
            padding=30,
            spacing=15
        )
        
        # Judul Aplikasi
        layout.add_widget(Label(
            text="Aplikasi Saya",
            font_size='28sp',
            bold=True,
            size_hint=(1, 0.3)
        ))
        
        # Tombol Navigasi ke Halaman Fitur
        btn_feature = Button(
            text="Buka Fitur Utama",
            font_size='18sp',
            size_hint=(1, 0.15),
            background_color=(0.2, 0.6, 1, 1)
        )
        btn_feature.bind(on_press=self.go_to_feature)
        layout.add_widget(btn_feature)
        
        # Tombol Navigasi ke Halaman Pengaturan
        btn_settings = Button(
            text="Pengaturan",
            font_size='18sp',
            size_hint=(1, 0.15),
            background_color=(0.5, 0.5, 0.5, 1)
        )
        btn_settings.bind(on_press=self.go_to_settings)
        layout.add_widget(btn_settings)
        
        # Space kosong di bawah
        layout.add_widget(BoxLayout(size_hint=(1, 0.4)))
        
        self.add_widget(layout)

    def go_to_feature(self, instance):
        self.manager.current = 'feature'

    def go_to_settings(self, instance):
        self.manager.current = 'settings'


class FeatureScreen(Screen):
    """Halaman Fitur Utama"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(
            orientation='vertical',
            padding=30,
            spacing=15
        )
        
        layout.add_widget(Label(
            text="Halaman Fitur",
            font_size='24sp',
            size_hint=(1, 0.3)
        ))
        
        # Deskripsi atau konten fitur
        layout.add_widget(Label(
            text="Area kerja/layar fitur utama.",
            font_size='16sp',
            size_hint=(1, 0.5)
        ))
        
        # Tombol Kembali
        btn_back = Button(
            text="Kembali ke Beranda",
            font_size='16sp',
            size_hint=(1, 0.15),
            background_color=(0.9, 0.3, 0.3, 1)
        )
        btn_back.bind(on_press=self.go_back)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'home'


class SettingsScreen(Screen):
    """Halaman Pengaturan"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(
            orientation='vertical',
            padding=30,
            spacing=15
        )
        
        layout.add_widget(Label(
            text="Pengaturan",
            font_size='24sp',
            size_hint=(1, 0.3)
        ))
        
        layout.add_widget(Label(
            text="Opsi konfigurasi aplikasi.",
            font_size='16sp',
            size_hint=(1, 0.5)
        ))
        
        btn_back = Button(
            text="Kembali ke Beranda",
            font_size='16sp',
            size_hint=(1, 0.15),
            background_color=(0.9, 0.3, 0.3, 1)
        )
        btn_back.bind(on_press=self.go_back)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'home'


class MainApp(App):
    """Aplikasi Utama"""
    def build(self):
        self.title = "Kivy Application"
        
        # Manajer Layar untuk mengatur perpindahan antar layar
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(FeatureScreen(name='feature'))
        sm.add_widget(SettingsScreen(name='settings'))
        
        return sm


if __name__ == '__main__':
    MainApp().run()
    
