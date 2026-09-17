from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.screenmanager import Screen


LOGIN_BG = (9/255, 13/255, 22/255, 1)             # #090d16
LOGIN_BANNER = (9/255, 14/255, 26/255, 1)         # #090e1a

# Lado direito
LOGIN_BOX = (20/255, 30/255, 51/255, 1)            # #141e33

# Campos
LOGIN_INPUT = (15/255, 23/255, 42/255, 1)         # #0f172a
LOGIN_INPUT_BORDER = (38/255, 51/255, 77/255, 1)  # #26334d

# Textos
LOGIN_TEXT = (255/255, 255/255, 255/255, 1)        # #ffffff
LOGIN_SUBTEXT = (148/255, 163/255, 184/255, 1)    # #94a3b8
LOGIN_FEATURE = (203/255, 213/255, 225/255, 1)    # #cbd5e1

# Botão
LOGIN_PRIMARY = (99/255, 102/255, 241/255, 1)     # #6366f1
LOGIN_PRIMARY_HOVER = (79/255, 70/255, 229/255, 1) # #4f46e5

# Destaque
LOGIN_ICON = (129/255, 140/255, 248/255, 1)       # #818cf8


# =========================================================
# FUNDO
# =========================================================

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
# CAMPO DE TEXTO
# =========================================================

class Campo(TextInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Cores
        self.background_normal = ""
        self.background_active = ""

        self.background_color = LOGIN_INPUT
        self.foreground_color = LOGIN_TEXT
        self.hint_text_color = LOGIN_SUBTEXT
        self.cursor_color = LOGIN_PRIMARY

        # Espaçamento interno
        self.padding = [15, 12]

        # Borda
        with self.canvas.before:

            Color(*LOGIN_INPUT_BORDER)

            self.borda = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[8]
            )

            Color(*LOGIN_INPUT)

            self.fundo = RoundedRectangle(
                pos=(self.x + 1, self.y + 1),
                size=(self.width - 2, self.height - 2),
                radius=[8]
            )

        self.bind(
            pos=self.atualizar,
            size=self.atualizar
        )

    def atualizar(self, *args):

        self.borda.pos = self.pos
        self.borda.size = self.size

        self.fundo.pos = (
            self.x + 1,
            self.y + 1
        )

        self.fundo.size = (
            self.width - 2,
            self.height - 2
        )


# =========================================================
# BOTÃO ENTRAR
# =========================================================

class BotaoEntrar(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""

        self.background_color = LOGIN_PRIMARY
        self.color = LOGIN_TEXT

        self.bold = True
        self.font_size = 15

        with self.canvas.before:

            Color(*LOGIN_PRIMARY)

            self.fundo = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[8]
            )

        self.bind(
            pos=self.atualizar,
            size=self.atualizar
        )

    def atualizar(self, *args):

        self.fundo.pos = self.pos
        self.fundo.size = self.size


# =========================================================
# BOTÃO ESQUECEU A SENHA
# =========================================================

class BotaoEsqueceu(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""

        self.background_color = (0, 0, 0, 0)

        self.color = LOGIN_SUBTEXT

        self.font_size = 13


# =========================================================
# LOGIN
# =========================================================

class Login(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        principal = Fundo(cor=LOGIN_BG, orientation="horizontal")
        self.add_widget(principal)

    def build(self):

        principal = Fundo(
            cor=LOGIN_BG,
            orientation="horizontal"
        )


        banner = Fundo(
            cor=LOGIN_BANNER,
            orientation="vertical",
            padding=60,
            spacing=15
        )

        banner.add_widget(
            Label(
                text="Visitas Técnicas",
                color=LOGIN_TEXT,
                font_size=28,
                bold=True,
                size_hint_y=None,
                height=60
            )
        )

        banner.add_widget(
            Label(
                text="Organização e controle das visitas do técnico.",
                color=LOGIN_SUBTEXT,
                font_size=15
            )
        )

        banner.add_widget(
            Label(
                text="Agende visitas",
                color=LOGIN_FEATURE,
                font_size=16
            )
        )

        banner.add_widget(
            Label(
                text="Acompanhe o andamento",
                color=LOGIN_FEATURE,
                font_size=16
            )
        )

        banner.add_widget(
            Label(
                text="Edite quando precisar",
                color=LOGIN_FEATURE,
                font_size=16
            )
        )

        banner.add_widget(
            Label(
                text="Mais praticidade no seu dia a dia",
                color=LOGIN_ICON,
                font_size=17,
                bold=True
            )
        )

        principal.add_widget(banner)

        login = Fundo(
            cor=LOGIN_BOX,
            orientation="vertical",
            padding=40,
            spacing=12
        )

        login.add_widget(
            Label(
                Button="Entrar",
                color=LOGIN_TEXT,
                font_size=26,
                bold=True,
                size_hint_y=None,
                height=50
            )
        )

        login.add_widget(
            Label(
                text="Acesse sua conta para continuar",
                color=LOGIN_SUBTEXT,
                font_size=14,
                size_hint_y=None,
                height=40
            )
        )


        usuario = Campo(
            hint_text="Usuário",
            multiline=False,
            size_hint_y=None,
            height=50
        )

        login.add_widget(usuario)

        senha = Campo(
            hint_text="Senha",
            password=True,
            multiline=False,
            size_hint_y=None,
            height=50
        )

        login.add_widget(senha)

        login.add_widget(
            BotaoEntrar(
                text="Entrar",
                size_hint_y=None,
                height=50
            )
        )


        login.add_widget(
            BotaoEsqueceu(
                text="Esqueceu sua senha?",
                size_hint_y=None,
                height=40
            )
        )

        principal.add_widget(login)

        return principal
