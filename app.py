from flask import Flask, request
app = Flask(__name__)
dados = {
    "alunos": [
        {"nome": "Eduardo", "id": 12},
        {"nome": "Gil", "id": 42},
        {"nome": "Tony", "id": 40},
    ],
    "Professor": [
        {"nome": "Frederico", "id": 12},  # Adicionei uma vírgula aqui
        {"nome": "Sheila", "id": 40}
    ]
}

dadosProfessor = {"Professor":[
    {"Id": 12, "Nome": "Caio"},
    {"Id": 15, "Nome": "Furlan"}
]}









if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)