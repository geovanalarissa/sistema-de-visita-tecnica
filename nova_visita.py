from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, Rectangle


# =========================================================
# CORES (mesmo padrão do resto do app)
# =========================================================

BG_PAGE = (241/255, 245/255, 249/255, 1)       # #f1f5f9
BG_CARD = (255/255, 255/255, 255/255, 1)       # #ffffff
TEXT_MAIN = (15/255, 23/255, 42/255, 1)        # #0f172a
TEXT_SUB = (100/255, 116/255, 139/255, 1)      # #64748b
BORDER = (226/255, 232/255, 240/255, 1)        # #e2e8f0
PRIMARY = (79/255, 70/255, 229/255, 1)         # #4f46e5
WHITE = (255/255, 255/255, 255/255, 1)
RED = (239/255, 68/255, 68/255, 1)             # #ef4444


def com_fundo(widget, cor):
    """Desenha um retângulo de fundo colorido atrás do widget."""
    with widget.canvas.before:
        Color(*cor)
        widget._bg_rect = Rectangle(pos=widget.pos, size=widget.size)

    def atualizar(_, __):
        widget._bg_rect.pos = widget.pos
        widget._bg_rect.size = widget.size

    widget.bind(pos=atualizar, size=atualizar)
    return widget


def texto(texto_valor, cor=TEXT_MAIN, halign="left", bold=False, tamanho=14, **kwargs):
    lbl = Label(
        text=texto_valor,
        color=cor,
        halign=halign,
        valign="middle",
        bold=bold,
        font_size=tamanho,
        **kwargs
    )

    def ajustar_text_size(_, tamanho_widget):
        lbl.text_size = (tamanho_widget[0], None)

    lbl.bind(size=ajustar_text_size)
    return lbl


def botao(texto_valor, cor_fundo=PRIMARY, cor_texto=WHITE, **kwargs):
    return Button(
        text=texto_valor,
        background_color=cor_fundo,
        background_normal="",
        background_down="",
        color=cor_texto,
        **kwargs
    )


def campo(hint, **kwargs):
    return TextInput(
        hint_text=hint,
        multiline=False,
        size_hint_y=None,
        height=45,
        padding=[12, 12],
        background_color=BG_CARD,
        foreground_color=TEXT_MAIN,
        **kwargs
    )


# =========================================================
# TELA: NOVA VISITA
# =========================================================

class NovaVisita(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        principal = com_fundo(
            BoxLayout(orientation="vertical", padding=25, spacing=15),
            BG_PAGE
        )

        topo = BoxLayout(orientation="horizontal", size_hint_y=None, height=50)

        topo.add_widget(
            texto("Nova Visita", cor=TEXT_MAIN, bold=True, tamanho=22, halign="left")
        )

        topo.add_widget(
            botao(
                "← Voltar",
                cor_fundo=BG_CARD,
                cor_texto=TEXT_MAIN,
                size_hint_x=0.2,
                on_release=self.voltar
            )
        )
        principal.add_widget(topo)

        principal.add_widget(
            texto(
                "Preencha os dados abaixo para cadastrar uma nova visita técnica.",
                cor=TEXT_SUB,
                tamanho=13,
                halign="left",
                size_hint_y=None,
                height=25
            )
        )

        # =========================
        # FORMULÁRIO (dentro de um card)
        # =========================

        form = com_fundo(
            BoxLayout(orientation="vertical", padding=20, spacing=12),
            BG_CARD
        )

        self.campo_cliente = campo("Nome do cliente")
        form.add_widget(texto("Cliente", cor=TEXT_SUB, tamanho=12, size_hint_y=None, height=20))
        form.add_widget(self.campo_cliente)

        self.campo_endereco = campo("Endereço da visita")
        form.add_widget(texto("Endereço", cor=TEXT_SUB, tamanho=12, size_hint_y=None, height=20))
        form.add_widget(self.campo_endereco)

        linha_data_hora = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=45)

        self.campo_data = campo("DD/MM/AAAA")
        self.campo_horario = campo("HH:MM")

        linha_data_hora.add_widget(self.campo_data)
        linha_data_hora.add_widget(self.campo_horario)

        form.add_widget(texto("Data e horário", cor=TEXT_SUB, tamanho=12, size_hint_y=None, height=20))
        form.add_widget(linha_data_hora)

        form.add_widget(texto("Técnico responsável", cor=TEXT_SUB, tamanho=12, size_hint_y=None, height=20))

        self.spinner_tecnico = Spinner(
            text="Selecione um técnico",
            values=("Lucas Andrade", "Ana Beatriz", "Carlos Souza"),
            size_hint_y=None,
            height=45,
            background_color=BG_CARD,
            color=TEXT_MAIN
        )
        form.add_widget(self.spinner_tecnico)

        form.add_widget(texto("Status inicial", cor=TEXT_SUB, tamanho=12, size_hint_y=None, height=20))

        self.spinner_status = Spinner(
            text="Agendada",
            values=("Agendada", "Em andamento", "Concluída", "Cancelada"),
            size_hint_y=None,
            height=45,
            background_color=BG_CARD,
            color=TEXT_MAIN
        )
        form.add_widget(self.spinner_status)

        principal.add_widget(form)

        # =========================
        # BOTÕES DE AÇÃO
        # =========================

        acoes = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=50)

        acoes.add_widget(
            botao(
                "Cancelar",
                cor_fundo=BG_CARD,
                cor_texto=TEXT_MAIN,
                on_release=self.voltar
            )
        )

        acoes.add_widget(
            botao(
                "Salvar Visita",
                cor_fundo=PRIMARY,
                cor_texto=WHITE,
                on_release=self.salvar_visita
            )
        )

        principal.add_widget(acoes)

        self.add_widget(principal)

    def voltar(self, *args):
        """Volta para a tela anterior (lista de visitas)."""
        self.manager.current = "visitas"

    def salvar_visita(self, *args):
        """Coleta os dados do formulário. Aqui depois entra a lógica de salvar
        (banco de dados, arquivo, etc.)."""

        dados = {
            "cliente": self.campo_cliente.text,
            "endereco": self.campo_endereco.text,
            "data": self.campo_data.text,
            "horario": self.campo_horario.text,
            "tecnico": self.spinner_tecnico.text,
            "status": self.spinner_status.text,
        }

        print("Visita cadastrada:", dados)

        self.manager.current = "dashboard"