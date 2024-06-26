from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from math import sqrt
from math import pi
from math import pow

# Determinado as cores
red = [1, 0, 0, 1]
blue = [0, 0, 1, 1]


class CalculadoraApp(App):
    def build(self):
        self.operators = ['+', '-', '*','^', '/', '(',')', '%', '=', '√', 'π', '}', '{'] # → Lista de operadores
        self.last_was_operator = None      
        self.last_button = None   
             

        # Utilizaremos os botoes acima mais tarde 
        # para verificar se o botão pressionado é um operador

        # Criando o layout

        layout = BoxLayout(orientation='vertical')
        colors = [red, blue]
        # Componente de inteface com algumas propriedades

        self.solucao = TextInput(multiline=False, readonly=True, halign='right', font_size=55)

        # Adicionando o componente ao layout

        layout.add_widget(self.solucao)

        # Adicionando os botões ao layout em matriz
        buttons = [
            ['%','^', '(', ')', '/'],
            ['{','7', '8', '9', '*'],  
            ['}','4', '5', '6', '-'], 
            ['π','1', '2', '3', '+'],
            ['=','.', '0', 'C', '√']
            
        ]
        # Instanciando a Classe BloxLayout e atribuindo a variável h_layout
        
        

        for row in buttons:
            h_layout = BoxLayout()
            
            for label in row:
                button = Button( text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size=30, background_color= colors[1])

                if label in self.operators:
                    button.background_color = colors[0]

                # Adicionando o evento de clique ao botão
                button.bind(on_press=self.on_press_button)

                # Adicionando o botão ao layout
                h_layout.add_widget(button)
            
            
            # Adicionando o layout ao layout principal
            layout.add_widget(h_layout)

        # Adicionando o botão de igualdade

        # Associado a um manipulador de eventos
        
        return layout

        

    
    # Manipulador de eventos para o botão de igualdade

    def on_press_button(self, instance):

        # Extraem e avaliam a expressão matemática 
        current = self.solucao.text
        button_text = instance.text
        
        if button_text == '√':
            if current:
                num = float(current)
                if num > 0 :
                    self.solucao.text = str(sqrt(num))
                else:
                    self.solucao.text = 'Erro'

        elif button_text == 'C':
            # Limpa a tela
            self.solucao.text = ''

        elif button_text == '=':
            # Avalia a expressão matemática
            self.solucao.text = str(eval(self.solucao.text))

        elif button_text == 'π':
            self.solucao.text = str(pi)

        elif button_text == '%':
            self.solucao.text = str(eval(self.solucao.text)/100)

        elif button_text == '^': 
            self.solucao.text = str(pow(float(self.solucao.text),2))
        else:     # Verifica se a expressão possui um valor pré-existente

            # Verificam se o ultimo botão pressionado foi um operador, se foi um operador, não faz nada, por exemplo 2 + + 2 não é uma expressão válida
            if current and (self.last_was_operator and button_text in self.operators):
                return  ('Operador duplicado')
            
            # verifica sé o primeiro valor é um operador
            
            
            # Se nenhuma das condições acima for atendida, a expressão é avaliada
            else:
                new_text = current + button_text
                self.solucao.text = new_text

    # Define last_button no rótulo do ultimo botão pressionado
        self.last_button = button_text

    # Define last_was_operator como True ou False, dependendo do botão pressionado, se é ou não um caracter ou operador

        self.last_was_operator = self.last_button in self.operators

    # Manipulador de eventos para os botões
    # On_solucão é chamado quando o botão de igualdade é pressionado    

    def on_solucao(self, instance):
        #Estamos lidando com uma operação de atribuição
        text = self.solucao.text
        
        if text:  
                # Avalia a expressão matemática
            solucão = str(eval(self.solucao.text))
            self.solucao.text = solucão

if __name__ == '__main__':
    CalculadoraApp().run()




            


            
                
            


