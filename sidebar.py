from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle


# Cores do seu CSS
SIDEBAR_BG = (15/255, 23/255, 42/255, 1)       # #0f172a
SIDEBAR_TEXT = (148/255, 163/255, 184/255, 1)  # #94a3b8
SIDEBAR_ACTIVE = (79/255, 70/255, 229/255, 1)  # #4f46e5
WHITE = (255/255, 255/255, 255/255, 1)


class Sidebar(BoxLayout):

    def __init__(self, tela_atual="", **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.size_hint_x = None
        self.width = 220
        self.padding = 15
        self.spacing = 8

        # Fundo da sidebar
        with self.canvas.before:
            Color(*SIDEBAR_BG)
            self.fundo = Rectangle(
                pos=self.pos,
                size=self.size
            )

        self.bind(
            pos=self.atualizar_fundo,
            size=self.atualizar_fundo
        )

        # Nome do sistema
        self.add_widget(
            Label(
                text="Visitas ao Técnico",
                color=WHITE,
                font_size=20,
                bold=True,
                size_hint_y=None,
                height=60
            )
        )

        # Menu
        self.adicionar_botao(
            "Dashboard",
            "dashboard",
            tela_atual
        )

        self.adicionar_botao(
            "Visitas",
            "visitas",
            tela_atual
        )

        self.adicionar_botao(
            "Nova Visita",
            "nova_visita",
            tela_atual
        )

        self.adicionar_botao(
            "Clientes",
            "clientes",
            tela_atual
        )

        self.adicionar_botao(
            "Técnicos",
            "tecnicos",
            tela_atual
        )

        # Espaço antes do perfil
        self.add_widget(
            Label(
                text="",
            )
        )

        # Perfil
        self.add_widget(
            Label(
                text="Camille Oliveira",
                color=WHITE,
                font_size=15,
                bold=True,
                size_hint_y=None,
                height=30
            )
        )

        self.add_widget(
            Label(
                text="Administradora",
                color=SIDEBAR_TEXT,
                font_size=12,
                size_hint_y=None,
                height=25
            )
        )

        # Sair
        self.adicionar_botao(
            "Sair",
            "login",
            tela_atual
        )

    def adicionar_botao(self, texto, tela, tela_atual):

        botao = Button(
            text=texto,
            color=WHITE if tela == tela_atual else SIDEBAR_TEXT,
            background_normal="",
            background_color=(
                SIDEBAR_ACTIVE
                if tela == tela_atual
                else (0, 0, 0, 0)
            ),
            size_hint_y=None,
            height=45
        )

        botao.bind(
            on_press=lambda x: self.ir_para(tela)
        )

        self.add_widget(botao)

    def ir_para(self, tela):

        if self.parent and hasattr(self.parent, "manager"):
            self.parent.manager.current = tela

    def atualizar_fundo(self, *args):

        self.fundo.pos = self.pos
        self.fundo.size = self.size