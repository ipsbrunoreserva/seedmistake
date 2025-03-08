from mnemonic import Mnemonic
from Levenshtein import distance
from itertools import islice, product
import hashlib
import hmac
import binascii
import bech32
from concurrent.futures import ThreadPoolExecutor, as_completed
from bitcoinlib.keys import HDKey
# Criar instância do BIP-39 para inglês
mnemo = Mnemonic("english")

# Obter a lista de palavras BIP-39
bip39_words = mnemo.wordlist
from mnemonic import Mnemonic
from bip32utils import BIP32Key
from bitcoinlib.keys import HDKey
mnemo = Mnemonic("english")
derivation_path = "m/84'/0'/0'/0/0"

def get_first_segwit_address(seed_words):

    seed = mnemo.to_seed(seed_words)
    
    # Gerar chave mestre
    master_key = HDKey.from_seed(seed, key_type='standard')

    child_key = master_key.subkey_for_path(derivation_path)
    
    # Gerar endereço SegWit
    return child_key.address()


# Seed errada recebida
seed_received = ["mister", "abandon", "pluck", "copper", "abandon", "merge",
                 "abandon", "abandon", "tree", "abandon", "state", "round"]


def find_similar_words(word, word_list, max_distance=2, max_results=3):
    # Calcula a distância para cada palavra e armazena com a palavra
    similar_words = [(w, distance(word, w)) for w in word_list if distance(word, w) <= max_distance]
    
    # Ordena por distância (menor primeiro)
    similar_words = sorted(similar_words, key=lambda x: x[1])
    
    # Pega apenas as palavras (sem as distâncias) e limita a 10
    result = [w for w, d in similar_words][:max_results]
    
    # Retorna a lista ou a palavra original se não houver similares
    return result if result else [word]

# Criar um dicionário de palavras parecidas para cada palavra errada
seeds_parecidas = {word: find_similar_words(word, bip39_words) for word in seed_received}


possible_seeds =product(*seeds_parecidas.values())




def ler_arquivo_em_lista(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = [linha.strip() for linha in arquivo]  # Remove \n de cada linha
        return linhas
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []

arquivo = "addr.txt"
array = ler_arquivo_em_lista(arquivo)
encontrada = 0
# Função para verificar uma seed
def check_seed(seed):

    seed_phrase = " ".join(seed)
    #if mnemo.check(seed_phrase):  # Verifica se a seed é válida
    address = get_first_segwit_address(seed_phrase)
    print(f"Seed encontrada: {seed_phrase}\n➡️ Endereço: {address}\n")
    if address in array:  # Verifica se o endereço está na lista
        print(f"✨ Seed encontrada: {seed_phrase}\n➡️ Endereço: {address}\n")
        encontrada = 1
        return seed_phrase, address
        
    return None

# Processar combinações com threads
valid_seeds = []
with ThreadPoolExecutor(max_workers=128) as executor:
    # Submeter cada seed para verificação em uma thread
    futures = [executor.submit(check_seed, seed) for seed in possible_seeds]
    
    # Processar os resultados conforme forem concluídos
    for future in as_completed(futures):
        result = future.result()
        if result:
            seed_phrase, address = result
            break  # Para o processo ao encontrar a primeira seed válida

print("Processamento concluído.")
