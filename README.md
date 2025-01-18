
![ObisdianLogo](https://obsidian.md/favicon.ico)

# Привет, Обсидиан!

# VaultGuard
**VaultGuard** é uma solução gratuita para fazer backup diário do seu [**Obsidian Vault**](https://forum.obsidian.md/t/what-exactly-is-a-vault/4369). Usando **Git** e **Python**, o script verifica alterações e realiza commits automáticos para o GitHub, **criando um histórico de** backups. Ideal para quem quer proteger suas notas de forma **simples** e **sem custos** adicionais.

## Requisitos
- [**Git**](https://git-scm.com/downloads) 2.48.1 ou superior.
- [**Python**](https://www.python.org/downloads/) 3.13.1 ou superior.
- App de Automação nativo do sistema:
  - Windows: [**Agendador de Tarefas**](http://cursos.basesoft.com.br/Reinf/Agendadar_Tarefas.pdf). ``Win+R > taskschd.msc``
  - MacOS: [**Automator**](https://support.apple.com/pt-br/guide/automator/welcome/mac). ``Cmd+Space > Automator``

## Por quê?
Que o app é uma maravilha todos sabemos, contudo para ter um backup dos seus dados pessoais é necessário **pagar uma assinatura** para desfrutar dessa vantagem.

Pensando em alguns colegas LATAM e Russos e que não podem pagar essa assinatura no momento e precisam trabalhar com a ferramenta, decidi desenvolver este projeto.

## Como funciona?
Todo e qualquer arquivo criado dentro do Obsidian fica armazenado dentro de um **Obsidian Vault**, que na prática é nada mais que uma pasta dedicada em: ``"C:\Users\seu_usuario_windows\Documents"`` ou ``"~/Users/seu_usuario_mac/Documents"`` com o mesmo nome.

Sabendo disso, este código verifica todos os arquivos e subpastas dentro do seu **Obsidian Vault** e, caso encontre alguma alteração, faz o commit e push para o seu repositório de backup no GitHub contendo a mensagem ``Daily backup: 00/00/0000 00:00:00`` com a data e hora do backup para que possa haver um histórico. 

# Como configurar?

## Repositório
O primeiro passo é ter uma conta cadastrada no [**GitHub**](https://github.com/), em seguida crie um repositório com o nome que desejar como por Ex: **ObsidianBackup** e por segurança, certifique-se de [**criar um repositório privado**](https://docs.github.com/pt/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility). 

Existem **duas formas** de configurar, sendo:
1. Clonar o repositório criado no **GitHub** dentro da sua pasta **Documents** ``cd "C:\Users\seu_usuario_windows\Documents"`` ou ``cd "~/Users/seu_usuario_mac/Documents"``. Execute o comando 👇

```
git clone https://github.com/seu_usuario_git/nome_do_seu_repositorio.git
```

2. Ou acessar o seu **Obsidian Vault** via terminal com ``cd "C:\Users\seu_usuario_windows\Documents\ObsidianVault"`` para Windows ou para MacOS ``cd "~/Users/seu_usuario_mac/Documents/ObsidianVault"`` e iniciar um repositório **git** direto. Execute o comando 👇

```
git init
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/seu_usuario_git/nome_do_seu_repositorio.git
git push -u origin main
```

## Código Python
Agora copie o código do script **Python** deste repositório e salve em algum lugar da sua máquina. Você pode fazer isso via terminal usando ``cd documents`` para ir até a pasta de documentos e ``echo "cole_o_script_aqui" > VaultGuard.py`` para criar o arquivo Python do script.

💡 Obs: Eu recomendo criar uma pasta chamada **Automações** dentro de documents e deixar o script lá.

## Movendo seu Vault para a pasta Backup
Por ultimo, basta mover o seu **Obsidian Vault** para dentro da pasta do seu repositório e pronto! 
Agora é só modificar algum em algum documento deste Vault para teste e clicar duas vezes no executável do script **Python** para ele fazer o primeiro backup.

## Como automatizar
Para que funcione de forma adequada e automática, deve-se utilizar o **software de automação padrão do sistema**. Basta programar uma **regra** para **executar esse script python diariamente** as 23:59:59.

Dessa forma, fica garantido um backup diário de todos o seu workflow **sem pagar nada** e de forma completamente segura e, a partir de qualquer dispositivo com acesso a internet, você tem total controle de acessar a sua conta github, baixar o arquivo .zip do repositório ou dar um ``git clone seu_repositorio.git`` e **continuar de onde parou**.

## Dicas
Agora você está seguro! Basta deixar que a mágica aconteça automaticamente todos os dias ou caso queira fazer um backup imediato, é só executar manualmente o script **Python** referente ao backup e pronto!

# Большое спасибо!
