from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# # Importações padrões para atualizar o chromedriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
# # Instalar a versão atualizada do chromedriver se estiver desatualizada
# servico = Service(ChromeDriverManager().install())

# Pegar a cotação do dólar

# Abrir o navegador
navegador = webdriver.Chrome()
# Entrar no google
navegador.get("https://www.google.com/")
# Escrever cotação dólar na barra de pesquisa
navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys('cotação dólar')
# Dar enter para pesquisar
navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys(Keys.ENTER)
# Pegar a cotação do dólar através do xpath da cotação
cdolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
# Pegar a cotação do euro

# Entrar no google
navegador.get("https://www.google.com/")
# Escrever cotação euro na barra de pesquisa
navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys('cotação euro')
# Dar enter para pesquisar
navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys(Keys.ENTER)
# Pegar a cotação do euro através do xpath da cotação
ceuro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Pegar a cotação do ouro

# Entrar no site da cotação do ouro, pois se pesquisar direto do google não aparece
navegador.get("https://www.melhorcambio.com/ouro-hoje")
# Pegar a cotação do ouro através da xpath da cotação
couro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')

# Pegar a Cotação do Bitcoin:

# Entrar no site 'www.google.com'.
navegador.get("https://www.google.com")
# Clicar no elemento indicado.
navegador.find_element('xpath', '//*[@id="APjFqb"]').click()
# Escrever 'Cotação Bitcoin' no elemento indicado.
navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys('Cotação Bitcoin')
# Dar Enter
navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys(Keys.ENTER)
# Pegar um atributo de um elemento.
cb = navegador.find_element('xpath', '//*[@id="crypto-updatable_2"]/div[3]/div[5]/div[2]/input').get_attribute('value')

navegador.minimize_window()

# Transforma o ponto do dólar em vírgula
cdolar = f'{float(cdolar):.2f}'
cdolar = str(cdolar)
cdolar = cdolar.split('.')
cdolar = cdolar[0] + ',' + cdolar[1]

# Transforma o ponto do euro em vírgula
ceuro = f'{float(ceuro):.2f}'
ceuro = str(ceuro)
ceuro = ceuro.split('.')
ceuro = ceuro[0] + ',' + ceuro[1]

# Trocar o ponto para a vírgula e colocar um ponto na separação da casa de milhar.
cbitcoin = f'{float(cb):,.2f}'
cbitcoin = cbitcoin.split(',')
cc = cbitcoin[1]
cbitcoin = cbitcoin[0]
cc = cc.split('.')
cbitcoin = cbitcoin + '.' + cc[0] + ',' + cc[1]

d = 1
e = 1
o = 1
b = 1

# Para o botão do Cotação dólar aparecer o text1 e sair
def dolar():
        global d
        if d == 1:
                text1.grid(column=0, row=4)
                d = 2
        else:
                text1.grid_forget()
                d = 1

# Para o botão do Cotação euro aparecer o text2 e sair
def euro():
        global e
        if e == 1:
                text2.grid(column=0, row=6)
                e = 2
        else:
                text2.grid_forget()
                e = 1

def bitcoin():
        global b
        if b == 1:
               text3.grid(column=0, row=10)
               b = 2
        else:
                text3.grid_forget()
                b = 1

# Para o botão do Cotação ouro aparecer o text3 e sair
def ouro():
        global o
        if o == 1:
               text4.grid(column=0, row=8)
               o = 2
        else:
                text4.grid_forget()
                o = 1

# Abrir uma janela
janela = Tk()
# Dar nome a essa janela
janela.title('Cotação das moedas')

s = Label(janela, text='')

s.grid(column=0, row=1)

# Texto que vai aparecer na janela
texto = Label(janela, text='Clique no botão para ver a cotação.', font=('impact', 15))
# Coluna e linha do texto
texto.grid(column=0, row=0)

# Texto que vai aparecer quando clicar na cotação dólar
text1 = Label(janela, text=f'Cotação Dólar: R${cdolar}', font=('Comic Sans MS', 13))

# Texto que vai aparecer quando clicar na cotação euro
text2 = Label(janela, text=f'Cotação Euro: R${ceuro}', font=('Comic Sans MS', 13))

# Texto que vai aparecer quando clicar na cotação dólar
text3 = Label(janela, text=f'Cotação Bitcoin: R${cbitcoin}', font=('Comic Sans MS', 13))

# Texto que vai aparecer quando clicar na cotação ouro
text4 = Label(janela, text=f'Cotação Ouro: R${couro}', font=('Comic Sans MS', 13))

# Botão para aparecer a cotação do dólar
botao_dolar = Button(janela, text='Cotação Dólar', command=dolar, font=('impact', 15), bg='blue')
# Para colocar a cor verde no texto do botão
botao_dolar.config(fg='green')
# Coluna e linha do botão da cotação do dólar
botao_dolar.grid(column=0, row=3)

# Botão para aparecer a cotação do euro
botao_euro = Button(janela, text='Cotação Euro', command=euro, font=('impact', 15), bg='blue')
# Para colocar a cor verde no texto do botão
botao_euro.config(fg='green')
# Coluna e linha do botão da cotação do euro
botao_euro.grid(column=0, row=5)

# Botão para aparecer a cotação do ouro
botao_ouro = Button(janela, text='Cotação Ouro', command=ouro, font=('impact', 15), bg='blue')
# Para colocar a cor verde no texto do botão
botao_ouro.config(fg='green')
# Coluna e linha do botão da cotação do ouro
botao_ouro.grid(column=0, row=7)

# Botão para aparecer a cotação do bitcoin
botao_bitcoin = Button(janela, text='Cotação Bitcoin', command=bitcoin, font=('impact', 15), bg='blue')
# Para colocar a cor verde no texto do botão
botao_bitcoin.config(fg='green')
# Coluna e linha do botão da cotação do ouro
botao_bitcoin.grid(column=0, row=9)

janela.mainloop()
