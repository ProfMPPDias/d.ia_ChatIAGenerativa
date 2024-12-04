# d.IA - IA Generativa

**d.IA** é uma IA generativa de texto construída com Python, Flask e a API do Ollama. A aplicação permite que os usuários interajam com um chatbot que gera respostas com base no texto enviado. A interface do chatbot é projetada com uma janela personalizável e arrastável em um tema moderno.

## 🚀 Funcionalidades

- **IA Generativa**: Utiliza a API do Ollama para gerar respostas em tempo real.
- **Janela de Chat Arrastável**: O usuário pode mover a janela de chat livremente pela tela.
- **Modo Escuro**: A interface é estilizada com o tema Dracula para um visual moderno e elegante.
- **Função de Copiar Mensagem**: O usuário pode copiar qualquer resposta da IA com um clique no botão.
- **Interação em Tempo Real**: Converse com a IA em tempo real, com respostas entregues quase instantaneamente.

## 🔧 Tecnologias Utilizadas

- **Python**: Para a lógica de backend e operações do servidor.
- **Flask**: Framework web leve para Python.
- **Ollama**: Fornece as respostas geradas pela IA.
- **HTML/CSS/JS**: Para a interface de usuário frontend.

## 🌐 Configuração e Instalação

### Pré-requisitos

Certifique-se de que você tem o seguinte instalado:

- Python 3.7+
- pip (gerenciador de pacotes do Python)
- Ollama (https://ollama.com/)

### Passo-a-Passo na Implementação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/d.IA.git
   cd d.IA
   ```
   
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicie o Servidor Flask

```bash
python main.py
```

4. Instale o Ollama, verifique qual sistema operacional irá usado (no servidor ou local);
   
5. Após instalação, faça o comando para instalar a rede neural Llama 3.2 em sua última versão, Llama 3.2:
   
```bash
ollama pull llama3.2
```

6. Finalmente, execute a rede neural do Llama 3.2:

```bash
ollama run llama3.2
```
7. Repare, que ao iniciar o Servidor Flask, você deverá fazer o passo á passo da Rede Neural do Llama em uma outra aba do CMD, PowerShell ou Terminal.

8. Caso esteja rodando em uma VPS, deverá utilizar o screen para gerenciar uma área de trabalho nova.

## 🛠️ Configuração da API

A aplicação utiliza rede neural baseada no Ollama para gerar as respostas de texto. Por padrão, o servidor deve estar rodando em http://0.0.0.0:11434/api/chat. 
Caso tenha a API do Ollama rodando em outro host ou porta, será necessário modificar a URL OLLAMA_URL no arquivo main.py.

## 💡 Como Usar

- Abra o aplicativo no seu navegador.
- Digite uma mensagem no campo de entrada e pressione "Enviar".
- O chatbot gerará uma resposta com base na sua mensagem.
- Você pode arrastar a janela de chat pela tela, clicando e segurando o cabeçalho.

## 🙏 Contribuindo

- Fique à vontade para fazer um fork deste repositório, enviar problemas e criar pull requests para contribuir.
