from selenium import webdriver 
import time 

navegador = webdriver.Chrome() #abrir o navegador

navegador.get("https://hashtagtreinamentos.com/") # acessar um site

navegador.maximize_window() # colocar o navegador em tela cheia

botao_verde = navegador.find_element("class name", "botao-verde") # selecionar um elemento na tela

botao_verde.click() #clickar em um elemento

# encontrar varios elementos
lista_botoes = navegador.find_elements("class name", "header__titulo") # selecionar um elemento na tela

for botao in lista_botoes:
    if "Assinatura" in botao.text:
        botao.click() # clickar 
        break 
 
 # selecionar uma aba 
abas = navegador.window_handles # cria uma variavel com as abas que estao sendo usadas
navegador.switch_to.window(abas[1]) #seleciona a aba pelo índice

 # navegar para um site diferente 
navegador.get("https://www.hashtagtreinamentos.com/curso-python") # acessa esse site

#escrever em um campo / formulário
campo_nome = navegador.find_element("id", "firstname") # Seleciona o elemento pelo id e armazena na variavel
campo_email = navegador.find_element("id", "email") # Seleciona o elemento pelo id e armazena na variavel
campo_phone = navegador.find_element("id", "phone") # Seleciona o elemento pelo id e armazena na variavel
botao_submit = navegador.find_element("id", "_form_2475_submit") # Seleciona o elemento pelo id e armazena na variavel

campo_nome.send_keys("Guilherme") # preenche o campo 
campo_email.send_keys("Guilherme@gmail.com") # preenche o campo 
campo_phone.send_keys("51 983357480") # preenche o campo 

#dar scroll (colocar um elemento na tela)
navegador.execute_script("arguments[0].scrollIntoView({block:'center'})", botao_submit) #executa um comando javascript 
time.sleep(3)

botao_submit.click() #clicka no botao 

time.sleep(10) #definir o tempo que o navegador fica aberto
