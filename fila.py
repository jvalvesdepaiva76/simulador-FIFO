from processo import Processo

class FilaProcessos:
    def __init__(self):
        self.fila = []

    def adicionar_processo(self, processo):
        self.fila.append(processo)

    def ordenar_por_chegada(self):
        self.fila.sort(key=lambda processo: processo.tempo_chegada)

    def obter_proximo_processo(self):
        if len(self.fila) > 0:
            return self.fila.pop(0)
        return None

    def tamanho_fila(self):
        return len(self.fila)
