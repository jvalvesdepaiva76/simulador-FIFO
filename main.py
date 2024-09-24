import tkinter as tk
from tkinter import filedialog, messagebox
from simulador import SimuladorFIFO
import json
import threading


import tkinter as tk
from tkinter import filedialog, messagebox
from simulador import SimuladorFIFO
import json
import threading


import tkinter as tk
from tkinter import filedialog, messagebox
from simulador import SimuladorFIFO
import json
import threading


class SimuladorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador FIFO")

        self.simulador = SimuladorFIFO()

        # Labels e Inputs para Adicionar Processos Manualmente
        self.lbl_chegada = tk.Label(root, text="Tempo de Chegada:")
        self.lbl_chegada.grid(row=0, column=0)
        self.entry_chegada = tk.Entry(root)
        self.entry_chegada.grid(row=0, column=1)

        self.lbl_execucao = tk.Label(root, text="Tempo de Execução:")
        self.lbl_execucao.grid(row=1, column=0)
        self.entry_execucao = tk.Entry(root)
        self.entry_execucao.grid(row=1, column=1)

        self.lbl_memoria = tk.Label(root, text="Memória Utilizada:")
        self.lbl_memoria.grid(row=2, column=0)
        self.entry_memoria = tk.Entry(root)
        self.entry_memoria.grid(row=2, column=1)

        # Checkbox para I/O necessário
        self.io_var = tk.IntVar()
        self.chk_io_necessario = tk.Checkbutton(root, text="I/O Necessário", variable=self.io_var)
        self.chk_io_necessario.grid(row=3, column=0)

        # Botão para Adicionar Processos Manualmente
        self.btn_adicionar_processo = tk.Button(root, text="Adicionar Processo", command=self.adicionar_processo)
        self.btn_adicionar_processo.grid(row=4, column=0, columnspan=2, pady=5)

        # Botão para Carregar Processos de um Arquivo JSON
        self.btn_carregar_arquivo = tk.Button(root, text="Carregar de Arquivo JSON", command=self.carregar_arquivo)
        self.btn_carregar_arquivo.grid(row=5, column=0, columnspan=2, pady=5)

        # Botão para Executar a Simulação
        self.btn_executar_simulacao = tk.Button(root, text="Executar Simulação", command=self.executar_simulacao_thread)
        self.btn_executar_simulacao.grid(row=6, column=0, columnspan=2, pady=5)

        # Lista de Processos
        self.processos_listbox = tk.Listbox(root, height=10, width=70)
        self.processos_listbox.grid(row=7, column=0, columnspan=2, pady=5)

        # Status da Simulação
        self.lbl_status = tk.Label(root, text="Status da Simulação:")
        self.lbl_status.grid(row=8, column=0, columnspan=2)
        self.text_status = tk.Text(root, height=20, width=50)
        self.text_status.grid(row=9, column=0, columnspan=2)

    def adicionar_processo(self):
        try:
            tempo_chegada = int(self.entry_chegada.get())
            tempo_execucao = int(self.entry_execucao.get())
            memoria = int(self.entry_memoria.get())
            io_necessario = self.io_var.get() == 1  # Verifica se o checkbox está marcado

            # Adiciona o processo no simulador
            self.simulador.adicionar_processo(tempo_chegada, tempo_execucao, memoria, io_necessario)

            # Adicionar o processo à lista na interface
            self.processos_listbox.insert(tk.END, f"Processo - Chegada: {tempo_chegada}, Execução: {tempo_execucao}, Memória: {memoria}, I/O: {'Sim' if io_necessario else 'Não'}")

            # Limpar campos de entrada
            self.entry_chegada.delete(0, tk.END)
            self.entry_execucao.delete(0, tk.END)
            self.entry_memoria.delete(0, tk.END)
            self.io_var.set(0)  # Desmarcar o checkbox de I/O
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def carregar_arquivo(self):
        caminho_arquivo = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if caminho_arquivo:
            try:
                with open(caminho_arquivo, 'r') as f:
                    processos = json.load(f)
                    for processo in processos:
                        self.simulador.adicionar_processo(processo['tempo_chegada'], processo['tempo_execucao'], processo['memoria'], processo.get('io_necessario', False))
                        self.processos_listbox.insert(tk.END, f"Processo - Chegada: {processo['tempo_chegada']}, Execução: {processo['tempo_execucao']}, Memória: {processo['memoria']}, I/O: {'Sim' if processo.get('io_necessario', False) else 'Não'}")
            except (FileNotFoundError, json.JSONDecodeError):
                messagebox.showerror("Erro", "Erro ao carregar o arquivo JSON.")

    def executar_simulacao_thread(self):
        """Inicia a simulação em uma thread separada."""
        thread_simulacao = threading.Thread(target=self.executar_simulacao)
        thread_simulacao.start()

    def executar_simulacao(self):
        self.text_status.delete(1.0, tk.END)
        processos = self.simulador.get_processos_em_fila()
        self.processar_proximos_processos(processos, 0)

    def processar_proximos_processos(self, processos, index):
        if index < len(processos):
            processo = processos[index]
            status = f"Processando: Processo {processo.id_processo}, Execução: {processo.tempo_execucao}s\n"
            self.atualizar_status(status)

            tempo_execucao_ms = processo.tempo_execucao * 1000
            self.root.after(tempo_execucao_ms, lambda: self.finalizar_processo(processo, processos, index))
        else:
            self.atualizar_status("Simulação finalizada.\n")
            self.exibir_metricas()

    def finalizar_processo(self, processo, processos, index):
        status_final = f"Finalizado: Processo {processo.id_processo}\n"
        self.atualizar_status(status_final)
        self.processar_proximos_processos(processos, index + 1)

    def atualizar_status(self, mensagem):
        self.text_status.insert(tk.END, mensagem)
        self.text_status.see(tk.END)

    def exibir_metricas(self):
        """Exibe as métricas de desempenho no campo de status."""
        metricas = self.simulador.metricas
        processos_executados = metricas["processos_executados"]

        if processos_executados > 0:
            tempo_medio_espera = metricas["tempo_espera_total"] / processos_executados
            tempo_medio_resposta = metricas["tempo_resposta_total"] / processos_executados
            tempo_medio_execucao = metricas["tempo_execucao_total"] / processos_executados
            throughput = processos_executados / metricas["tempo_total_simulacao"]

            # Exibir as métricas no campo de status
            self.atualizar_status("\nMétricas de Desempenho:\n")
            self.atualizar_status(f"Tempo médio de espera: {tempo_medio_espera:.2f}\n")
            self.atualizar_status(f"Tempo médio de resposta: {tempo_medio_resposta:.2f}\n")
            self.atualizar_status(f"Tempo médio de execução: {tempo_medio_execucao:.2f}\n")
            self.atualizar_status(f"Throughput: {throughput:.2f} processos por unidade de tempo.\n")
        else:
            self.atualizar_status("Nenhum processo foi executado.\n")


# Main loop do Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorApp(root)
    root.mainloop()

