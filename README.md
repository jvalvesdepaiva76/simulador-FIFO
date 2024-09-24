---

# 🖥️ Simulador de Escalonamento FIFO em Python

## 🎯 **Objetivo**

Este projeto tem como objetivo analisar e implementar o algoritmo de escalonamento de processos **FIFO (First In, First Out)**, simulando o comportamento de processos em um ambiente de sistemas operacionais.

## 💡 **Justificativa**

O escalonamento de processos é crucial para a eficiência dos sistemas operacionais, impactando diretamente a performance e a experiência do usuário. Este projeto oferece uma oportunidade de entender o funcionamento do algoritmo FIFO no contexto de gerenciamento de processos.

## 📚 **Estudo Teórico**

Foram estudados os principais algoritmos de escalonamento de processos, incluindo:

- **FIFO (First In, First Out)**
- **SJF (Shortest Job First)**
- **RR (Round Robin)**
- **Prioridade**

**🔍 O algoritmo escolhido para este projeto foi o FIFO.**

## 🚀 **Funcionalidades Implementadas**

1. **Simulação de Escalonamento FIFO**:
   - Implementação de um simulador baseado no algoritmo FIFO.
   - Gerenciamento de processos com os seguintes parâmetros:
     - **⏰ Tempo de Chegada**
     - **🕒 Tempo de Execução**
     - **💾 Memória Utilizada**
     - **🔄 Status do Processo**:
       - **Pronto**: O processo está aguardando execução.
       - **Executando**: O processo está sendo executado.
       - **Concluído**: O processo terminou sua execução.
     - **🚀 Tempo de Início da Execução**: Registrado quando o processo começa a ser executado.
     - **🏁 Tempo de Conclusão**: Registrado quando o processo finaliza sua execução.

2. **Execução de Processos**:
   - Processos executados na ordem de chegada (FIFO).
   - Simulação em tempo real dos estados dos processos ("Pronto", "Executando", "Concluído").

3. **Interface Gráfica**:
   - Implementação de uma interface gráfica utilizando Tkinter.
   - O usuário pode adicionar processos manualmente ou carregar de um arquivo JSON.
   - Visualização gráfica dos processos em execução e da memória do sistema (representada por um paralelepípedo com 16 partições).
     - Quando um processo é executado, as partições de memória são preenchidas de acordo com o uso de memória do processo.

4. **Simulação Visual da Memória**:
   - Um paralelepípedo com 16 partições representa a memória do sistema.
   - Quando um processo está em execução, as partições correspondentes ao tamanho de memória são coloridas para indicar uso.
   - Após a conclusão do processo, a memória é liberada visualmente.

5. **Coleta de Métricas de Desempenho**:
   - **Tempo Médio de Espera**: O tempo médio que os processos aguardam na fila antes da execução.
   - **Tempo Médio de Resposta**: O tempo médio desde a chegada do processo até o início da execução.
   - **Tempo Médio de Execução (Turnaround)**: O tempo total que o processo leva desde sua chegada até sua conclusão.
   - **Throughput**: O número de processos finalizados por unidade de tempo da simulação.

## 📈 **Exemplo de Execução**

**Processos de Exemplo:**
```json
[
    {
        "tempo_chegada": 1,
        "tempo_execucao": 2,
        "memoria": 1
    },
    {
        "tempo_chegada": 2,
        "tempo_execucao": 3,
        "memoria": 6
    },
    {
        "tempo_chegada": 6,
        "tempo_execucao": 1,
        "memoria": 1
    }
]
```

**Métricas de Desempenho**:
```
Métricas de Desempenho:
Tempo médio de espera: 0.33
Tempo médio de resposta: 0.33
Tempo médio de execução: 2.33
Throughput: 0.43 processos por unidade de tempo.
```

## 🛠️ **Funcionalidades Futuras**

1. **Simulação de I/O e Bloqueio**:
   - Implementação de operações de I/O que suspendem temporariamente a execução dos processos.
   - Adição de tempo de bloqueio para simular espera por recursos.

2. **Expansão da Interface Gráfica**:
   - Opções para visualização mais detalhada do uso de memória e recursos.
   - Representação gráfica das operações de I/O e bloqueios dos processos.

3. **Melhoria na Visualização da Memória**:
   - Representar a memória com maior granularidade e ajustes dinâmicos.

4. **Compilação do Projeto em Executável**:
   - Planejamento para compilar o projeto em um executável utilizando ferramentas como PyInstaller.

## 🔧 **Instruções para Execução**

1. **Clonar o repositório**:
   ```bash
   git clone https://github.com/jvalvesdepaiva76/simulador-FIFO.git
   cd simulador-FIFO
   ```

2. **Instalar as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar o simulador**:
   ```bash
   python main.py
   ```

4. **Baixando tkinter**:
   No terminal execute o comando: apt-get install python3-tk
      ```bash
   apt-get install python3-tk
   ```

---

## 🤝 **Contribuições**

Contribuições são bem-vindas! Se você tem ideias para novas funcionalidades ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.
