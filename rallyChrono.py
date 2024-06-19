from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivy.uix.widget import Widget
from datetime import datetime, timedelta
from kivy.core.window import Window

class CalcoloOrario(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.input_partenza_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.input_partenza_layout.add_widget(MDLabel(text="Ora Corrente (HH:MM):", halign='center'))
        self.add_widget(self.input_partenza_layout)

        # Prima riga: Ora Corrente (HH)
        self.ora_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.ora_input = MDTextField(hint_text="HH", input_filter='int', size_hint=(1, None), height=30)
        self.ora_layout.add_widget(self.ora_input)
        self.minuti_input = MDTextField(hint_text="MM", input_filter='int', size_hint=(1, None), height=30)
        self.ora_layout.add_widget(self.minuti_input)
        self.add_widget(self.ora_layout)

        self.input_trasferimento_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.input_trasferimento_layout.add_widget(MDLabel(text="Minuti al Prossima C.O:", halign='center'))
        self.add_widget(self.input_trasferimento_layout)

        # Terza riga: Minuti alla Prossima Tappa
        self.minuti_prossima_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.ore_prossima_input = MDTextField(hint_text="Ore", text="0", input_filter='int', size_hint=(1, None), height=30)
        self.minuti_prossima_layout.add_widget(self.ore_prossima_input)
        self.minuti_prossima_input = MDTextField(hint_text="Minuti", input_filter='int', size_hint=(1, None), height=30)
        self.minuti_prossima_layout.add_widget(self.minuti_prossima_input)
        self.add_widget(self.minuti_prossima_layout)

        # Quarta riga: Bottone di calcolo
        self.calcola_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.calcola_button = MDRaisedButton(text="Calcola")
        self.calcola_button.bind(on_press=self.calcola_orario)
        self.calcola_layout.add_widget(self.calcola_button)
        self.add_widget(self.calcola_layout)

        # Quinta riga: Risultato
        self.risultato_label = MDLabel(text="", halign='center')
        self.add_widget(self.risultato_label)

    def calcola_orario(self, instance):
        try:
            ora_corrente = int(self.ora_input.text)
            minuti_correnti = int(self.minuti_input.text)
            ore_alla_prossima_tappa = int(self.ore_prossima_input.text)
            minuti_prossima_tappa = int(self.minuti_prossima_input.text)

            orario_corrente_dt = datetime.strptime(f"{ora_corrente}:{minuti_correnti}", "%H:%M")
            prossimo_orario_dt = orario_corrente_dt + timedelta(hours=ore_alla_prossima_tappa, minutes=minuti_prossima_tappa)
            prossimo_orario_str = prossimo_orario_dt.strftime("%H:%M")

            self.risultato_label.text = f"Il prossimo controllo orario è alle: {prossimo_orario_str}"
        except ValueError:
            self.risultato_label.text = "Errore: inserisci valori validi."

class RallyChronosApp(MDApp):
    def build(self):
        Window.size = (320, 640)
        return CalcoloOrario()

if __name__ == '__main__':
    RallyChronosApp().run()
