from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Configurações de estilo
Window.clearcolor = (1, 1, 1, 1)  # Fundo branco

# Variáveis globais
saldo_atual = 0  # Saldo atual da conta
historico_transacoes = []  # Lista para armazenar histórico de transações
saques = 0  # Contador de saques realizados no dia

# Função para realizar depósito
def deposito(quantia):
    global saldo_atual, historico_transacoes
    try:
        quantia = float(quantia)
        if quantia > 0:
            saldo_atual += quantia
            detalhes_op = {'tipo de operação': 'Depósito', 'quantia': quantia}
            historico_transacoes.append(detalhes_op)
            return True, f"Depósito de R$ {quantia:.2f} realizado com sucesso!"
        else:
            return False, "Quantia inválida!"
    except ValueError:
        return False, "Digite uma quantia válida!"

# Função para realizar saque
def saque(quantia):
    global saldo_atual, historico_transacoes, saques
    try:
        quantia = float(quantia)
        if saldo_atual == 0:
            return False, "Saldo insuficiente para realizar o saque."
        elif saques >= 3:
            return False, "Você já atingiu o limite de 3 saques diários."
        elif quantia > saldo_atual:
            return False, "Quantia maior do que o saldo disponível."
        elif quantia > 500:
            return False, "Limite de saque excedido."
        else:
            saldo_atual -= quantia
            saques += 1
            detalhes_op = {'tipo de operação': 'Saque', 'quantia': quantia}
            historico_transacoes.append(detalhes_op)
            return True, f"Saque de R$ {quantia:.2f} realizado com sucesso!"
    except ValueError:
        return False, "Digite uma quantia válida!"

# Função para gerar o extrato
def extrato():
    extrato_text = "Extrato:\n"
    for transacao in historico_transacoes:
        extrato_text += f"{transacao['tipo de operação']}: R$ {transacao['quantia']:.2f}\n"
    extrato_text += f"Saldo Atual: R$ {saldo_atual:.2f}"
    return extrato_text

# Tela Inicial
class TelaInicial(Screen):
    def __init__(self, **kwargs):
        super(TelaInicial, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=100, spacing=10)

        # Adiciona um título
        layout.add_widget(Label(text="Bem-vindo ao Banco!", font_size='24sp', color=(0, 0, 0, 1)))

        # Define o estilo dos botões
        btn_style = {'font_size': '18sp', 'background_color': (0, 1, 0, 1), 'color': (1, 1, 1, 1)}
        layout.add_widget(Button(text="Extrato", on_press=self.ir_para_extrato, **btn_style))
        layout.add_widget(Button(text="Saque", on_press=self.ir_para_saque, **btn_style))
        layout.add_widget(Button(text="Depósito", on_press=self.ir_para_deposito, **btn_style))

        self.add_widget(layout)

    def ir_para_extrato(self, instance):
        self.manager.current = 'extrato'

    def ir_para_saque(self, instance):
        self.manager.current = 'saque'

    def ir_para_deposito(self, instance):
        self.manager.current = 'deposito'

# Tela de Extrato
class TelaExtrato(Screen):
    def __init__(self, **kwargs):
        super(TelaExtrato, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=100, spacing=10)
        self.label_extrato = Label(text=extrato(), font_size='18sp', color=(0, 0, 0, 1))
        layout.add_widget(self.label_extrato)

        # Define o estilo do botão
        btn_style = {'font_size': '25sp', 'background_color': (0, 1, 0, 1), 'color': (1, 1, 1, 1)}
        layout.add_widget(Button(text="Voltar", on_press=self.voltar_tela_inicial, **btn_style))    
        self.add_widget(layout)

    def on_enter(self):
        # Atualiza o extrato quando a tela é exibida
        self.label_extrato.text = extrato()

    def voltar_tela_inicial(self, instance):
        self.manager.current = 'inicial'

# Tela de Saque
class TelaSaque(Screen):
    def __init__(self, **kwargs):
        super(TelaSaque, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=100, spacing=10)
        
        # Campo para entrada da quantia
        self.quantia_input = TextInput(hint_text="Digite a quantia para saque", multiline=False, font_size='18sp')
        layout.add_widget(self.quantia_input)

        # Define o estilo dos botões
        btn_style = {'font_size': '18sp', 'background_color': (0, 1, 0, 1), 'color': (1, 1, 1, 1)}
        layout.add_widget(Button(text="Confirmar Saque", on_press=self.confirmar_saque, **btn_style))
        layout.add_widget(Button(text="Voltar", on_press=self.voltar_tela_inicial, **btn_style))
        
        self.add_widget(layout)

    def confirmar_saque(self, instance):
        status, mensagem = saque(self.quantia_input.text)
        if status:
            self.manager.current = 'sucesso'
        else:
            self.manager.current = 'erro'
        self.manager.get_screen('sucesso').mensagem = mensagem
        self.manager.get_screen('erro').mensagem = mensagem

    def voltar_tela_inicial(self, instance):
        self.manager.current = 'inicial'

# Tela de Depósito
class TelaDeposito(Screen):
    def __init__(self, **kwargs):
        super(TelaDeposito, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=100, spacing=10)
        
        # Campo para entrada da quantia
        self.quantia_input = TextInput(hint_text="Digite a quantia para depósito", multiline=False, font_size='18sp')
        layout.add_widget(self.quantia_input)

        # Define o estilo dos botões
        btn_style = {'font_size': '18sp', 'background_color': (0, 1, 0, 1), 'color': (1, 1, 1, 1)}
        layout.add_widget(Button(text="Confirmar Depósito", on_press=self.confirmar_deposito, **btn_style))
        layout.add_widget(Button(text="Voltar", on_press=self.voltar_tela_inicial, **btn_style))
        
        self.add_widget(layout)

    def confirmar_deposito(self, instance):
        status, mensagem = deposito(self.quantia_input.text)
        if status:
            self.manager.current = 'sucesso'
        else:
            self.manager.current = 'erro'
        self.manager.get_screen('sucesso').mensagem = mensagem
        self.manager.get_screen('erro').mensagem = mensagem

    def voltar_tela_inicial(self, instance):
        self.manager.current = 'inicial'

# Tela de Sucesso
class TelaSucesso(Screen):
    def __init__(self, **kwargs):
        super(TelaSucesso, self).__init__(**kwargs)
        self.mensagem = ""
        layout = BoxLayout(orientation='vertical', padding=100, spacing=10)
        self.label_mensagem = Label(text="", font_size='18sp', color=(0, 0, 0, 1))
        layout.add_widget(self.label_mensagem)
        
        # Define o estilo do botão
        btn_style = {'font_size': '18sp', 'background_color': (0, 1, 0, 1), 'color': (1, 1, 1, 1)}
        layout.add_widget(Button(text="Voltar", on_press=self.voltar_tela_inicial, **btn_style))
        self.add_widget(layout)

    def on_enter(self):
        # Atualiza a mensagem de sucesso quando a tela é exibida
        self.label_mensagem.text = self.mensagem

    def voltar_tela_inicial(self, instance):
        self.manager.current = 'inicial'

# Tela de Erro
class TelaErro(Screen):
    def __init__(self, **kwargs):
        super(TelaErro, self).__init__(**kwargs)
        self.mensagem = ""
        layout = BoxLayout(orientation='vertical', padding=100, spacing=10)
        self.label_mensagem = Label(text="", font_size='18sp', color=(0, 0, 0, 1))
        layout.add_widget(self.label_mensagem)
        
        # Define o estilo do botão
        btn_style = {'font_size': '18sp', 'background_color': (0, 1, 0, 1), 'color': (1, 1, 1, 1)}
        layout.add_widget(Button(text="Voltar", on_press=self.voltar_tela_inicial, **btn_style))
        self.add_widget(layout)

    def on_enter(self):
        # Atualiza a mensagem de erro quando a tela é exibida
        self.label_mensagem.text = self.mensagem

    def voltar_tela_inicial(self, instance):
        self.manager.current = 'inicial'

# Gerenciador de Telas
class GerenciadorDeTelas(ScreenManager):
    pass

# Aplicação Principal
class BancoApp(App):
    def build(self):
        sm = GerenciadorDeTelas()
        sm.add_widget(TelaInicial(name='inicial'))
        sm.add_widget(TelaExtrato(name='extrato'))
        sm.add_widget(TelaSaque(name='saque'))
        sm.add_widget(TelaDeposito(name='deposito'))
        sm.add_widget(TelaSucesso(name='sucesso'))
        sm.add_widget(TelaErro(name='erro'))
        return sm

if __name__ == '__main__':
    BancoApp().run()
