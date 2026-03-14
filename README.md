# Mini Sistema de Adivinhação com Árvores (BFS e DFS)

## Descrição do Projeto

Este projeto implementa um sistema simples de adivinhação inspirado no Akinator.
O programa utiliza uma **árvore de decisão**, onde cada nó contém uma pergunta e cada folha contém uma resposta final.

O sistema também implementa dois algoritmos de busca em árvores:

* DFS (Depth-First Search)
* BFS (Breadth-First Search)

Além disso, o programa permite uma simulação de jogo onde o usuário responde perguntas até que o sistema encontre uma possível resposta.

---

# Estrutura da Árvore

A árvore utilizada no projeto possui a seguinte estrutura:

```
                É um dispositivo eletrônico?
                /                     \
             Sim                       Não
              |                         |
       É usado para comunicação?   É um meio de transporte?
           /           \              /            \
       Celular       Notebook      Carro        Bicicleta
```

Tipos de nós:

* **Nós internos:** perguntas
* **Nós folha:** respostas finais

---

# Algoritmos Implementados

## DFS (Depth First Search)

DFS significa **Busca em Profundidade**.

Esse algoritmo percorre um caminho completo da árvore antes de voltar para explorar outros caminhos.

### Funcionamento

1. Começa na raiz da árvore
2. Visita o nó atual
3. Vai para o primeiro filho
4. Continua até chegar a uma folha
5. Volta para explorar outros ramos

### Exemplo de ordem de visita

```
É um dispositivo eletrônico?
É usado para comunicação?
Celular
Notebook
É um meio de transporte?
Carro
Bicicleta
```

---

## BFS (Breadth First Search)

BFS significa **Busca em Largura**.

Esse algoritmo percorre a árvore **nível por nível**.

### Funcionamento

1. Começa na raiz
2. Visita todos os nós do nível atual
3. Depois passa para o próximo nível

### Exemplo de ordem de visita

```
É um dispositivo eletrônico?
É usado para comunicação?
É um meio de transporte?
Celular
Notebook
Carro
Bicicleta
```

---

# Comparação entre BFS e DFS

## Ordem de exploração

DFS explora **primeiro os caminhos mais profundos da árvore**.

BFS explora **todos os nós de um nível antes de ir para o próximo**.

---

## Qual algoritmo encontra resposta mais rápido em árvores profundas?

O **DFS** pode encontrar uma resposta mais rapidamente em árvores profundas, pois ele segue um caminho direto até o final da árvore.

---

## Qual algoritmo consome mais memória?

O **BFS consome mais memória**, porque ele precisa armazenar todos os nós de um nível na fila.

Já o DFS normalmente usa menos memória, pois percorre um caminho por vez.

---

## Quando usar BFS?

BFS é mais indicado quando queremos encontrar o **menor caminho** ou a solução mais próxima da raiz.

Exemplos:

* sistemas de rotas
* redes de computadores
* busca em grafos

---

## Quando usar DFS?

DFS é mais indicado quando queremos **explorar todas as possibilidades de uma árvore ou grafo**.

Exemplos:

* árvores de decisão
* jogos
* algoritmos de backtracking

---

# Execução do Sistema

Para executar o programa, utilize o comando:

```
python main.py
```

O programa irá:

1. Mostrar a ordem de visita usando DFS
2. Mostrar a ordem de visita usando BFS
3. Iniciar o jogo de adivinhação

---

# Exemplo de execução

```
É um dispositivo eletrônico? (s/n)
s

É usado para comunicação? (s/n)
s

A resposta é: Celular
```

---

# Criado por (Matheus Santa Ritta)


