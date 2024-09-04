from fila import FilaProcessos
from processo import Processo
import time

class SimuladorFIFO:
    def __init__(self):
        self.fila = FilaProcessos()
        self.proximo_id = 1  # ID inicial para processos

    def adicionar_processo(self, tempo_chegada, tempo_execucao, memoria):
        processo = Processo(self.proximo_id, tempo_chegada, tempo_execucao, memoria)
        self.fila.adicionar_processo(processo)
        self.proximo_id += 1

    def executar_simulacao(self):
        self.fila.ordenar_por_chegada()
        
        tempo_atual = 0
        while self.fila.tamanho_fila() > 0:
            processo_atual = self.fila.obter_proximo_processo()

            print(f"Processo {processo_atual.id_processo} está {processo_atual.status}.")

            # Aguardar o tempo de chegada do processo
            if tempo_atual < processo_atual.tempo_chegada:
                tempo_atual = processo_atual.tempo_chegada

            processo_atual.status = "Executando"
            processo_atual.tempo_inicio = tempo_atual
            print(f"Processo {processo_atual.id_processo} está {processo_atual.status}. "
                  f"Começando no tempo {tempo_atual}.")

            # Simulando tempo de execução
            time.sleep(processo_atual.tempo_execucao)
            tempo_atual += processo_atual.tempo_execucao

            processo_atual.status = "Concluído"
            processo_atual.tempo_conclusao = tempo_atual
            print(f"Processo {processo_atual.id_processo} está {processo_atual.status}. "
                  f"Concluído no tempo {tempo_atual}.")

