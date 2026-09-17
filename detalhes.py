from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

BG_PAGE = (241/255, 245/255, 249/255, 1)       # #f1f5f9
BG_CARD = (255/255, 255/255, 255/255, 1)       # #ffffff
TEXT_MAIN = (15/255, 23/255, 42/255, 1)        # #0f172a
TEXT_SUB = (100/255, 116/255, 139/255, 1)      # #64748b
BORDER = (226/255, 232/255, 240/255, 1)        # #e2e8f0

# Sidebar
SIDEBAR_BG = (15/255, 23/255, 42/255, 1)       # #0f172a
SIDEBAR_TEXT = (148/255, 163/255, 184/255, 1)  # #94a3b8
SIDEBAR_ACTIVE = (79/255, 70/255, 229/255, 1)  # #4f46e5

# Principal
PRIMARY = (79/255, 70/255, 229/255, 1)         # #4f46e5
PRIMARY_HOVER = (67/255, 56/255, 202/255, 1)   # #4338ca

# Status
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

# Avatar
AVATAR_BG = (203/255, 213/255, 225/255, 1)
AVATAR_TEXT = (71/255, 85/255, 105/255, 1)
AVATAR_BLUE = (99/255, 102/255, 241/255, 1)

# Tag
TAG_RED_BG = (254/255, 226/255, 226/255, 1)
TAG_RED_TEXT = (220/255, 38/255, 38/255, 1)

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
            Color(*cor_fundo)
            self.fundo = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[raio]
            )

        self.bind(
            pos=self.atualizar_fundo,
            size=self.atualizar_fundo
        )

    def atualizar_fundo(self, *args):
        self.fundo.pos = self.pos
        self.fundo.size = self.size

class Detalhes(Screen):

    def __init__(self, **kwargs):
        super().__init__(
            **kwargs
        )

        fundo = BoxLayout( 
            orientation= 'horizontal'
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

        sidebar = Fundo(
            SIDEBAR_BG,
            orientation="vertical",
            size_hint_x=None,
            width=250,
            padding=12,
            spacing=5
        )

        titulo_sidebar = Label(
            text="Visitas ao Técnico",
            color=WHITE,
            font_size=16,
            bold=True,
            size_hint_y=None,
            height=50
        )

        dashboard = BotaoArredondado(
            SIDEBAR_BG,
            text="Dashboard",
            color=SIDEBAR_TEXT,
            size_hint_y=None,
            height=45
        )

        visitas = BotaoArredondado(
            SIDEBAR_ACTIVE,
            text="Visitas",
            color=WHITE,
            size_hint_y=None,
            height=45
        )

        nova_visita = BotaoArredondado(
            SIDEBAR_BG,
            text="Nova Visita",
            color=SIDEBAR_TEXT,
            size_hint_y=None,
            height=45
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

        dashboard.bind(
            on_press=lambda instance: self.ir_para("dashboard")
        )

        visitas.bind(
            on_press=lambda instance: self.ir_para("visitas")
        )

        nova_visita.bind(
            on_press=lambda instance: self.ir_para("nova_visita")
        )

        sidebar.add_widget(titulo_sidebar)
        sidebar.add_widget(dashboard)
        sidebar.add_widget(visitas)
        sidebar.add_widget(nova_visita)
        sidebar.add_widget(clientes)
        sidebar.add_widget(tecnicos)

        sidebar.add_widget(Label(text=""))

        nome_usuario = Label(
            text="Camille Oliveira",
            color=WHITE,
            font_size=14,
            bold=True,
            size_hint_y=None,
            height=30
        )

        tipo_usuario = Label(
            text="Administradora",
            color=SIDEBAR_TEXT,
            font_size=12,
            size_hint_y=None,
            height=25
        )

        sair = BotaoArredondado(
            SIDEBAR_BG,
            text="Sair",
            color=SIDEBAR_TEXT,
            size_hint_y=None,
            height=45
        )

        sair.bind(
            on_press=lambda instance: self.ir_para("login")
        )

        sidebar.add_widget(nome_usuario)
        sidebar.add_widget(tipo_usuario)
        sidebar.add_widget(sair)

        self.add_widget(sidebar)

        conteudo = BoxLayout(
            orientation="vertical",
            padding=24,
            spacing=15
        )

        titulo = Label(
            text="Detalhes da Visita",
            color=TEXT_MAIN,
            font_size=22,
            bold=True,
            size_hint_y=None,
            height=40,
            halign="left"
        )

        titulo.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        subtitulo = Label(
            text="Informações completas da visita agendada",
            color=TEXT_SUB,
            font_size=12,
            size_hint_y=None,
            height=30,
            halign="left"
        )

        subtitulo.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        conteudo.add_widget(titulo)
        conteudo.add_widget(subtitulo)

        linha_topo = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=45,
            spacing=10
        )

        voltar = BotaoArredondado(
            BG_CARD,
            text="← Voltar para a lista",
            color=PRIMARY,
            size_hint_x=None,
            width=180
        )

        status = BotaoArredondado(
            BG_BLUE,
            text="Agendada",
            color=BLUE,
            size_hint_x=None,
            width=110
        )

        voltar.bind(
            on_press=lambda instance: self.ir_para("visitas")
        )

        linha_topo.add_widget(voltar)
        linha_topo.add_widget(status)
        linha_topo.add_widget(Label())

        conteudo.add_widget(linha_topo)


        card = Fundo(
            BG_CARD,
            orientation="vertical",
            padding=20,
            spacing=12
        )

        identificacao = Label(
            text="Visita #00126",
            color=TEXT_MAIN,
            font_size=18,
            bold=True,
            size_hint_y=None,
            height=35,
            halign="left"
        )

        identificacao.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        data = Label(
            text="26 de Setembro de 2026 - 08:00",
            color=TEXT_SUB,
            font_size=13,
            size_hint_y=None,
            height=30,
            halign="left"
        )

        data.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        card.add_widget(identificacao)
        card.add_widget(data)

        # =====================================================
        # INFORMAÇÕES
        # =====================================================

        informacoes = BoxLayout(
            orientation="vertical",
            spacing=5
        )

        cliente_titulo = Label(
            text="Cliente",
            color=TEXT_SUB,
            font_size=12,
            size_hint_y=None,
            height=22,
            halign="left"
        )

        cliente_titulo.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        cliente = Label(
            text="João da Silva",
            color=TEXT_MAIN,
            font_size=14,
            bold=True,
            size_hint_y=None,
            height=28,
            halign="left"
        )

        cliente.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        endereco_titulo = Label(
            text="Endereço",
            color=TEXT_SUB,
            font_size=12,
            size_hint_y=None,
            height=22,
            halign="left"
        )

        endereco_titulo.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        endereco = Label(
            text="Rua das Flores, 123 - Recife/PE",
            color=TEXT_MAIN,
            font_size=14,
            size_hint_y=None,
            height=28,
            halign="left"
        )

        endereco.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        tecnico_titulo = Label(
            text="Técnico",
            color=TEXT_SUB,
            font_size=12,
            size_hint_y=None,
            height=22,
            halign="left"
        )

        tecnico_titulo.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        tecnico = Label(
            text="Lucas Andrade",
            color=TEXT_MAIN,
            font_size=14,
            bold=True,
            size_hint_y=None,
            height=28,
            halign="left"
        )

        tecnico.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        observacoes_titulo = Label(
            text="Observações",
            color=TEXT_SUB,
            font_size=12,
            size_hint_y=None,
            height=22,
            halign="left"
        )

        observacoes_titulo.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        observacoes = Label(
            text=(
                "Cliente solicitou o técnico para verificar problema "
                "na rede elétrica. Levar ferramentas completas."
            ),
            color=TEXT_MAIN,
            font_size=13,
            size_hint_y=None,
            height=45,
            halign="left",
            valign="top"
        )

        observacoes.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", (value[0], None))
        )

        informacoes.add_widget(cliente_titulo)
        informacoes.add_widget(cliente)

        informacoes.add_widget(endereco_titulo)
        informacoes.add_widget(endereco)

        informacoes.add_widget(tecnico_titulo)
        informacoes.add_widget(tecnico)

        informacoes.add_widget(observacoes_titulo)
        informacoes.add_widget(observacoes)

        card.add_widget(informacoes)

        conteudo.add_widget(card)

        participantes_titulo = Label(
            text="Participantes",
            color=TEXT_MAIN,
            font_size=17,
            bold=True,
            size_hint_y=None,
            height=35,
            halign="left"
        )

        participantes_titulo.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        conteudo.add_widget(participantes_titulo)

        participantes = Fundo(
            BG_CARD,
            orientation="vertical",
            padding=12,
            spacing=8,
            size_hint_y=None,
            height=150
        )

        participantes.add_widget(
            self.criar_participante(
                "João da Silva",
                "Cliente",
                "Presente",
                BG_GREEN,
                GREEN
            )
        )

        participantes.add_widget(
            self.criar_participante(
                "Lucas Andrade",
                "Técnico",
                "Presente",
                BG_GREEN,
                GREEN
            )
        )

        participantes.add_widget(
            self.criar_participante(
                "Maria Souza",
                "Acompanhante",
                "Pendente",
                BG_AMBER,
                AMBER
            )
        )

        conteudo.add_widget(participantes)


        botoes = BoxLayout(
            orientation="horizontal",
            spacing=10,
            size_hint_y=None,
            height=45
        )

        editar = BotaoArredondado(
            PRIMARY,
            text="Editar Visita",
            color=WHITE
        )

        cancelar = BotaoArredondado(
            BG_RED,
            text="Cancelar Visita",
            color=RED
        )

        adicionar_participante = BotaoArredondado(
            BG_PURPLE,
            text="Adicionar Participantes",
            color=PURPLE
        )

        imprimir = BotaoArredondado(
            BG_CARD,
            text="Imprimir",
            color=TEXT_MAIN
        )

        # =====================================================
        # AÇÕES DOS BOTÕES
        # =====================================================

        editar.bind(
            on_press=lambda instance:
            self.ir_para("nova_visita")
        )

        cancelar.bind(
            on_press=lambda instance:
            self.cancelar_visita()
        )

        adicionar_participante.bind(
            on_press=lambda instance:
            self.ir_para("participantes")
        )

        # =====================================================
        # ADICIONA BOTÕES
        # =====================================================

        botoes.add_widget(editar)
        botoes.add_widget(cancelar)
        botoes.add_widget(adicionar_participante)
        botoes.add_widget(imprimir)

        conteudo.add_widget(botoes)

        self.add_widget(conteudo)

    # =========================================================
    # NAVEGAÇÃO
    # =========================================================

    def ir_para(self, tela):

        if self.manager:
            self.manager.current = tela

    # =========================================================
    # PARTICIPANTE
    # =========================================================

    def criar_participante(
        self,
        nome,
        funcao,
        status,
        cor_fundo,
        cor_texto
    ):

        linha = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=38,
            spacing=10
        )

        avatar = BotaoArredondado(
            AVATAR_BG,
            raio=20,
            text=nome[0],
            color=AVATAR_TEXT,
            size_hint_x=None,
            width=38
        )

        informacao = BoxLayout(
            orientation="vertical"
        )

        nome_label = Label(
            text=nome,
            color=TEXT_MAIN,
            font_size=13,
            bold=True,
            halign="left"
        )

        nome_label.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        funcao_label = Label(
            text=funcao,
            color=TEXT_SUB,
            font_size=11,
            halign="left"
        )

        funcao_label.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        informacao.add_widget(nome_label)
        informacao.add_widget(funcao_label)

        tag = BotaoArredondado(
            cor_fundo,
            raio=8,
            text=status,
            color=cor_texto,
            size_hint_x=None,
            width=85
        )

        linha.add_widget(avatar)
        linha.add_widget(informacao)
        linha.add_widget(tag)

        return linha

    # =========================================================
    # CANCELAR VISITA
    # =========================================================

    def cancelar_visita(self):

        conteudo = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=15
        )

        mensagem = Label(
            text="Deseja realmente cancelar esta visita?",
            color=TEXT_MAIN,
            font_size=14
        )

        botoes = BoxLayout(
            orientation="horizontal",
            spacing=10,
            size_hint_y=None,
            height=45
        )

        nao = BotaoArredondado(
            BG_CARD,
            text="Não",
            color=TEXT_MAIN
        )

        sim = BotaoArredondado(
            BG_RED,
            text="Cancelar Visita",
            color=RED
        )

        botoes.add_widget(nao)
        botoes.add_widget(sim)

        conteudo.add_widget(mensagem)
        conteudo.add_widget(botoes)

        popup = Popup(
            title="Cancelar Visita",
            content=conteudo,
            size_hint=(None, None),
            size=(400, 220),
            separator_color=PRIMARY
        )

        nao.bind(
            on_press=popup.dismiss
        )

        sim.bind(
            on_press=lambda instance: popup.dismiss()
        )

        popup.open()


    def atualizar_fundo(self, *args):
        self.fundo.pos = self.pos
        self.fundo.size = self.size