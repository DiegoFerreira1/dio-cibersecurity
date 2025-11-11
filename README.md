# DIO - Santander - Cibersegurança
## Projeto de simulação de ataque com *Brute Force*

# Etapa 1:

## Passos Introdutórios

***
## `Passo 1: Criar máquinas virtuais`

O primeiro passo é instalar o **Oracle Virtual Box** para simular os sistemas *Kali Linux* e *Metaspotable 2*.
![alt text](/image/virtualbox.png)
***
## `Passo 2: Criar rede interna`

A seguir é necessário criar uma rede interna no Virtual box clicando em Arquivo - Ferramentas - Rede (N).
![alt text](/image/rede1.png)
***
## `Passo 3: Configurar nome e endereço da rede interna`

Ao abrir, vai em Redes NAT, depois Criar, escolhe o nome no canto inferior como *hacking lab*, por fim define o endereço IPv4 como exemplo: **192.168.1.0/25**.
![alt text](/image/rede2.png)
***
## `Passo 4: Definir a rede para ambos os sistemas`

Sob a imagem do sistema, clica com o botão direito do mouse em configurações, em seguida vai em rede e define ao adaptador 1:

1) Ligado a: *Rede NAT*
2) Nome: *hacking_lab*

![alt text](/image/rede3.png)
***
## `Passo 5: Acessar o Metaspotable 2`

Ao abrir o sistema de testes e carregar, será necessário informar o usuário e a senha de acesso.
- usuário: **msfadmin**
- senha: **msfadmin**

Para descobrir qual ip a máquina está rodando, digita o comando: 

*ip a*

Anota o IP fornecido como exemplo: *198.168.1.3*. Este IP é só um exemplo, normalmente o ip será o que foi definido na rede interna NAT.
***
## `Passo 6: Acessar o Kali Linux`

Ao abrir o sistema, será necessário informar usuário e senha padrão do linux ou se voce instalar do zero, informa seu usuário e sua senha. 

Abre o terminal e testa a conexão de rede utilizando o comando:

*ping -c 3 198.168.1.3* 

Se a conexão for estabelecida, isso retornará 3 pacotes do IP destino, Obs: o sistema do metaspotable deve estar aberto.

![alt text](/image/ping.png)

# Etapa 2:

## Enumeração

## `Passo 1: Utilizando o comando nmap`

O primeiro comando na enumeração utilizando a ferramente de varredura em redes *nmap*. O comando é usado para realizar um escaneamento de portas específico em um endereço IP alvo (192.168.1.3) usando a ferramenta *nmap*.

*nmap -sV -p 21,22,80,445,139 198.168.1.3*

* `nmap`: O nome da ferramenta de código aberto usada para exploração de rede e auditoria de segurança.

* `-sV`: Esta opção habilita a detecção de versão. O Nmap tentará determinar qual serviço está sendo executado nas portas abertas e a versão exata do software (por exemplo, "Apache httpd 2.4.41" em vez de apenas "http").

* `-p 21,22,80,445,139`: Esta opção especifica as portas que você deseja escanear. Em vez de escanear todas as 65535 portas, o Nmap verificará apenas as portas listadas:

    * `21`: Frequentemente usada para FTP (File Transfer Protocol).

    * `22`: Frequentemente usada para SSH (Secure Shell).

    * `80`: Frequentemente usada para HTTP (World Wide Web).

    * `445`: Frequentemente usada para SMB (Server Message Block) sobre TCP/IP.

    * `139`: Frequentemente usada para NetBIOS (sessão SMB).

    * `192.168.1.3`: O endereço IP do host alvo que será escaneado. 

![alt text](/image/portas.png)
***

## `Passo 2: Testando a porta FTP`

Para testar a porta *ftp*, utiliza o comando:

*ftp 198.168.1.3*

Isso retornará um pedido de login, caso aceito o sistema retorna boas vindas, caso falhe ele retorna um erro.

![alt text](/image/testftp.png)

# Etapa 3:

## Criando wordlists para nomes de usuário e senhas

## `Passo 1: Criando wordlist de usuários`
Para criar a lista de nomes de usuários comuns, utiliza o comando:

*echo -e “user\nmsfadmin\nadmin\nroot” > users.txt*

Cria uma lista *user\nmsfadmin\nadmin\nroot* e salva o arquivo com o nome *users.txt*
***

## `Passo 2: Criando wordlist de senhas`

Para criar a lista de senhas comuns, utiliza o comando:

*echo -e “123456\npassword\nqwerty\nmsfadmin” > pass.txt*

Cria uma lista *123456\npassword\nqwerty\nmsfadmin* e salva o arquivo com o nome *pass.txt*
***

## `Passo 3: Utilizando a ferramenta medusa`

**Medusa** é uma ferramenta de código aberto para realizar ataques de força bruta rápidos e paralelos contra diversos serviços de rede (como HTTP, FTP, SSH, etc.) para testar a robustez de senhas.

**Comando**:

*medusa -h 192.168.1.0 -U users.txt -P pass.txt -M ftp -t 6*

O comando medusa acima instrui a ferramenta Medusa a realizar um ataque de força bruta contra um serviço FTP, utilizando os seguintes parâmetros: 

* `-h 198.168.1.0`: Especifica o host alvo (endereço IP). Note que 198.168.1.0 é geralmente um endereço de rede (ou um endereço IP inválido para um host específico, dependendo da configuração da sub-rede) e pode ser necessário especificar um IP de host válido, como 198.168.1.1 ou similar, ou usar a opção -H para um arquivo com múltiplos hosts.

* `-U users.txt`: Define o arquivo (users.txt) que contém uma lista de nomes de usuário a serem testados durante o ataque.

* `-P pass.txt`: Define o arquivo (pass.txt) que contém uma lista de senhas a serem testadas para cada nome de usuário.

* `-M ftp`: Especifica o módulo (protocolo) a ser utilizado, neste caso, o FTP (*File Transfer Protocol*).

* `-t 6`: Define o número total de logins a serem testados concorrentemente (em paralelo), o que acelera o processo de ataque, mas pode sobrecarregar o servidor alvo ou a rede. 

![alt text](/image/medusa1.png)
***
# Etapa 4:

## Ataques de força bruta em formulários de login web

Os ataques de força bruta não se aplicam somente ao *ftp*, mas também sistemas web como um formulário. 
***
## `Passo 1: Acessando o DVWA via mozila no kali`
O link para acessar o formulário DVWA: 

*198.168.1.3/dvwa/login.php*

![alt text](/image/dvwa.png)

## `Passo 2: Verificando os códigos internos do formulário web`

Para entrar e inspecionar o código fonte do formulário, aperta o *f12* e sem seguida vai em network.

![alt text](/image/network.png)
***

## `Passo 3: Criando wordlists de usuário e senha`

* Usuários possíveis: *echo -e “user\nmsfadmin\nadmin\nroot” > users.txt*

* Senhas possíveis: *echo -e “123456\npassword\nqwerty\nmsadmin” > pass.txt*
***

## `Passo 4: Realizando o ataque com o medusa`

`medusa -h 198.168.1.3 -U users.txt -P pass.txt -M http \ 
-m PAGE: ‘/dvwa/login.php’ \
-m FORM: ‘username=^USER^&password=^PASS^&Login=Login’ \
-m FAIL=Login failed -t 6`

O comando fornecido utiliza a ferramenta de segurança cibernética Medusa para realizar um ataque de força bruta contra um formulário de login em um servidor web específico.

* `medusa`: Inicia a ferramenta Medusa, que é usada para testar senhas em vários serviços (FTP, SSH, HTTP, etc.).

* `-h 198.168.1.3`: Especifica o host ou endereço IP do servidor alvo (neste caso, 198.168.1.3).

* `-U users.txt`: Define o caminho para um arquivo (users.txt) que contém uma lista de nomes de usuário a serem testados.

* `-P pass.txt`: Define o caminho para um arquivo (pass.txt) que contém uma lista de senhas a serem testadas para cada usuário.

* `-M http`: Especifica o módulo ou protocolo a ser usado para o ataque, que é o HTTP (protocolo de formulários web).

* `-m PAGE:` ‘/dvwa/login.php’: Uma opção específica do módulo HTTP que define o caminho da página de login onde o formulário está localizado no servidor alvo.

* `-m FORM`: *‘username=^USER^&password=^PASS^&Login=Login’*: Define a estrutura do formulário de login, indicando os nomes dos campos (username, password, Login) e onde o Medusa deve inserir os valores da lista de usuários (^USER^) e da lista de senhas (^PASS^) durante as tentativas.

* `-m FAIL=Login failed`: Instrução para o Medusa, indicando o texto exato (Login failed) que aparece na página quando uma tentativa de login falha. Isso permite que a ferramenta saiba quando uma combinação de usuário/senha não funcionou.

* `-t 6`: Define o número de threads paralelas a serem executadas simultaneamente (6 threads), o que acelera o processo do ataque, mas pode sobrecarregar o servidor alvo. 

![alt text](/image/medusa2.png)

![alt text](/image/medusa3.png)

***
# Etapa 5:

## Ataques em cadeia, enumeração smb + password spraying

Envolve uma combinação de técnicas de reconhecimento e ataque para obter acesso a um ambiente de rede, especificamente visando o protocolo SMB. O processo ocorre em cadeia: a enumeração SMB fornece a base para o subsequente password spraying. 
***
## `Passo 1: Enumeração SMB (Server Message Block)`
A enumeração SMB é a fase de reconhecimento, onde o atacante coleta informações sobre o ambiente de rede usando o protocolo SMB, que é usado principalmente para compartilhamento de arquivos e impressoras no Windows. O objetivo é obter dados que serão úteis nas fases seguintes do ataque.

O SMB (Server Message Block) da Microsoft é um protocolo de rede essencial usado para compartilhar arquivos, impressoras e outros recursos entre computadores em uma rede local (LAN). É a base do compartilhamento de arquivos no ecossistema Windows.

### Resumo das funções e caracteristícas:

* `Acesso a Recursos Remotos`: Permite que um computador (cliente) acesse arquivos e pastas localizados em outro computador ou servidor (servidor) como se estivessem em sua própria máquina.

* `Modelo Cliente-Servidor`: Funciona em um modelo onde um dispositivo solicita acesso (cliente) e outro fornece (servidor).

* `Multiplataforma`: Embora seja nativo do Windows, é suportado por outros sistemas operacionais (como macOS e Linux via Samba).

* `Portas de Comunicação`: Utiliza principalmente a porta TCP 445 para comunicação.

* `Evolução e Segurança`: O protocolo evoluiu significativamente. As versões modernas (SMBv3 e posteriores) incluem recursos de segurança importantes como criptografia de ponta a ponta e assinatura de pacotes para proteger os dados contra interceptação e ataques, sendo as versões antigas (SMBv1) consideradas inseguras. 

Para sistemas Linux, a implementação do protocolo SMB é feita através do software livre chamado Samba.

O Samba é uma suíte de software que permite a interoperabilidade total entre sistemas operacionais Unix/Linux, Windows e macOS, fazendo com que o Linux funcione como um servidor de arquivos e impressão compatível com as redes Microsoft. 

### Técnicas e ferramentas

* `Listagem de Compartilhamentos`: O atacante tenta listar os compartilhamentos de rede disponíveis, o que pode revelar dados sensíveis ou configurações de segurança fracas (como acesso de convidado habilitado).

* `Enumeração de Usuários e Grupos`: Ferramentas podem ser usadas para extrair listas de nomes de usuários válidos, grupos e, às vezes, informações sobre a estrutura de domínio.

* `Identificação de Versão e Vulnerabilidades`: Determinar a versão do serviço SMB em execução pode revelar vulnerabilidades conhecidas que podem ser exploradas.

* `Ferramentas Comuns`: smbclient, enum4linux, nmap (com scripts SMB), Metasploit (módulos auxiliares), e CrackMapExec são ferramentas comuns usadas para essa finalidade.

## `Passo 2: Password Spraying (pulverização de senhas)`
O password spraying é um tipo de ataque de força bruta "lento e discreto" que visa contornar os mecanismos de bloqueio de conta. Em vez de tentar muitas senhas em uma única conta (o que levaria ao bloqueio), o atacante tenta um número limitado de senhas comuns (ex: "Password123", "Verao2024", "123456") em uma grande lista de nomes de usuários válidos (obtidos na etapa de enumeração). 

### O ciclo do ataque

1.	`Obter lista de usuários`: Usando os resultados da enumeração SMB ou outras fontes, como e-mail corporativo ou redes sociais.

2.	`Escolher senhas comuns`: Selecionar uma ou poucas senhas que são frequentemente usadas pelos usuários.

3.	`Executar o ataque`: Tentar as senhas em cada usuário, geralmente com atrasos aleatórios entre as tentativas para evitar detecção por sistemas de monitoramento.

4.	`Acesso`: Se uma senha for bem-sucedida para uma conta, o atacante obtém um ponto de apoio inicial na rede, o que pode levar a um movimento lateral e escalonamento de privilégios. 

### Ataques em cadeia
A combinação dessas técnicas é um exemplo clássico de um ataque em cadeia. Uma etapa alimenta a próxima: 
* A enumeração fornece a inteligência necessária (usuários válidos, serviços SMB expostos) para tornar o password spraying mais eficiente e direcionado.

* O sucesso do password spraying (obtenção de credenciais válidas) permite que o atacante se autentique em serviços SMB ou outros serviços de rede, facilitando o movimento lateral e a exploração adicional, continuando a cadeia de ataque.

### Mitigação

Para se defender contra esses ataques:

* Políticas de Senhas Fortes: Implementar políticas que exijam senhas complexas e longas para reduzir a eficácia do password spraying.

* Autenticação Multifator (MFA): Habilitar MFA em todos os serviços, o que torna as credenciais roubadas inúteis sem o segundo fator de autenticação.

* Monitoramento e Detecção: Monitorar proativamente os logs de autenticação para padrões incomuns ou picos de falhas de login.

* Restringir Enumeração: Configurar sistemas para limitar as informações que podem ser enumeradas por usuários não autenticados ou por convidados.

* Desativar Contas Inativas e Acesso de Convidado: Garantir que contas de convidado estejam desativadas por padrão e que contas de usuários inativos sejam removidas ou desabilitadas. 

`Passo 1`: Simular situação em que conseguiu acesso a uma rede interna por phishing, acesso físico ou vetor e descobriu que existe um servidor SMB ativo.

`Passo 2`: Descobrir se existe algum usuário ativo no sistema e testar senhas fracas em todos eles, de forma discreta e sem bloquear contas.

`Passo 3`: Testas senhas em diferentes usuários existentes usando o Password Spraying, evitando o problema de bloqueio após múltiplas requisições. O password Spraying é uma técnica furtiva de ataque a senhas, ou seja, ao invés de testar muitas senhas para um único usuário que leva ao bloqueio de tentativas, ele testa uma senha comum para muitos usuários diferentes.

Exemplo: testar 123456 para todos os usuários válidos.

`Passo 4`: Enumeração de usuário com o enum4linux:

	enum4linux -a 198.168.1.3 | tee enum4_output.txt

O comando acima é usado para realizar a enumeração de informações detalhadas de um sistema Windows ou Samba em uma rede. 

* `enum4linux`: É uma ferramenta de script projetada para extrair o máximo de informações possível de sistemas baseados em Windows e Samba. É comumente utilizada em testes de penetração e auditorias de segurança para identificar vulnerabilidades.

* `-a`: Esta flag significa "tudo" (all). Ela instrui a ferramenta a realizar todas as enumerações simples disponíveis, incluindo:

    * Nomes NetBIOS.

    * Configurações de servidor.

    * Listas de compartilhamentos (shares).

    * Listas de usuários e grupos.

    * Informações sobre senhas (se disponíveis).

* 198.168.1.3: Este é o endereço IP do sistema alvo que você está tentando enumerar.

* | tee enum4_output.txt: Este é um comando de redirecionamento do shell:

    * | (pipe) redireciona a saída padrão do comando enum4linux para o próximo comando (tee).

    * tee enum4_output.txt exibe a saída na tela (console) e, simultaneamente, a salva em um arquivo chamado enum4_output.txt. 

Após usar o comando e salvar, é possível ver o arquivo usando o comando:
less enum4_output.txt no terminal.

![alt text](/image/users.png)

## `Passo 3: Criando uma wordlist`

*Para usuários*

*echo -e “user\nmsfadmin\nservice” > smb_users.txt*

*Para senhas*

*echo -e “password\n123456\nWelcome123\nmsfadmin” > pass_spray.txt*
***

## `Passo 4: Realizando o ataque com o medusa`

Ao rodar o comando, é preciso verificar as saídas e observar o seguinte termo:  *ACCOUNT FOUND*

![alt text](/image/medusa4.png)
***

## `Passo 5: Testar o acesso`

Para realizar o teste de penetração, utiliza o comando smbclient:

*smbclient -L //198.168.1.3 -U msfadmin*

![alt text](/image/medusa5.png)
***

## `Passo 6: Como se proteger?`

Para finalizar essas etapas, aqui está uma lista de como se proteger contra ataques cibernéticos.

1. utenticação de múltiplos fatores;

2.	Senhas forte e expiradas regularmente; 

3.	Bloqueio de IP’s após múltiplas tentativas de login;

4.	Monitoramento inteligente de LOG’s e comportamento usando IA;

5.	Segmentação da rede (Serviços internos não devem ser expostos);

6.	Auditorias regulares com as ferramentas do kali (medusa por exemplo);

7.	Desativar serviços não utilizados.


# Recursos Úteis

* [Criando um Ataque Brute Force de senhas com Medusa e Kali Linux](https://hermes.dio.me/files/assets/2dd3d3ad-b7e5-4325-8d1d-ddd8e7205fea.pdf)

# Documentações Oficiais

* [Kali Linux](https://www.kali.org/docs/)

* [DVWA](https://www.100security.com.br/dvwa)

* [Medusa](http://foofus.net/goons/jmk/medusa/medusa.html)

* [Nmap](https://nmap.org/book/)