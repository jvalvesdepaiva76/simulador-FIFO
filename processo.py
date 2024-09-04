class Processo:
    def __init__(self, id_processo, tempo_chegada, tempo_execucao, memoria):
        self.id_processo = id_processo
        self.tempo_chegada = tempo_chegada
        self.tempo_execucao = tempo_execucao
        self.memoria = memoria
        
        self.status = "Pronto"
        self.tempo_inicio = None
        self.tempo_conclusao = None
        
        # Placeholder para futuras funcionalidades:
        self.io_necessario = False  # Simulação de I/O
        self.tempo_bloqueio = 0  # Placeholder para tempo de bloqueio
