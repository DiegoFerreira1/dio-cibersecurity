# Documentação do arquivo descripto.py

Abaixo estão os métodos principais utilizados no script de descriptografia (descripto.py), com explicações sobre sua funcionalidade, parâmetros e uso.

## `1. Função carregar chave`
Carrega a chave de criptografia necessária para a descriptografia dos arquivos.

```python
def carregar_chave():
    return open("chave.key", "rb").read()
```
### O que o módulo os faz?
Abre o arquivo chave.key em modo de leitura binária ("rb"), lê seu conteúdo e o retorna. Este arquivo contém a chave gerada anteriormente pelo script de "ransomware".

## `2. Função descriptografar arquivo`
Descriptografa o conteúdo de um arquivo específico usando a chave fornecida.

```python
def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_descriptografados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)
```
### O que o módulo os faz?
Utiliza a biblioteca cryptography.fernet para descriptografar os dados. Primeiramente, lê o conteúdo criptografado do arquivo. Em seguida, descriptografa esses dados e sobrescreve o arquivo original com o conteúdo restaurado.

## `3. Função encontrar arquivos`
Percorre um diretório específico e coleta uma lista de todos os arquivos que precisam ser descriptografados.

```python
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista
```
### O que o módulo os faz?
Utiliza os.walk para caminhar recursivamente por todas as pastas a partir do diretorio especificado. Adiciona o caminho completo de cada arquivo a uma lista, exceto o próprio script do "ransomware" (ransoware.py) e o arquivo da chave (.key).

## `4. Função main`
Função principal que orquestra o processo de descriptografia.

```python
if __name__ == "__main__":
    main()
```
### O que o módulo os faz?
Define o fluxo principal do programa: (1) Carrega a chave, (2) Encontra todos os arquivos elegíveis em um diretório de teste (test_files), e (3) Itera sobre a lista, chamando a função descriptografar_arquivo para cada item.