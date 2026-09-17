from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle, RoundedRectangle


BG_PAGE = (241/255, 245/255, 249/255, 1)       # #f1f5f9
BG_CARD = (255/255, 255/255, 255/255, 1)       # #ffffff

TEXT_MAIN = (15/255, 23/255, 42/255, 1)        # #0f172a
TEXT_SUB = (100/255, 116/255, 139/255, 1)      # #64748b
BORDER = (226/255, 232/255, 240/255, 1)        # #e2e8f0

SIDEBAR_BG = (15/255, 23/255, 42/255, 1)       # #0f172a
SIDEBAR_TEXT = (148/255, 163/255, 184/255, 1)  # #94a3b8
SIDEBAR_ACTIVE = (79/255, 70/255, 229/255, 1)  # #4f46e5

PRIMARY = (79/255, 70/255, 229/255, 1)         # #4f46e5
PRIMARY_HOVER = (67/255, 56/255, 202/255, 1)   # #4338ca

BLUE = (59/255, 130/255, 246/255, 1)           # #3b82f6
BG_BLUE = (239/255, 246/255, 255/255, 1)       # #eff6ff

GREEN = (16/255, 185/255, 129/255, 1)          # #10b981
BG_GREEN = (236/255, 253/255, 245/255, 1)      # #ecfdf5

AMBER = (245/255, 158/255, 11/255, 1)          # #f59e0b
BG_AMBER = (255/255, 251/255, 235/255, 1)      # #fffbeb

RED = (239/255, 68/255, 68/255, 1)             # #ef4444
BG_RED = (254/255, 242/255, 242/255, 1)        # #fef2f2

PURPLE = (139/255, 92/255, 246/255, 1)         # #8b5cf6
BG_PURPLE = (245/255, 243/255, 255/255, 1)     # #f5f3ff

WHITE = (255/255, 255/255, 255/255, 1)


class Fundo(BoxLayout):

    def __init__(self, cor, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*cor)
            self.fundo = Rectangle(
                pos=self.pos,
                size=self.size
            )

        self.bind(
            pos=self.atualizar_fundo,
            size=self.atualizar_fundo
        )

    def atualizar_fundo(self, *args):
        self.fundo.pos = self.pos
        self.fundo.size = self.size


# =========================================================
# BOTÃO DA SIDEBAR
# =========================================================

class BotaoSidebar(Button):

    def __init__(self, ativo=False, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""

        if ativo:
            self.background_color = SIDEBAR_ACTIVE
            self.color = WHITE
        else:
            self.background_color = SIDEBAR_BG
            self.color = SIDEBAR_TEXT

        self.font_size = 14


class Participantes(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        principal = BoxLayout(
            orientation="vertical"
        )

        with principal.canvas.before:
            Color(*SIDEBAR_BG)
            principal.fundo = Rectangle(
                pos=principal.pos,
                size=principal.size
            )

        principal.bind(
            pos=lambda obj, value: setattr(
                principal.fundo, "pos", value
            ),
            size=lambda obj, value: setattr(
                principal.fundo, "size", value
            )
        )

        principal.add_widget(
            Label(
                text="Visitas ao Técnico",
                color=WHITE,
                font_size=19,
                bold=True,
                size_hint_y=None,
                height=60
            )
        )

        principal.add_widget(
            BotaoSidebar(
                text="Dashboard"
            )
        )

        principal.add_widget(
            BotaoSidebar(
                text="Visitas"
            )
        )

        principal.add_widget(
            BotaoSidebar(
                text="Nova Visita"
            )
        )

        principal.add_widget(
            BotaoSidebar(
                text="Clientes"
            )
        )

        principal.add_widget(
            BotaoSidebar(
                ativo=True,
                text="Técnicos"
            )
        )

        # Espaço
        principal.add_widget(
            Label(
                text=""
            )
        )

        principal.add_widget(
            Label(
                text="Camila Oliveira",
                color=WHITE,
                font_size=14,
                bold=True,
                size_hint_y=None,
                height=30
            )
        )

        principal.add_widget(
            Label(
                text="Administradora",
                color=SIDEBAR_TEXT,
                font_size=12,
                size_hint_y=None,
                height=25
            )
        )

        principal.add_widget(
            BotaoSidebar(
                text="Sair"
            )
        )

        conteudo = Fundo(
            cor=BG_PAGE,
            orientation="vertical"
        )

        topo = BoxLayout(
            size_hint_y=None,
            height=80,
            padding=[20, 10],
            spacing=8
        )

        titulo = BoxLayout(
            orientation="vertical"
        )

        label_titulo = Label(
            text="Participantes da Visita",
            color=TEXT_MAIN,
            font_size=23,
            bold=True,
            halign="left",
            valign="middle"
        )
        label_titulo.bind(
            size=lambda obj, value: setattr(obj, "text_size", value)
        )
        titulo.add_widget(label_titulo)

        label_subtitulo = Label(
            text="Gerencie os participantes da visita #00126",
            color=TEXT_SUB,
            font_size=13,
            halign="left",
            valign="middle"
        )
        label_subtitulo.bind(
            size=lambda obj, value: setattr(obj, "text_size", value)
        )
        titulo.add_widget(label_subtitulo)

        topo.add_widget(titulo)

        topo.add_widget(
            Button(
                text="☀",
                color=TEXT_SUB,
                background_normal="",
                background_color=BG_CARD,
                size_hint_x=None,
                width=45
            )
        )

        topo.add_widget(
            Button(
                text="☾",
                color=TEXT_SUB,
                background_normal="",
                background_color=BG_CARD,
                size_hint_x=None,
                width=45
            )
        )

        topo.add_widget(
            Button(
                text="🔔 3",
                color=TEXT_SUB,
                background_normal="",
                background_color=BG_CARD,
                size_hint_x=None,
                width=65
            )
        )

        topo.add_widget(
            Button(
                text="👤",
                color=TEXT_SUB,
                background_normal="",
                background_color=BG_CARD,
                size_hint_x=None,
                width=45
            )
        )

        conteudo.add_widget(topo)

        scroll = ScrollView()

        area = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10,
            size_hint_y=None
        )

        area.bind(
            minimum_height=area.setter("height")
        )

        area.add_widget(
            Button(
                text="← Voltar para a visita",
                color=PRIMARY,
                background_normal="",
                background_color=BG_PAGE,
                size_hint_y=None,
                height=50
            )
        )

        label_visita = Label(
            text="Visita #00126\n"
                 "26 de Setembro de 2026 - 08:00\n\n"
                 "Cliente: João da Silva\n"
                 "Técnico: Lucas Andrade",
            color=TEXT_MAIN,
            font_size=15,
            halign="left",
            valign="middle",
            size_hint_y=None,
            height=130
        )
        label_visita.bind(
            size=lambda obj, value: setattr(obj, "text_size", value)
        )
        area.add_widget(label_visita)

        botao_adicionar = Button(
            text="+ Adicionar Participante",
            color=WHITE,
            background_normal="",
            background_color=PRIMARY,
            size_hint_y=None,
            height=50
        )

        area.add_widget(botao_adicionar)

        area.add_widget(
            Label(
                text="Lista de Participantes (3)",
                color=TEXT_MAIN,
                font_size=18,
                bold=True,
                halign="left",
                size_hint_y=None,
                height=40
            )
        )

        label_p1 = Label(
            text="João da Silva\n"
                 "Função: Cliente\n"
                 "Status: Presente\n"
                 "Mais opções",
            color=TEXT_MAIN,
            font_size=14,
            halign="left",
            valign="middle",
            size_hint_y=None,
            height=80
        )
        label_p1.bind(
            size=lambda obj, value: setattr(obj, "text_size", value)
        )
        area.add_widget(label_p1)

        label_p2 = Label(
            text="Lucas Andrade\n"
                 "Função: Técnico\n"
                 "Status: Presente\n"
                 "Mais opções",
            color=TEXT_MAIN,
            font_size=14,
            halign="left",
            valign="middle",
            size_hint_y=None,
            height=80
        )
        label_p2.bind(
            size=lambda obj, value: setattr(obj, "text_size", value)
        )
        area.add_widget(label_p2)

        label_p3 = Label(
            text="Maria Souza\n"
                 "Função: Acompanhante\n"
                 "Status: Pendente\n"
                 "Mais opções",
            color=TEXT_MAIN,
            font_size=14,
            halign="left",
            valign="middle",
            size_hint_y=None,
            height=80
        )
        label_p3.bind(
            size=lambda obj, value: setattr(obj, "text_size", value)
        )
        area.add_widget(label_p3)

        area.add_widget(
            Label(
                text="Mostrando 1 a 3 de 3 participantes",
                color=TEXT_SUB,
                font_size=13,
                size_hint_y=None,
                height=40
            )
        )

        area.add_widget(
            Button(
                text="1",
                color=WHITE,
                background_normal="",
                background_color=PRIMARY,
                size_hint_y=None,
                height=40
            )
        )

        scroll.add_widget(area)

        conteudo.add_widget(scroll)

        principal.add_widget(conteudo)

        def abrir_modal(instance):

            layout = BoxLayout(
                orientation="vertical",
                padding=15,
                spacing=10
            )

            layout.add_widget(
                Label(
                    text="Adicionar Participante",
                    color=TEXT_MAIN,
                    font_size=20,
                    bold=True,
                    size_hint_y=None,
                    height=40
                )
            )

            layout.add_widget(
                Label(
                    text="Nome do Participante *",
                    color=TEXT_MAIN
                )
            )

            nome = TextInput(
                hint_text="Ex: Carlos Santos",
                multiline=False,
                size_hint_y=None,
                height=45,
                background_color=BG_CARD,
                foreground_color=TEXT_MAIN,
                hint_text_color=TEXT_SUB
            )

            layout.add_widget(nome)

            layout.add_widget(
                Label(
                    text="Função *",
                    color=TEXT_MAIN
                )
            )

            funcao = Spinner(
                text="Acompanhante",
                values=(
                    "Acompanhante",
                    "Técnico Auxiliar",
                    "Cliente"
                ),
                size_hint_y=None,
                height=45,
                background_color=BG_CARD,
                color=TEXT_MAIN
            )

            layout.add_widget(funcao)

            layout.add_widget(
                Label(
                    text="Status *",
                    color=TEXT_MAIN
                )
            )

            status = Spinner(
                text="Pendente",
                values=(
                    "Pendente",
                    "Presente",
                    "Ausente"
                ),
                size_hint_y=None,
                height=45,
                background_color=BG_CARD,
                color=TEXT_MAIN
            )

            layout.add_widget(status)

            botoes = BoxLayout(
                size_hint_y=None,
                height=50,
                spacing=10
            )

            cancelar = Button(
                text="Cancelar",
                color=TEXT_SUB,
                background_normal="",
                background_color=BORDER
            )

            adicionar = Button(
                text="Adicionar",
                color=WHITE,
                background_normal="",
                background_color=PRIMARY
            )

            botoes.add_widget(cancelar)
            botoes.add_widget(adicionar)

            layout.add_widget(botoes)

            popup = Popup(
                title="Adicionar Participante",
                content=layout,
                size_hint=(0.8, 0.8),
                background_color=BG_CARD,
                separator_color=PRIMARY
            )

            cancelar.bind(
                on_press=popup.dismiss
            )

            popup.open()

        botao_adicionar.bind(
            on_press=abrir_modal
        )

        self.add_widget(principal)