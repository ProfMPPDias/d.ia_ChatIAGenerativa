import json
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# URL da API do Ollama
OLLAMA_URL = "http://0.0.0.0:11434/api/chat"
model = "llama3.2"

# Função para comunicação com a API do Ollama
def chat(messages):
    r = requests.post(
        OLLAMA_URL,
        json={"model": model, "messages": messages, "stream": True},
        stream=True
    )
    r.raise_for_status()
    output = ""

    for line in r.iter_lines():
        body = json.loads(line)
        if "error" in body:
            raise Exception(body["error"])
        if body.get("done") is False:
            message = body.get("message", "")
            content = message.get("content", "")
            output += content

        if body.get("done", False):
            message["content"] = output
            return message

# Rota inicial que exibe o frontend
@app.route("/")
def home():
    return render_template("index.html")

# Rota para enviar mensagens e obter respostas
@app.route("/chat", methods=["POST"])
def chat_route():
    user_input = request.form.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    messages = [{"role": "user", "content": user_input}]
    message = chat(messages)
    return jsonify({"response": message["content"]})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)