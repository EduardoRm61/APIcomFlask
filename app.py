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

class AtualizacaoTurma(Exception):
    def __init__(self, *msg):
        self.msg = msg
        super().__init__(*msg)

class ValorBoll(Exception):
    def __init__(self, *msg):
        self.msg = msg
        super().__init__(*msg)

#Funções Auxiliares:

def ListarTurma():
    return dadosTurma["Turma"]

def ListarProfessor():
    return dadosProfessor["Professor"]

def ListarAlunos():
    return dados["Alunos"]

def ProcurarTurmaPorId(Id_turma):
    for dict in dadosTurma["Turma"]:
        if dict["Id"] == Id_turma:
            return dict
    raise TurmaNaoIdentificada

def CriarNovaTurma(nv_dict):
    dadosTurma["Turma"].append(nv_dict)
    return

def CriarNovoProfessor(nv_dict):
    dadosProfessor["Professor"].append(nv_dict)
    return

def CriarNovoAluno(nv_dict):
    dados["Alunos"].append(nv_dict)
    return



if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)