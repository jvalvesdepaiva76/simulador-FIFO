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
        """Adiciona um novo processo à fila de execução"""
        processo = Processo(self.proximo_id, tempo_chegada, tempo_execucao, memoria, io_necessario)
        self.fila.enfileirar(processo)
        self.proximo_id += 1

    def get_processos_em_fila(self):
        """Executa os processos sem tempo simulado e calcula as métricas"""
        processos = []
        tempo_conclusao_anterior = 0  # Mantém o tempo de conclusão do processo anterior

        while len(self.fila) > 0:
            processo = self.fila.desenfileirar()
            processos.append(processo)

            # O processo inicia quando chega a sua vez de execução
            processo.tempo_inicio = max(tempo_conclusao_anterior, processo.tempo_chegada)

            # O processo termina depois de ser executado
            processo.tempo_conclusao = processo.tempo_inicio + processo.tempo_execucao
            tempo_conclusao_anterior = processo.tempo_conclusao

            # Calcular tempos para métricas
            processo.tempo_espera = processo.tempo_inicio - processo.tempo_chegada  # Tempo de Espera
            processo.tempo_resposta = processo.tempo_conclusao - processo.tempo_chegada  # Tempo de Resposta

            # Atualizar métricas globais
            self.metricas["tempo_espera_total"] += processo.tempo_espera
            self.metricas["tempo_resposta_total"] += processo.tempo_resposta
            self.metricas["tempo_execucao_total"] += processo.tempo_execucao
            self.metricas["processos_executados"] += 1

        # Define o tempo total de simulação como o tempo do último processo concluído
        self.metricas["tempo_total_simulacao"] = tempo_conclusao_anterior
        self.processos_executados = processos
        return processos

    def exibir_metricas(self):
        """Calcula e exibe as métricas ao final da simulação"""
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
