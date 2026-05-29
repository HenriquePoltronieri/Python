# Cartilha GitHub pelo terminal do VS Code no Windows

## 1. Abrir o projeto no VS Code

Abra o VS Code e clique em:

```
File > Open Folder
```

Escolha a pasta do projeto.

Depois abra o terminal:

```
Terminal > New Terminal
```

Atalho no Windows:

```
Ctrl + '
```

---

## 2. Configurar nome e e-mail no Git

Esse passo identifica quem está fazendo os commits.

```bash
git config --global user.name "Seu Nome"
```

```bash
git config --global user.email "seuemail@gmail.com"
```

Exemplo:

```bash
git config --global user.name "João Silva"
git config --global user.email "joao@email.com"
```

Para conferir se deu certo:

```bash
git config --global --list
```

Observação:

O `user.name` não precisa ser igual ao usuário do GitHub.

Exemplo:

```bash
git config --global user.name "João Silva"
```

O link do GitHub pode ser:

```
https://github.com/jsilva123/meu-projeto.git
```

Nesse caso:

```
João Silva = nome que aparece nos commits
jsilva123 = usuário da conta no GitHub
```

---

# Parte 1: Enviar um projeto novo para o GitHub

Use esse caminho quando o projeto já está no computador, mas ainda não está no GitHub.

## 1. Iniciar o Git na pasta do projeto

```bash
git init
```

Esse comando transforma a pasta do projeto em um repositório Git.

---

## 2. Verificar os arquivos

```bash
git status
```

Esse comando mostra os arquivos criados ou alterados.

---

## 3. Adicionar os arquivos

```bash
git add .
```

O ponto `.` significa que todos os arquivos da pasta serão adicionados.

---

## 4. Criar o commit

```bash
git commit -m "Primeiro commit"
```

O commit é como um salvamento do projeto.

---

## 5. Criar o repositório no GitHub

No navegador, entre no GitHub.

Clique em:

```
New repository
```

Preencha o nome do repositório.

Escolha se será:

```
Public
```

ou

```
Private
```

Depois clique em:

```
Create repository
```

---

## 6. Copiar o link HTTPS do repositório

Depois de criar o repositório, copie o link HTTPS.

Ele será parecido com:

```
https://github.com/seu-usuario/nome-do-projeto.git
```

Importante:

O `seu-usuario` é o nome de usuário da conta no GitHub.

Exemplo:

```
https://github.com/jsilva123/meu-projeto.git
```

---

## 7. Conectar o projeto local ao GitHub

No terminal, digite:

```bash
git remote add origin https://github.com/seu-usuario/nome-do-projeto.git
```

Exemplo:

```bash
git remote add origin https://github.com/jsilva123/meu-projeto.git
```

---

## 8. Definir a branch principal

```bash
git branch -M main
```

---

## 9. Enviar para o GitHub

```bash
git push -u origin main
```

Na primeira vez, pode abrir uma janela pedindo login no GitHub.

Faça login com sua conta.

---

# Depois que já enviou uma vez

Sempre que fizer alterações no projeto, use:

```bash
git status
git add .
git commit -m "Atualiza projeto"
git push
```

---

# Parte 2: Clonar um projeto do GitHub

Use esse caminho quando o projeto já existe no GitHub e você quer baixar para o computador.

## 1. Copiar o link do repositório

No GitHub, entre no repositório.

Clique em:

```
Code
```

Depois copie o link HTTPS.

Exemplo:

```
https://github.com/seu-usuario/nome-do-projeto.git
```

---

## 2. Escolher onde salvar o projeto

No terminal, entre na pasta onde quer salvar o projeto.

Exemplo:

```bash
cd Documents
```

Ou, dependendo do computador:

```bash
cd Documentos
```

Para ver as pastas disponíveis:

```bash
dir
```

---

## 3. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-projeto.git
```

Exemplo:

```bash
git clone https://github.com/jsilva123/meu-projeto.git
```

---

## 4. Entrar na pasta do projeto

```bash
cd nome-do-projeto
```

Exemplo:

```bash
cd meu-projeto
```

---

## 5. Abrir no VS Code

```bash
code .
```

---

# Baixar atualizações do GitHub

Quando o projeto já está no computador e você quer buscar atualizações do GitHub:

```bash
git pull
```

Esse comando baixa as alterações mais recentes do repositório online.

---

# Comandos principais

| Comando | Para que serve |
| --- | --- |
| `git config --global user.name "Seu Nome"`                | Configura o nome do autor |
| `git config --global user.email "seuemail@gmail.com"`     | Configura o e-mail do autor |
| `git config --global --list`                              | Confere as configurações |
| `git init`                                                | Inicia o Git no projeto |
| `git status`                                              | Mostra alterações |
| `git add .`                                               | Adiciona todos os arquivos |
| `git commit -m "mensagem"`                                | Salva uma versão |
| `git remote add origin link`                              | Conecta o projeto ao GitHub |
| `git branch -M main`                                      | Define a branch principal |
| `git push -u origin main`                                 | Envia pela primeira vez |
| `git push`                                                | Envia alterações |
| `git clone link`                                          | Baixa um projeto |
| `git pull`                                                | Baixa atualizações |
| `dir`                                                     | Lista arquivos e pastas no Windows |
| `cd nome-da-pasta`                                        | Entra em uma pasta |
| `code .`                                                  | Abre a pasta atual no VS Code |

---

# Resumo rápido

## Enviar projeto novo

```bash
git init
git status
git add .
git commit -m "Primeiro commit"
git remote add origin https://github.com/seu-usuario/nome-do-projeto.git
git branch -M main
git push -u origin main
```

## Enviar alterações depois

```bash
git status
git add .
git commit -m "Atualiza projeto"
git push
```

## Clonar projeto

```bash
git clone https://github.com/seu-usuario/nome-do-projeto.git
cd nome-do-projeto
code .
```

## Configurar nome e e-mail no Git

Esse passo identifica quem está fazendo os commits.

```bash
git config --global user.name "HenriquePoltronieri"
git config --global user.email "henrique.poltronieri2008@gmail.com"
```

Para conferir se deu certo:

```bash
git config --global --list
```