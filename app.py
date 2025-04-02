from flask import Flask, request
app = Flask(__name__)
dados = {"Alunos":[
        {"Id": 8,
        "Nome": "Getúlio",
        "Idade": 77,
        "Turma Id":22,
        "Data_Nascimento": "19/04/1882",
        "Nota_primeiro_semestre": 8.0,
        "Nota_segundo_semestre": 9.5,
        "Média_final": 8.75},

        {"Id": 8,
        "Nome": "JUcelino Kubicast",
        "Idade": 73,
        "Turma Id":22,
        "Data_Nascimento": "12/09/1902",
        "Nota_primeiro_semestre": 8.0,
        "Nota_segundo_semestre": 9.5,
        "Média_final": 8.75}
        
]}

dadosProfessor = {"Professor":[
    {"Id": 12, "Nome": "Caio", "Idade": 26, "Matéria": "Eng. de Requisitos", "Observações": "Conversa com chat"},
    {"Id": 15, "Nome": "Furlan"}
]}

dadosTurma = {"Turma":[
        {"Id":12,"Descrição": "Eng. de Requisitos", "Professor Id": 22},
        {"ID": 10,"Descrição": "Ambientes Aperacionais", "Professor Id": 24}
]}

# Aqui estarão as classes de exceção:

class TurmaNaoIdentificada(Exception):
    def __init__(self, msg="Erro, Turma não iden"):
        self.msg = msg
        super().__init__(self.msg)

class ProfessorNaoIdentificado(Exception):
    def __init__(self, msg = "Erro, Professor não cadastrado ou inexistente"):
        self.msg = msg
        super().__init__(self.msg)

class TurmaExistente(Exception):
    def __init__(self, *msg):
        self.msg = msg
        super().__init__(*msg)

class CadastroDeTurmaFalhado(Exception):
     def __init__(self, *msg):
        self.msg = msg
        super().__init__(*msg)
        

if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)