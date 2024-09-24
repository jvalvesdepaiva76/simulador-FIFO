import random
from fila import Fila
from processo import Processo

class SimuladorFIFO:
    def __init__(self):
        self.fila = Fila()
        self.proximo_id = 1
        self.processos_executados = []
        self.metricas = {
            "tempo_espera_total": 0,
            "tempo_resposta_total": 0,
            "tempo_execucao_total": 0,
            "processos_executados": 0,
            "tempo_total_simulacao": 0
        }

    def adicionar_processo(self, tempo_chegada, tempo_execucao, memoria, io_necessario=False):
        processo = Processo(self.proximo_id, tempo_chegada, tempo_execucao, memoria, io_necessario)
        self.fila.enfileirar(processo)
        self.proximo_id += 1

    def get_processos_em_fila(self):
        processos = []
        tempo_atual = 0

        while len(self.fila) > 0:
            processo = self.fila.desenfileirar()
            processos.append(processo)

            while processo.tempo_restante > 0:
                if processo.io_necessario:
                    processo.bloquear()
                    while processo.bloqueado:
                        processo.desbloquear()
                        tempo_atual += 1

                processo.executar()
                tempo_atual += 1

            # Calcular métricas
            tempo_espera = tempo_atual - processo.tempo_chegada
            if processo.tempo_inicio is None:
                processo.tempo_inicio = tempo_atual
                tempo_resposta = processo.tempo_inicio - processo.tempo_chegada
            else:
                tempo_resposta = 0

            self.metricas["tempo_espera_total"] += tempo_espera
            self.metricas["tempo_resposta_total"] += tempo_resposta
            self.metricas["processos_executados"] += 1

            processo.tempo_conclusao = tempo_atual
            self.metricas["tempo_execucao_total"] += (processo.tempo_conclusao - processo.tempo_chegada)

        self.metricas["tempo_total_simulacao"] = tempo_atual
        self.processos_executados = processos
        return processos

    def exibir_metricas(self):
        """Calcula e exibe as métricas de desempenho."""
        processos_executados = self.metricas["processos_executados"]

        if processos_executados > 0:
            tempo_medio_espera = self.metricas["tempo_espera_total"] / processos_executados
            tempo_medio_resposta = self.metricas["tempo_resposta_total"] / processos_executados
            tempo_medio_execucao = self.metricas["tempo_execucao_total"] / processos_executados
            throughput = processos_executados / self.metricas["tempo_total_simulacao"]

            print("\nMétricas de Desempenho:")
            print(f"Tempo médio de espera: {tempo_medio_espera:.2f}")
            print(f"Tempo médio de resposta: {tempo_medio_resposta:.2f}")
            print(f"Tempo médio de execução: {tempo_medio_execucao:.2f}")
            print(f"Throughput: {throughput:.2f} processos por unidade de tempo.")
        else:
            print("Nenhum processo foi executado.")


