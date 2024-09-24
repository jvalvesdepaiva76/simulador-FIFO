class Processo:
    def __init__(self, id_processo, tempo_chegada, tempo_execucao, memoria, io_necessario=False):
        self.id_processo = id_processo
        self.tempo_chegada = tempo_chegada
        self.tempo_execucao = tempo_execucao
        self.memoria = memoria
       
        self.status = "Pronto"
        self.tempo_inicio = None
        self.tempo_conclusao = None
        self.tempo_restante = tempo_execucao
       
        # Simulação de I/O
        self.io_necessario = io_necessario
        self.tempo_bloqueio = 0
        self.bloqueado = False

    def executar(self):
        if self.bloqueado:
            return False

        if self.tempo_restante > 0:
            self.tempo_restante -= 1
            return True
        else:
            self.status = "Concluído"
            return False

    def bloquear(self):
        if self.io_necessario:
            self.bloqueado = True
            self.status = "Bloqueado"
            self.tempo_bloqueio = random.randint(1, 5)

    def desbloquear(self):
        if self.bloqueado and self.tempo_bloqueio > 0:
            self.tempo_bloqueio -= 1
        if self.tempo_bloqueio == 0:
            self.bloqueado = False
            self.status = "Pronto"

    def __str__(self):
        return f"Processo {self.id_processo}: Execução restante: {self.tempo_restante}, Bloqueado: {self.bloqueado}"
