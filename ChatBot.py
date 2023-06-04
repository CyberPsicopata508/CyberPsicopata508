import tkinter as tk
import openai

openai.api_key = "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"

def obter_resposta():
    pergunta = entrada.get()
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=pergunta,
        max_tokens=100,
        temperature=0.7
    )
    resposta = response.choices[0].text.strip()
    exibir_resposta(resposta)

def exibir_resposta(resposta):
    texto_resposta.config(state=tk.NORMAL)
    texto_resposta.delete("1.0", tk.END)
    texto_resposta.insert(tk.END, resposta)
    texto_resposta.config(state=tk.DISABLED)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Assistente Virtual")
janela.geometry("400x200")

# Entrada de pergunta
entrada = tk.Entry(janela, font=("Helvetica", 14))
entrada.pack(pady=10)

# Botão de enviar pergunta
botao_enviar = tk.Button(janela, text="Enviar", command=obter_resposta)
botao_enviar.pack()

# Área de exibição da resposta
texto_resposta = tk.Text(janela, height=5, width=40)
texto_resposta.config(state=tk.DISABLED)
texto_resposta.pack(pady=10)

janela.mainloop()
