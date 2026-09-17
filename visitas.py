from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
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

STATUS_CORES = {
    "Agendada": (BLUE, BG_BLUE),
    "Concluída": (GREEN, BG_GREEN),
    "Cancelada": (RED, BG_RED),
    "Em andamento": (AMBER, BG_AMBER),
}


# =========================================================
# HELPERS
# =========================================================

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
    """Label pronto para alinhamento correto (halign exige text_size)."""
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
    """Botão colorido (background_normal precisa ser vazio para Kivy respeitar background_color)."""
    return Button(
        text=texto_valor,
        background_color=cor_fundo,
        background_normal="",
        background_down="",
        color=cor_texto,
        **kwargs
    )


class Visitas(Screen):

    def build(self):

        Window.size = (1000, 650)
        Window.clearcolor = BG_PAGE

        principal = BoxLayout(orientation="horizontal")

    
        sidebar = com_fundo(
            BoxLayout(
                orientation="vertical",
                size_hint_x=0.23,
                padding=15,
                spacing=8
            ),
            SIDEBAR_BG
        )

        sidebar.add_widget(
            texto(
                "Visitas ao Técnico",
                cor=WHITE,
                bold=True,
                tamanho=18,
                halign="left",
                size_hint_y=None,
                height=50
            )
        )

        itens_menu = ["Dashboard", "Visitas", "Nova Visita", "Clientes", "Técnicos"]
        for i, item in enumerate(itens_menu):
            cor_fundo = SIDEBAR_ACTIVE if i == 0 else SIDEBAR_BG
            sidebar.add_widget(
                botao(
                    item,
                    cor_fundo=cor_fundo,
                    cor_texto=WHITE if i == 0 else SIDEBAR_TEXT,
                    size_hint_y=None,
                    height=42
                )
            )

        # Espaço antes do perfil
        sidebar.add_widget(Label())

        sidebar.add_widget(
            texto("Camila Oliveira", cor=WHITE, bold=True, size_hint_y=None, height=25)
        )

        sidebar.add_widget(
            texto("Administradora", cor=SIDEBAR_TEXT, tamanho=12, size_hint_y=None, height=25)
        )

        sidebar.add_widget(
            botao("Sair", cor_fundo=RED, cor_texto=WHITE, size_hint_y=None, height=45)
        )

        principal.add_widget(sidebar)

        # =========================
        # CONTEÚDO
        # =========================

        conteudo = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        # =========================
        # TOPBAR
        # =========================

        topbar = BoxLayout(orientation="horizontal", size_hint_y=None, height=60)

        titulo = BoxLayout(orientation="vertical")

        titulo.add_widget(
            texto("Dashboard", cor=TEXT_MAIN, bold=True, tamanho=20, halign="left")
        )

        titulo.add_widget(
            texto(
                "Bem-vindo ao Sistema de Visitas Técnicas",
                cor=TEXT_SUB,
                tamanho=13,
                halign="left"
            )
        )

        topbar.add_widget(titulo)

        tema = BoxLayout(orientation="horizontal", size_hint_x=0.35, spacing=6)

        tema.add_widget(botao("☀", cor_fundo=BG_CARD, cor_texto=TEXT_MAIN))
        tema.add_widget(botao("☾", cor_fundo=BG_CARD, cor_texto=TEXT_MAIN))
        tema.add_widget(botao("🔔 3", cor_fundo=BG_CARD, cor_texto=TEXT_MAIN))
        tema.add_widget(botao("👤", cor_fundo=PRIMARY, cor_texto=WHITE))

        topbar.add_widget(tema)

        conteudo.add_widget(topbar)

        # =========================
        # CARDS KPI
        # =========================

        kpi = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=100)

        cards = [
            ("Total de Visitas", "152", "Este mês"),
            ("Agendadas", "45", "Este mês"),
            ("Concluídas", "82", "Este mês"),
            ("Canceladas", "12", "Este mês"),
            ("Em Andamento", "13", "Hoje")
        ]

        for titulo_card, numero, periodo in cards:

            card = com_fundo(
                BoxLayout(orientation="vertical", padding=10),
                BG_CARD
            )

            card.add_widget(texto(titulo_card, cor=TEXT_SUB, tamanho=12, halign="left"))
            card.add_widget(texto(numero, cor=TEXT_MAIN, bold=True, tamanho=24, halign="left"))
            card.add_widget(texto(periodo, cor=TEXT_SUB, tamanho=11, halign="left"))

            kpi.add_widget(card)

        conteudo.add_widget(kpi)

        # =========================
        # BOTÃO NOVA VISITA
        # =========================

        conteudo.add_widget(
            botao(
                "+ Adicionar Visita",
                cor_fundo=PRIMARY,
                cor_texto=WHITE,
                size_hint_y=None,
                height=45
            )
        )

        # =========================
        # VISITAS
        # =========================

        conteudo.add_widget(
            texto(
                "Visitas de hoje (22/09/2026)",
                cor=TEXT_MAIN,
                bold=True,
                tamanho=16,
                halign="left",
                size_hint_y=None,
                height=35
            )
        )

        filtro = Spinner(
            text="Hoje",
            values=("Hoje", "Amanhã", "Esta Semana"),
            size_hint_y=None,
            height=40,
            background_color=BG_CARD,
            color=TEXT_MAIN
        )

        conteudo.add_widget(filtro)

        visitas = [
            ("08:00", "João da Silva", "Rua das Flores, 123 - Recife/PE", "Lucas Andrade", "Em andamento"),
            ("10:30", "Maria Oliveira", "Av. Boa Viagem, 456 - Recife/PE", "Ana Beatriz", "Agendada"),
            ("14:00", "Empresa ABC Ltda.", "Rua do Sol, 789 - Olinda/PE", "Lucas Andrade", "Agendada"),
            ("16:30", "José Pereira", "Av. Caxangá, 321 - Recife/PE", "Carlos Souza", "Cancelada"),
            ("17:45", "Fernanda Lima", "Av. da Aurora, 654 - Recife/PE", "Ana Beatriz", "Concluída"),
        ]

        for horario, cliente, endereco, tecnico, status in visitas:

            visita = com_fundo(
                BoxLayout(
                    orientation="horizontal",
                    size_hint_y=None,
                    height=70,
                    spacing=8,
                    padding=8
                ),
                BG_CARD
            )

            visita.add_widget(
                texto(horario, cor=TEXT_SUB, bold=True, size_hint_x=0.12, halign="left")
            )

            info = BoxLayout(orientation="vertical")
            info.add_widget(texto(cliente, cor=TEXT_MAIN, bold=True, halign="left"))
            info.add_widget(texto(endereco, cor=TEXT_SUB, tamanho=12, halign="left"))
            info.add_widget(texto(tecnico, cor=TEXT_SUB, tamanho=12, halign="left"))

            visita.add_widget(info)

            cor_status, fundo_status = STATUS_CORES.get(status, (TEXT_SUB, BG_CARD))
            badge = com_fundo(
                BoxLayout(size_hint_x=0.18),
                fundo_status
            )
            badge.add_widget(texto(status, cor=cor_status, bold=True, tamanho=12, halign="center"))
            visita.add_widget(badge)

            visita.add_widget(
                botao(
                    "Ver detalhes",
                    cor_fundo=PRIMARY,
                    cor_texto=WHITE,
                    size_hint_x=0.18
                )
            )

            conteudo.add_widget(visita)

        conteudo.add_widget(
            botao(
                "Ver todas as visitas",
                cor_fundo=BG_CARD,
                cor_texto=PRIMARY,
                size_hint_y=None,
                height=40
            )
        )

        # =========================
        # AGENDA
        # =========================

        conteudo.add_widget(
            texto(
                "Agenda de Visitas",
                cor=TEXT_MAIN,
                bold=True,
                tamanho=16,
                halign="left",
                size_hint_y=None,
                height=40
            )
        )

        conteudo.add_widget(
            texto("Setembro 2026", cor=TEXT_SUB, halign="left", size_hint_y=None, height=25)
        )

        calendario = com_fundo(
            BoxLayout(orientation="vertical", size_hint_y=None, height=180, padding=8, spacing=4),
            BG_CARD
        )

        dias_semana = BoxLayout()
        for dia in ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]:
            dias_semana.add_widget(texto(dia, cor=TEXT_SUB, bold=True, halign="center"))
        calendario.add_widget(dias_semana)

        dias = [
            "30", "31", "1", "2", "3", "4", "5",
            "6", "7", "8", "9", "10", "11", "12",
            "13", "14", "15", "16", "17", "18", "19",
            "20", "21", "22", "23", "24", "25", "26",
            "27", "28", "29", "30", "1", "2", "3"
        ]

        dia_atual = "22"
        for inicio in range(0, len(dias), 7):

            semana = BoxLayout(spacing=2)

            for dia in dias[inicio:inicio + 7]:
                if dia == dia_atual:
                    semana.add_widget(
                        botao(dia, cor_fundo=PRIMARY, cor_texto=WHITE)
                    )
                else:
                    semana.add_widget(
                        botao(dia, cor_fundo=BG_CARD, cor_texto=TEXT_MAIN)
                    )

            calendario.add_widget(semana)

        conteudo.add_widget(calendario)

        # =========================
        # LEGENDA
        # =========================

        legenda = BoxLayout(size_hint_y=None, height=25, spacing=15)
        for nome, (cor, _) in STATUS_CORES.items():
            legenda.add_widget(texto(f"● {nome}", cor=cor, tamanho=12, halign="left"))
        conteudo.add_widget(legenda)

        # =========================
        # PRÓXIMAS VISITAS
        # =========================

        conteudo.add_widget(
            texto(
                "Próximas Visitas",
                cor=TEXT_MAIN,
                bold=True,
                tamanho=16,
                halign="left",
                size_hint_y=None,
                height=40
            )
        )

        proximas = [
            ("Carlos Pereira", "23/09/2026 - 09:00", "Agendada"),
            ("Residencial Parque", "23/09/2026 - 14:30", "Agendada"),
            ("Loja Total", "24/09/2026 - 10:20", "Agendada"),
        ]

        for nome, data, status in proximas:

            item = com_fundo(
                BoxLayout(orientation="horizontal", size_hint_y=None, height=50, padding=8),
                BG_CARD
            )

            item.add_widget(texto(nome, cor=TEXT_MAIN, halign="left"))
            item.add_widget(texto(data, cor=TEXT_SUB, halign="left"))

            cor_status, _ = STATUS_CORES.get(status, (TEXT_SUB, BG_CARD))
            item.add_widget(texto(status, cor=cor_status, bold=True, halign="right"))

            conteudo.add_widget(item)

        conteudo.add_widget(
            botao("Ver todas", cor_fundo=BG_CARD, cor_texto=PRIMARY)
        )

        principal.add_widget(conteudo)

        return principal
