import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
from transformers import pipeline, AutoTokenizer

nltk.download('punkt_tab')

def leitura(nome):
    arq = open(nome, 'r', encoding='utf-8')
    texto = arq.read()
    arq.close()
    return texto

def limpar(lista):
    lixo = '.,:;?!"\'()[]{}\/|#$%^&*-'
    quase_limpo = [x.strip(lixo).lower() for x in lista]
    return [x for x in quase_limpo if x.isalpha() or '-' in x]

corpus_base = leitura('corpus.txt')

sentencas_brutas = sent_tokenize(corpus_base, language='portuguese')

sentencas = [['<s>'] + limpar(word_tokenize(s, language='portuguese')) + ['</s>'] for s in sentencas_brutas]

arq = open('corpus_treino.txt', 'w',  encoding='utf-8')

for s in sentencas:
    arq.write(' '.join(s) + '\n')
arq.close()

arq = open('corpus_treino.txt', 'r', encoding='utf-8')
sentencas = arq.readlines()
arq.close()

vocab = set()
contagens = defaultdict(int)

for linha in sentencas:
    sent = linha.split()
    for palavra in sent:
        vocab |= {palavra}
        contagens[palavra] += 1

hapax = [p for p in contagens if contagens[p] == 1]
vocab -= set(hapax)
vocab |= {'<DES>'}

def ngramas(n, sent):
    return [tuple(sent[i:i+n]) for i in range(len(sent) - n + 1)]

unigramas = defaultdict(int)
bigramas = defaultdict(int)
trigramas = defaultdict(int)

for linha in sentencas:
    sent = linha.split()
    for i in range(len(sent)):
        if sent[i] in hapax:
            sent[i] = '<DES>'
    for x in ngramas(1, sent):
        unigramas[x] += 1
    for x in ngramas(2, sent):
        bigramas[x] += 1
    for x in ngramas(3, sent):
        trigramas[x] += 1

def prob_uni(x):
    V = len(vocab)
    N = sum(unigramas.values())
    return (unigramas[x] + 1) / (N + V)

def prob_bi(x):
    V = len(vocab)
    return (bigramas[x] + 1) / (unigramas[(x[0],)] + V)

def prob_tri(x):
    V = len(vocab)
    bigrama = (x[0], x[1])
    return (trigramas[x] + 1) / (bigramas[bigrama] + V)

def prever(palavra):
    lista = [ch for ch in bigramas if ch[0] == palavra]
    ordem = sorted(lista, key=lambda x: prob_bi(x), reverse=True)
    possibilidades = [x[1] for x in ordem[:3]]
    return possibilidades

def prever_trigramas(palavra1, palavra2):
    lista = [ch for ch in trigramas if ch[0] == palavra1 and ch[1] == palavra2]
    ordem = sorted(lista, key=lambda x: prob_tri(x), reverse=True)
    possibilidades = [x[2] for x in ordem[:3]]
    return possibilidades

def prever_proximas_palavras(palavra1, palavra2=None):
    palavrasBi = []
    palavrasTri = []
    if palavra2 is not None:
        palavrasTri = prever_trigramas(palavra1, palavra2)
        if not palavrasTri:
            palavrasBi = prever(palavra2)
            if not palavrasBi:
                print("Não foi possível prever.")
            else:
                print(f"As palavras previstas são: {palavrasBi}")
        else:
            print(f"As palavras previstas são: {palavrasTri}")
    else:
        palavrasBi = prever(palavra1)
        if not palavrasBi:
            print("Não foi possível prever.")
        else:
            print(f"As palavras previstas são: {palavrasBi}")
        

generator = pipeline("text-generation", model="TucanoBR/Tucano-2b4-Instruct")

def predicao_tucano(texto):

    completions = generator(texto, num_return_sequences=3, max_new_tokens=1)

    for i, comp in enumerate(completions):
        print(f"Opção {i + 1}: {comp['generated_text']}")


print("Olá, prevejo palavras do filme 'O auto da Compadecida'.")
anterior = []
opcao = input("\nDigite '1' para usar n-gramas, '2' para o modelo TUCANO e '0' para encerrar: ")

if(opcao == '1'):
    while True:
        palavra = input("\nDigite uma palavra ou '0' para encerrar: ")
        if palavra == '0':
            print("Encerrando o programa. Até logo!")
            break
        else:
            if not anterior:
                entrada = palavra
                palavras = entrada.strip().lower().split()
                if len(palavras) == 1:
                    prever_proximas_palavras(palavras[0])
                    anterior.append(palavra)
                else:
                    print("Digite apenas uma palavra")
            else:
                entrada = anterior[-1] + " " + palavra
                palavras = entrada.strip().lower().split()
                anterior.append(palavra)
                if len(palavras) == 2:
                    previsao = prever_proximas_palavras(palavras[0], palavras[1])
                else:
                    print("Por favor, digite no máximo uma palavra.")

elif(opcao == '2'):
    while True:
        palavra = input("\nDigite uma palavra ou '0' para encerrar: ")
        if palavra == '0':
            print("Encerrando o programa. Até logo!")
            break
        else:
            predicao_tucano(palavra)
