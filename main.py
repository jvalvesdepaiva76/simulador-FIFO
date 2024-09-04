from simulador import SimuladorFIFO
import json
import os

def listar_arquivos_programas(diretorio):
    try:
        arquivos = [f for f in os.listdir(diretorio) if f.endswith('.json')]
        if arquivos:
            print("Programas instalados:")
            for i, arquivo in enumerate(arquivos, start=1):
                print(f"{i}. {arquivo}")
            return arquivos
        else:
            print("Nenhum programa instalado encontrado.")
            return None
    except FileNotFoundError:
        print(f"Diretório {diretorio} não encontrado.")
        return None

def carregar_processos_de_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as f:
            processos = json.load(f)
            return processos
    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado.")
        return None

def main():
    simulador = SimuladorFIFO()
    
    escolha = input("Deseja (1) Adicionar processos manualmente ou (2) Carregar de um arquivo JSON? ")

    if escolha == '1':
        print("Insira os processos manualmente.")
        while True:
            try:
                tempo_chegada = int(input("Informe o tempo de chegada do processo: "))
                tempo_execucao = int(input("Informe o tempo de execução do processo: "))
                memoria = int(input("Informe a memória utilizada pelo processo: "))
                simulador.adicionar_processo(tempo_chegada, tempo_execucao, memoria)
                
                continuar = input("Deseja adicionar outro processo? (s/n): ")
                if continuar.lower() != 's':
                    break
            except ValueError:
                print("Por favor, insira um número válido.")
    
    elif escolha == '2':
        diretorio_programas = "programas"
        arquivos_programas = listar_arquivos_programas(diretorio_programas)
        
        if arquivos_programas:
            try:
                escolha_programa = int(input("Escolha o número do programa que deseja carregar: ")) - 1
                if 0 <= escolha_programa < len(arquivos_programas):
                    arquivo_escolhido = arquivos_programas[escolha_programa]
                    caminho_arquivo = os.path.join(diretorio_programas, arquivo_escolhido)
                    
                    processos = carregar_processos_de_arquivo(caminho_arquivo)
                    if processos:
                        for processo in processos:
                            simulador.adicionar_processo(processo['tempo_chegada'], processo['tempo_execucao'], processo['memoria'])
                else:
                    print("Escolha inválida. Encerrando o programa.")
                    return
            except ValueError:
                print("Entrada inválida. Encerrando o programa.")
                return
        else:
            return

    else:
        print("Escolha inválida. Encerrando o programa.")
        return

    simulador.executar_simulacao()

if __name__ == "__main__":
    main()
