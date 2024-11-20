import tkinter as tk
from tkinter import messagebox
import os
import sys

def calcular_media():
    try:
        nota1 = float(entry_nota1.get())
        nota2 = float(entry_nota2.get())
        nota3 = float(entry_nota3.get())

        res1 = nota1 * 1
        res2 = nota2 * 2
        res3 = nota3 * 3

        soma = res1 + res2 + res3
        media = soma / 6
        media_arredondada = round(media, 1)

        messagebox.showinfo("Resultado", f"Média: {media_arredondada}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos ou use '.'")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cálculo de Média")

# Define o tamanho da janela
janela.geometry("300x200")  # Largura x Altura
janela.resizable(False, False)  # Impede redimensionamento

# Icone do aplicativo
# Obter o caminho do ícone corretamente, mesmo após a conversão para .exe
if getattr(sys, 'frozen', False):
    # Quando o script é executado como .exe
    icone_path = os.path.join(sys._MEIPASS, "cosin.ico")
else:
    # Quando o script é executado diretamente
    icone_path = os.path.join(os.path.dirname(__file__), "cosin.ico")

janela.iconbitmap(icone_path)

# Criação de um frame centralizado
frame = tk.Frame(janela)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o frame na janela

# Labels e entradas para as notas
tk.Label(frame, text="Nota 1:").grid(row=0, column=0, padx=10, pady=5)
entry_nota1 = tk.Entry(frame)
entry_nota1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Nota 2:").grid(row=1, column=0, padx=10, pady=5)
entry_nota2 = tk.Entry(frame)
entry_nota2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Nota 3:").grid(row=2, column=0, padx=10, pady=5)
entry_nota3 = tk.Entry(frame)
entry_nota3.grid(row=2, column=1, padx=10, pady=5)

# Botão para calcular a média
btn_calcular = tk.Button(frame, text="Calcular Média", command=calcular_media)
btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

# Inicia o loop da interface
janela.mainloop()
