# 🤖 Bot - Automatizador de Reservas IFPI

Esse repositório apresenta um bot em Python desenvolvido para automatizar o processo de reserva de refeições no sistema SUAP do Instituto Federal do Piauí (IFPI). Ele foi criado para ser rápido, silencioso e eficiente.

## 🚀 Funcionalidades

- **Busca Inteligente:** Varre o sistema em busca de refeições para o dia atual e o dia seguinte.
- **Filtro Preciso:** Identifica cartões de "JANTAR" com base na data exata da refeição.
- **Modo Invisível (Headless):** Roda em segundo plano sem abrir janelas do navegador.
- **Injeção de URL:** Captura o ID da reserva e executa o comando diretamente via URL.

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Selenium WebDriver](https://www.selenium.dev/)
- [Python-Dotenv](https://pypi.org/project/python-dotenv/)
- [PyInstaller](https://pyinstaller.org/)

## 🚀 Como fazer funcionar no seu VS Code

Siga esses passos simples para rodar o bot no seu computador:

### 1. Preparar a pasta do projeto
Abra o seu VS Code, vá em **Arquivo > Abrir Pasta** e escolha a pasta onde você baixou este projeto.

### 2. Instalar o necessário
Abra o terminal do VS Code (aperte `Ctrl + '` ou vá em **Terminal > Novo Terminal**) e cole o comando abaixo para instalar as bibliotecas:
```bash
pip install selenium python-dotenv
```
### 3. Configurar sua Matrícula e Senha
Crie um arquivo chamado exatamente .env na raiz da pasta e coloque seus dados assim:

```bash
SUAP_MATRICULA=sua_matricula_aqui
SUAP_SENHA=sua_senha_aqui
```
⚠️ O arquivo .env é secreto! Nunca compartilhe ele com ninguém.

### 4. Rodar o Bot
Para testar, basta apertar o botão de Play do Python no canto superior direito do VS Code ou digitar no terminal:

```bash
python bot.py
```

### 5. Criando o arquivo .exe (Para sua amiga)
Se você quiser mandar o programa pronto para alguém que não tem o VS Code instalado:

Instale o criador de executáveis:

```bash
pip install pyinstaller
```
Gere o arquivo único e invisível:

```bash
python -m PyInstaller --onefile --noconsole bot.py
```
O programa pronto estará na pasta dist. Para funcionar no PC dela, envie o .exe junto com o arquivo .env.

### 6.Segurança e Privacidade
Este projeto foi desenvolvido para fins de estudo de automação. Seus dados de login ficam salvos apenas localmente no seu arquivo .env, o qual é ignorado pelo Git para sua segurança.

Desenvolvido por Antonio Marcos 🚀
