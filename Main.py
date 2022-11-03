#pyinstaller --onefile nome_arquivo.py -> transformar em .exe
#pyinstaller --onefile --noconsole nome_arquivo.py -> transformar em .exe sem console
#pyinstaller --onefile -w nome_arquivo.py -> transformar em .exe com janela UI
#pyinstaller --noconsole --name="MLOutPut" --ico="data-icon.ico" --add-data="data-icon.ico;." --onefile Main.py -> transformar em .exe com janela UI

from tkinter import *
from introdução_a_machine_learning_classificação_1 import training_model
import os

def funcao1():
    texto = training_model()
    print(texto)
    text2['text'] = texto

# Criando Janela Principal
window = Tk()

# Título
window.title("MLOutPut")

# Configurar tamanho de tela
#window.geometry("250x200")

# Mudando icone da janela
pastaApp = os.path.dirname(__file__)
window.iconbitmap(f'{pastaApp}\\data-icon.ico')

# Texto na Janela
text1 = Label(window, text="Clique no botão para ver o resultado \ndo treinamento do modelo")
text1.grid(column=0, row=0, padx=10, pady=10)

# Botão de Rodar Modelo
button = Button(window, text="Run Model", command=funcao1)
button.grid(column=0, row=1, padx=10, pady=10)

# Texto2 na Janela
text2 = Label(window, text="")
text2.grid(column=0, row=2, padx=10, pady=10)

# Para deixar a janela aberta
window.mainloop()