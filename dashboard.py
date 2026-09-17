from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.screenmanager import Screen


BG_PAGE = (241/255, 245/255, 249/255, 1)       # #f1f5f9
BG_CARD = (255/255, 255/255, 255/255, 1)       # #ffffff
TEXT_MAIN = (15/255, 23/255, 42/255, 1)        # #0f172a
TEXT_SUB = (100/255, 116/255, 139/255, 1)      # #64748b
BORDER = (226/255, 232/255, 240/255, 1)        # #e2e8f0

SIDEBAR_BG = (15/255, 23/255, 42/255, 1)       # #0f172a
SIDEBAR_TEXT = (148/255, 163/255, 184/255, 1)  # #94a3b8
SIDEBAR_ACTIVE = (79/255, 70/255, 229/255, 1)  # #4f46e5

PRIMARY = (79/255, 70/255, 229/255, 1)         # #4f46e5
PRIMARY_HOVER = (67/255, 56/255, 202/255, 1)  # #4338ca

BLUE = (59/255, 130/255, 246/255, 1)           # #3b82f6
BG_BLUE = (239/255, 246/255, 255/255, 1)       # #eff6ff

GREEN = (16/255, 185/255, 129/255, 1)          # #10b981
BG_GREEN = (236/255, 253/255, 245/255, 1)      # #ecfdf5

AMBER = (245/255, 158/255, 11/255, 1)          # #f59e0b
BG_AMBER = (255/255, 251/255, 235/255, 1)      # #fffbeb

RED = (239/255, 68/255, 68/255, 1)             # #ef4444
BG_RED = (254/255, 242/255, 242/255, 1)        # #fef2f2

PURPLE = (139/255, 92/255, 246/255, 1)         # #8b5cf6
BG_PURPLE = (245/255, 243/255, 255/255, 1)

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


class BotaoArredondado(Button):

    def __init__(self, cor_fundo, raio=8, **kwargs):
        super().__init__(
            background_normal="",
            background_down="",
            **kwargs
        )

        self.cor_fundo = cor_fundo
        self.raio = raio

        with self.canvas.before:
            Color(*self.cor_fundo)
            self.fundo = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[self.raio]
            )

        self.bind(
            pos=self.atualizar_fundo,
            size=self.atualizar_fundo
        )

    def atualizar_fundo(self, *args):
        self.fundo.pos = self.pos
        self.fundo.size = self.size


class Dashboard(Screen):

    def __init__(self, **kwargs):
        super().__init__(
            **kwargs
        )

        with self.canvas.before:
            Color(*BG_PAGE)
            self.fundo = Rectangle(
                pos=self.pos,
                size=self.size
            )

        self.bind(
            pos=self.atualizar_fundo,
            size=self.atualizar_fundo
        )

        # =========================================================
        # Container principal: sidebar + conteúdo lado a lado
        # =========================================================

        principal = BoxLayout(
            orientation="horizontal"
        )

        sidebar = Fundo(
            SIDEBAR_BG,
            orientation="vertical",
            size_hint_x=None,
            width=250,
            padding=12,
            spacing=5
        )

        titulo = Label(
            text="Visitas ao Técnico",
            color=WHITE,
            font_size=16,
            bold=True,
            size_hint_y=None,
            height=50
        )

        dashboard = BotaoArredondado(
            SIDEBAR_ACTIVE,
            text="Dashboard",
            color=WHITE,
            size_hint_y=None,
            height=45
        )

        visitas = BotaoArredondado(
            SIDEBAR_BG,
            text="Visitas",
            color=SIDEBAR_TEXT,
            size_hint_y=None,
            height=45
        )

        nova_visita = BotaoArredondado(
            SIDEBAR_BG,
            text="Nova Visita",
            color=SIDEBAR_TEXT,
            size_hint_y=None,
            height=45,
            on_release=self.abrir_nova_visita
        )

        clientes = BotaoArredondado(
            SIDEBAR_BG,
            text="Clientes",
            color=SIDEBAR_TEXT,
            size_hint_y=None,
            height=45
        )

        tecnicos = BotaoArredondado(
            SIDEBAR_BG,
            text="Técnicos",
            color=SIDEBAR_TEXT,
            size_hint_y=None,
            height=45
        )

        sidebar.add_widget(titulo)
        sidebar.add_widget(dashboard)
        sidebar.add_widget(visitas)
        sidebar.add_widget(nova_visita)
        sidebar.add_widget(clientes)
        sidebar.add_widget(tecnicos)

        principal.add_widget(sidebar)

        conteudo = BoxLayout(
            orientation="vertical",
            padding=24,
            spacing=20
        )

        titulo_pagina = Label(
            text="Olá, Usuário",
            color=TEXT_MAIN,
            font_size=20,
            bold=True,
            size_hint_y=None,
            height=40,
            halign="left",
            valign="middle"
        )

        titulo_pagina.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        subtitulo = Label(
            text="Bem-vindo ao Sistema de Visitas Técnicas",
            color=TEXT_SUB,
            font_size=12,
            size_hint_y=None,
            height=30,
            halign="left",
            valign="middle"
        )

        subtitulo.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        conteudo.add_widget(titulo_pagina)
        conteudo.add_widget(subtitulo)

        cards = BoxLayout(
            orientation="horizontal",
            spacing=12,
            size_hint_y=None,
            height=90
        )

        card1 = BotaoArredondado(
            BG_BLUE,
            raio=10,
            text="Total de Visitas\n152\nEste mês",
            color=BLUE
        )

        # Agendadas
        card2 = BotaoArredondado(
            BG_PURPLE,
            raio=10,
            text="Agendadas\n45\nEste mês",
            color=PURPLE
        )

        # Concluídas
        card3 = BotaoArredondado(
            BG_GREEN,
            raio=10,
            text="Concluídas\n82\nEste mês",
            color=GREEN
        )

        # Canceladas
        card4 = BotaoArredondado(
            BG_RED,
            raio=10,
            text="Canceladas\n12\nEste mês",
            color=RED
        )

        # Em andamento
        card5 = BotaoArredondado(
            BG_AMBER,
            raio=10,
            text="Em Andamento\n13\nHoje",
            color=AMBER
        )

        cards.add_widget(card1)
        cards.add_widget(card2)
        cards.add_widget(card3)
        cards.add_widget(card4)
        cards.add_widget(card5)

        conteudo.add_widget(cards)

        adicionar = BotaoArredondado(
            PRIMARY,
            raio=8,
            text="+ Adicionar Visita",
            color=WHITE,
            size_hint_y=None,
            height=45,
            on_release=self.abrir_nova_visita
        )
        conteudo.add_widget(adicionar)

        principal.add_widget(conteudo)

        self.add_widget(principal)

    def atualizar_fundo(self, *args):
        self.fundo.pos = self.pos
        self.fundo.size = self.size

    def abrir_nova_visita(self, *args):
        self.manager.current = "nova_visita"