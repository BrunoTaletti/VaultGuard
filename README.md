
![ObisdianLogo](https://obsidian.md/favicon.ico)

# **Привет, Обсидиан!**

# Sobre o Projeto
**VaultGuard** é uma solução gratuita para fazer backup diário do seu [**Obsidian Vault**](https://forum.obsidian.md/t/what-exactly-is-a-vault/4369). Usando **Git** e **Python**, o script verifica alterações e realiza commits automáticos para o GitHub, **criando um histórico de** backups. Ideal para quem quer proteger suas notas de forma **simples** e **sem custos** adicionais.

## **Requisitos**
- [**Git**](https://git-scm.com/downloads) 2.48.1 ou superior.
- [**Python**](https://www.python.org/downloads/) 3.13.1 ou superior.
- App de Automação nativo do sistema:
  - Windows: [**Agendador de Tarefas**](http://cursos.basesoft.com.br/Reinf/Agendadar_Tarefas.pdf). ``Win+R > taskschd.msc``
  - MacOS: [**Automator**](https://support.apple.com/pt-br/guide/automator/welcome/mac). ``Cmd+Space > Automator``

## **Por quê?**
Embora o Obsidian seja uma ferramenta incrível, fazer backups dos dados pessoais exige uma assinatura paga. Pensando nas dificuldades de alguns usuários da LATAM e Rússia que não podem arcar com esse custo, decidi criar uma solução gratuita para permitir que todos possam proteger suas notas com facilidade e segurança.

## **Como funciona?**
O Obsidian Vault é uma pasta que armazena todos os seus arquivos. O script verifica alterações nos arquivos e, quando detecta mudanças, realiza um commit e push para o seu repositório GitHub, criando um histórico com a data e hora de cada backup.

# Como configurar?

## **Repositório**
Crie uma conta no [**GitHub**](https://github.com/) e um repositório privado para garantir a segurança dos seus dados. Você pode criar o repositório com o nome que preferir, como por exemplo: **VaultBackup**.

Existem **duas formas** de configurar, sendo:
1. Clonar o repositório GitHub na pasta **Documents**:

```
git clone https://github.com/seu_usuario_git/nome_do_seu_repositorio.git
```

2. Ou no seu **Obsidian Vault**, inicie um repositório **git**:

```
git init
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/seu_usuario_git/nome_do_seu_repositorio.git
git push -u origin main
```

## **Código Python**
Baixe o script Python deste repositório e salve-o em sua máquina. Uma sugestão é criar uma pasta chamada **Automações** dentro de **Documents** para armazená-lo de forma organizada.

## **Movendo o Vault**
Mova seu **Obsidian Vault** para a pasta do repositório. Modifique um arquivo do Vault e execute o script Python para realizar o primeiro backup.

## **Como automatizar**
Para automatizar o processo, utilize o **software de automação padrão do sistema**. Programe uma **tarefa** para **rodar o script diariamente** as 00:00:00 ou no horário que preferir.

Com isso, você garante backups diários do seu workflow **sem custos** e de forma totalmente segura. A partir de qualquer dispositivo com acesso à internet, você pode acessar sua conta GitHub, baixar o arquivo .zip do repositório ou clona-lo para **continuar de onde parou**.

## **Dicas**
Agora você está protegido! O backup será feito automaticamente todos os dias. Se precisar de um backup imediato, basta rodar o script manualmente.

# **Большое спасибо!**
