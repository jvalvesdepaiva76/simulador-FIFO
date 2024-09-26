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

        self.btn_clear_all = tk.Button(root, text="Limpar Tudo", command=self.clear_all)
        self.btn_clear_all.grid(row=7, column=0, columnspan=2, pady=5)

        # Lista de Processos
        self.processos_listbox = tk.Listbox(root, height=10, width=70)
        self.processos_listbox.grid(row=8, column=0, columnspan=2, pady=5)


        # Canvas para representação gráfica da simulação
        self.canvas = tk.Canvas(root, width=600, height=300, bg="white")
        self.canvas.grid(row=9, column=0, columnspan=2, pady=5)


        # Campo de texto para exibir as métricas de desempenho
        self.text_metricas = tk.Text(root, height=10, width=70)
        self.text_metricas.grid(row=10, column=0, columnspan=2, pady=5)


        # Armazenar referência visual de processos
        self.processos_visuais = {}

        # Memória visual (16 partições)
        self.memoria_visual = []
        self.desenhar_memoria()

    def clear_all(self):
        # Limpar campos de entrada
        self.entry_chegada.delete(0, tk.END)
        self.entry_execucao.delete(0, tk.END)
        self.entry_memoria.delete(0, tk.END)
        self.io_var.set(0)  # Desmarcar o checkbox de I/O

        # Limpar a lista de processos
        self.processos_listbox.delete(0, tk.END)

        # Limpar o canvas e redesenhar a memória
        self.canvas.delete("all")
        self.desenhar_memoria()

        # Limpar o campo de métricas
        self.text_metricas.delete(1.0, tk.END)

        # Resetar o simulador
        self.simulador = SimuladorFIFO()

    def desenhar_memoria(self):
        """Desenha um paralelepípedo dividido em 16 partições representando a memória."""
        self.memoria_visual = []
        x0, y0, largura, altura = 10, 250, 35, 20  # Definir o tamanho de cada partição de memória
        for i in range(16):
            x1 = x0 + largura
            y1 = y0 + altura
            particao = self.canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")
            self.memoria_visual.append(particao)
            x0 = x1 + 2  # Adicionar espaço entre as partições


    def atualizar_memoria_visual(self, memoria_necessaria, cor):
        """Atualiza as partições da memória com a cor correspondente ao processo executando."""
        for i in range(memoria_necessaria):
            if i < len(self.memoria_visual):  # Para evitar exceções
                self.canvas.itemconfig(self.memoria_visual[i], fill=cor)


        # Força a atualização imediata da interface gráfica
        self.root.update_idletasks()


    def liberar_memoria_visual(self):
        """Libera todas as partições de memória, retornando à cor branca."""
        for particao in self.memoria_visual:
            self.canvas.itemconfig(particao, fill="white")


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


            # Desenhar processo na interface gráfica
            self.desenhar_processo_visual(self.simulador.proximo_id - 1, tempo_execucao, memoria)


            # Limpar campos de entrada
            self.entry_chegada.delete(0, tk.END)
            self.entry_execucao.delete(0, tk.END)
            self.entry_memoria.delete(0, tk.END)
            self.io_var.set(0)  # Desmarcar o checkbox de I/O
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")


    def desenhar_processo_visual(self, id_processo, tempo_execucao, memoria):
        """Desenha um processo como uma barra colorida na canvas."""
        x0, y0 = 10, 20 + (id_processo * 30)  # Posicionamento inicial baseado no ID
        x1 = 10 + (tempo_execucao * 20)  # Largura do retângulo proporcional ao tempo de execução
        y1 = y0 + 20


        cor = "green"  # Cor inicial para processos prontos
        processo_visual = self.canvas.create_rectangle(x0, y0, x1, y1, fill=cor)
        texto_visual = self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=f"ID {id_processo}")
        self.processos_visuais[id_processo] = (processo_visual, texto_visual)


    def atualizar_processo_visual(self, id_processo, status):
        """Atualiza a cor do processo na visualização com base no status."""
        processo_visual, _ = self.processos_visuais[id_processo]


        cor_status = {
            "Pronto": "green",
            "Executando": "blue",
            "Bloqueado": "orange",
            "Concluído": "gray"
        }
        nova_cor = cor_status.get(status, "green")
        self.canvas.itemconfig(processo_visual, fill=nova_cor)


        # Força a atualização imediata da interface gráfica
        self.root.update_idletasks()


    def carregar_arquivo(self):
        caminho_arquivo = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if caminho_arquivo:
            try:
                with open(caminho_arquivo, 'r') as f:
                    processos = json.load(f)
                    for processo in processos:
                        self.simulador.adicionar_processo(processo['tempo_chegada'], processo['tempo_execucao'], processo['memoria'], processo.get('io_necessario', False))
                        self.processos_listbox.insert(tk.END, f"Processo - Chegada: {processo['tempo_chegada']}, Execução: {processo['tempo_execucao']}, Memória: {processo['memoria']}, I/O: {'Sim' if processo.get('io_necessario', False) else 'Não'}")
                        self.desenhar_processo_visual(self.simulador.proximo_id - 1, processo['tempo_execucao'], processo['memoria'])
            except (FileNotFoundError, json.JSONDecodeError):
                messagebox.showerror("Erro", "Erro ao carregar o arquivo JSON.")


    def executar_simulacao_thread(self):
        """Inicia a simulação em uma thread separada."""
        thread_simulacao = threading.Thread(target=self.executar_simulacao)
        thread_simulacao.start()

    def executar_simulacao(self):
        self.text_metricas.delete(1.0, tk.END)  # Limpar o campo de texto das métricas
        processos = self.simulador.get_processos_em_fila()
        self.processar_proximos_processos(processos, 0)

    def processar_proximos_processos(self, processos, index):
        if index < len(processos):
            processo = processos[index]
            self.atualizar_processo_visual(processo.id_processo, "Executando")
            self.atualizar_memoria_visual(processo.memoria, "gray")  # Atualizar a memória conforme o processo executa


            tempo_execucao_ms = processo.tempo_execucao * 1000
            self.root.after(tempo_execucao_ms, lambda: self.finalizar_processo(processo, processos, index))
        else:
            self.exibir_metricas()


    def finalizar_processo(self, processo, processos, index):
        self.atualizar_processo_visual(processo.id_processo, "Concluído")
        self.liberar_memoria_visual()  # Libera a memória após o processo terminar
        self.processar_proximos_processos(processos, index + 1)


    def exibir_metricas(self):
        """Exibe as métricas de desempenho no campo de texto."""
        metricas = self.simulador.metricas
        processos_executados = metricas["processos_executados"]


        if processos_executados > 0:
            tempo_medio_espera = metricas["tempo_espera_total"] / processos_executados
            tempo_medio_resposta = metricas["tempo_resposta_total"] / processos_executados
            tempo_medio_execucao = metricas["tempo_execucao_total"] / processos_executados
            throughput = processos_executados / metricas["tempo_total_simulacao"]


            # Exibir as métricas no campo de texto
            self.text_metricas.insert(tk.END, "\nMétricas de Desempenho:\n")
            self.text_metricas.insert(tk.END, f"Tempo médio de espera: {tempo_medio_espera:.2f}\n")
            self.text_metricas.insert(tk.END, f"Tempo médio de resposta: {tempo_medio_resposta:.2f}\n")
            self.text_metricas.insert(tk.END, f"Tempo médio de execução: {tempo_medio_execucao:.2f}\n")
            self.text_metricas.insert(tk.END, f"Throughput: {throughput:.2f} processos por unidade de tempo.\n")
        else:
            self.text_metricas.insert(tk.END, "Nenhum processo foi executado.\n")


# Main loop do Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorApp(root)
    root.mainloop()
