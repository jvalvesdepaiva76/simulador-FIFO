# 🖥️ Simulador de Escalonamento FIFO em Python

## 🎯 **Objetivo**

Este projeto tem como objetivo analisar e implementar um algoritmo de escalonamento de processos **FIFO (First In, First Out)**.

## 💡 **Justificativa**

O escalonamento de processos é crucial para a eficiência dos sistemas operacionais, impactando diretamente a performance e a experiência do usuário. Este projeto oferece uma oportunidade para entender melhor o funcionamento de um algoritmo de escalonamento FIFO.

## 📚 **Estudo Teórico**

Antes de iniciar a implementação, foram estudados os principais algoritmos de escalonamento de processos, incluindo:

- **FIFO (First In, First Out)**
- **SJF (Shortest Job First)**
- **RR (Round Robin)**
- **Prioridade**

**🔍 O algoritmo escolhido para este projeto foi o FIFO.**

## 🚀 **Funcionalidades Implementadas**

1. **Simulação de Escalonamento FIFO**:
   - Implementação de um simulador de escalonamento de processos baseado no algoritmo FIFO.
   - Adição e gerenciamento de processos com os seguintes parâmetros:
     - **⏰ Tempo de Chegada**
     - **🕒 Tempo de Execução**
     - **💾 Memória Utilizada**
     - **🔄 Status do Processo**:
       - **Pronto**: O processo está na fila aguardando execução.
       - **Executando**: O processo está sendo executado.
       - **Concluído**: O processo terminou sua execução.
     - **🚀 Tempo de Início da Execução**: Registrado no momento em que o processo começa a ser executado.
     - **🏁 Tempo de Conclusão**: Registrado quando o processo finaliza sua execução.

2. **Execução de Processos**:
   - Os processos são executados na ordem de chegada (FIFO).
   - A simulação imprime em tempo real o status de cada processo à medida que ele avança de "Pronto" para "Executando" e, finalmente, "Concluído".

## 🛠️ **Funcionalidades Futuras**

1. **Coleta de Métricas de Desempenho**:
   - **Tempo de Espera Médio**: Cálculo do tempo médio que os processos esperam na fila antes de serem executados.
   - **Tempo de Resposta Médio**: Cálculo do tempo médio desde a chegada do processo até a sua conclusão.
   - **Throughput**: Medição do número de processos finalizados por unidade de tempo.

2. **Interface Gráfica**:
   - Adição de uma interface gráfica para facilitar a interação com o simulador.
   - Implementação planejada quando o projeto for convertido em um executável.

3. **Simulação de I/O e Tempo de Bloqueio**:
   - Simulação de processos que realizam operações de I/O, que podem suspender a execução do processo.
   - Implementação de tempos de bloqueio, simulando a espera por recursos ou operações de entrada/saída.

## 🔧 **Simulação**

O simulador foi desenvolvido em Python e permite a adição manual de processos ou o carregamento de processos a partir de arquivos JSON. Durante a simulação, o usuário pode observar a mudança de estado dos processos e seu tempo de execução, facilitando o entendimento do funcionamento do algoritmo FIFO.

## **Instruções para Execução (Ainda a implementar o executável)**

1. **Clonar o repositório**:
   ```bash
   git clone https://github.com/jvalvesdepaiva76/simulador-FIFO.git
   cd simulador-FIFO
   ```

2. **Executar o simulador**:
   ```bash
   python main.py
   ```

## 🤝 **Contribuições**

Contribuições são bem-vindas! Se você tem ideias para novas funcionalidades ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.