# SeedMistake - Reparador de Seeds 🔑✨


## O que é? 🤔
O **SeedMistake** é uma ferramenta para recuperar seeds de carteiras de criptomoedas digitadas ou anotadas com erros. Usa a distância de Levenshtein para corrigir palavras e verifica endereços com fundos. Especialmente útil em casos aonde a seed tem erros de digitação, rasuras, ou erros de escrita.

---

## Funcionalidades 🚀
- 🔍 Corrige palavras erradas em seeds  
- 🏠 Gera endereços públicos a partir das seeds corrigidas  
- 💰 Verifica se os endereços têm saldo (via arquivo TXT)  
- 🔒 Processamento local, sem envio de dados  

---

## Como funciona? 🛠️
1. Insira a seed com erros  
2. Corrige palavras com base na lista BIP-39  
3. Gera o endereço público  
4. Compara com a lista de endereços com fundos  
5. Retorna seeds válidas  

---

## Exemplo 📝
- **Entrada**: "aplle banan chery dogg"  
- **Correção**: "apple banana cherry dog"  
- **Endereço**: `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa`  
- **Resultado**: "Seed válida com fundos" (se estiver na lista)  

---

## Detalhes Técnicos 💻
- **Linguagem**: Python 3.8+  
- **Bibliotecas**: `python-Levenshtein`, `bip32utils`, `web3.py`  
- **Algoritmo**: Distância de Levenshtein  
- **Arquivo TXT**: Endereços com fundos (atualizado diariamente)  

---



Bruno da Silva
Pesquisador de segurança da Informaçao
2025
