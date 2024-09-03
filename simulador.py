from fila import FilaProcessos
from processo import Processo

class SimuladorFIFO:
    def __init__(self):
        self.fila = FilaProcessos()

    def adicionar_processo(self, id_processo, tempo_chegada, tempo_execucao):
        processo = Processo(id_processo, tempo_chegada, tempo_execucao)
        self.fila.adicionar_processo(processo)

    def executar_simulacao(self):
        self.fila.ordenar_por_chegada()
        
        tempo_atual = 0
        while self.fila.tamanho_fila() > 0:
            processo_atual = self.fila.obter_proximo_processo()
            
            if tempo_atual < processo_atual.tempo_chegada:
                tempo_atual = processo_atual.tempo_chegada

            print(f"Executando processo {processo_atual.id_processo} "
                  f"com tempo de execução {processo_atual.tempo_execucao} "
                  f"no tempo {tempo_atual}")
            
            tempo_atual += processo_atual.tempo_execucao
