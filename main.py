from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login import Login
from dashboard import Dashboard
from nova_visita import NovaVisita
from visitas import Visitas
from detalhes import Detalhes
from participantes import Participantes

class VisitasApp(App):

    def build(self):

        telas = ScreenManager()

        telas.add_widget(Login(name="login"))
        telas.add_widget(Dashboard(name="dashboard"))
        telas.add_widget(NovaVisita(name="nova_visita"))
        telas.add_widget(Visitas(name="visitas"))
        telas.add_widget(Detalhes(name="detalhes"))
        telas.add_widget(Participantes(name="participantes"))

        telas.current = "dashboard"

        return telas


if __name__ == "__main__":
    VisitasApp().run()