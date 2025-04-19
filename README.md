
# N-Gramas e Previsão de Palavras

Este projeto tem como objetivo implementar dois métodos para prever palavras em uma sequência de texto: **n-gramas** (unigramas, bigramas e trigramas) e o modelo de **geração de texto** do modelo **TUCANO**. O código está escrito em Python, utilizando bibliotecas como `nltk` e `transformers`.

## Funcionalidades

### 1. **Previsão com N-Gramas**
A previsão é baseada em modelos de n-gramas, sendo capaz de prever:
- **Unigramas**: Palavras independentes.
- **Bigramas**: Duplas de palavras consecutivas.
- **Trigramas**: Sequências de três palavras consecutivas.

O código realiza as seguintes etapas:
- **Leitura e limpeza do corpus**: O corpus é lido de um arquivo `corpus.txt` e tokenizado em sentenças e palavras.
- **Contagem de n-gramas**: O código cria contagens de unigramas, bigramas e trigramas.
- **Previsão de palavras**: Baseado nas palavras anteriores, o código sugere as próximas palavras possíveis.

### 2. **Previsão com o Modelo TUCANO**
Utilizando o modelo de **geração de texto** TUCANO da Hugging Face, o código pode prever a continuação de um texto dado. O modelo é treinado para gerar texto fluente e coerente em português.

### Como usar

1. **Instalação das dependências**:
   Certifique-se de que as bibliotecas necessárias estão instaladas. Você pode instalar as dependências usando o `pip`:

   ```bash
   pip install nltk transformers
   ```

2. **Execução do código**:
   O código pode ser executado diretamente com o seguinte comando:

   ```bash
   python main.py
   ```

   O programa vai apresentar um menu com as seguintes opções:
   - Digitar **1** para usar **n-gramas** e prever palavras baseadas nas anteriores.
   - Digitar **2** para usar o modelo **TUCANO** e gerar texto de maneira mais fluente.
   - Digitar **0** para encerrar o programa.

   **Exemplo de interação**:
   - O programa solicitará que você digite uma palavra e, com base nela, preverá a próxima palavra ou sequência.

3. **Arquivos**:
   - **corpus.txt**: Arquivo de texto contendo o corpus de treinamento. O código usa este arquivo para aprender as palavras e gerar previsões.
   - **corpus_treino.txt**: Arquivo gerado pelo programa, contendo as sentenças tokenizadas e preparadas para treinamento.

### Estrutura do código

O código é dividido em funções que fazem o seguinte:

- **leitura(nome)**: Lê o conteúdo de um arquivo de texto.
- **limpar(lista)**: Limpa palavras removendo pontuação e caracteres especiais.
- **ngramas(n, sent)**: Gera n-gramas a partir de uma sentença.
- **prob_*()**: Calcula a probabilidade de um n-grama ocorrer.
- **prever_*()**: Funções para prever a próxima palavra com base no modelo de n-gramas ou trigramas.
- **predicao_tucano()**: Usa o modelo TUCANO para gerar texto.

### Exemplo de Previsão com N-Gramas

Ao executar o programa e escolher a opção `1`, você pode prever palavras baseadas na entrada dada:

```
Digite uma palavra ou '0' para encerrar: auto
As palavras previstas são: ['da', 'das', 'do']
```

### Exemplo de Previsão com TUCANO

Ao escolher a opção `2`, você pode gerar texto usando o modelo TUCANO:

```
Digite uma palavra ou '0' para encerrar: auto
Opção 1: Auto da Compadecida - Geração de Texto com TUCANO
Opção 2: O auto da Compadecida - A continuação do drama
Opção 3: Auto da Compadecida - Continuação do enredo.
```

---

### Dependências

- `nltk`: Biblioteca para processamento de linguagem natural.
- `transformers`: Biblioteca da Hugging Face para utilização de modelos de linguagem como TUCANO.

### Contribuições

Contribuições são bem-vindas! Caso tenha sugestões ou melhorias, fique à vontade para abrir uma **issue** ou **pull request**.

