from simulador import SimuladorFIFO

def main():
    simulador = SimuladorFIFO()

    simulador.adicionar_processo(1, 0, 5)
    simulador.adicionar_processo(2, 2, 3)
    simulador.adicionar_processo(3, 4, 2)

    simulador.executar_simulacao()

if __name__ == "__main__":
    main()
