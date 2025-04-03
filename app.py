from flask import Flask, request
app = Flask(__name__)

# Aqui estão todos os dicionários: 

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
    {"Id": 12, "Nome": "Caio", "Idade": 26, "Matéria": "Eng. de Requisitos", "Observação": "Conversa com chat"},
    {"Id": 15, "Nome": "Furlan", "Idade": 32, "Matéria": "Banco de Dados", "Observação": None}
]}

dadosTurma = {"Turma":[
        {"Id":12,"Descrição": "Eng. de Requisitos","Ativa": True, "Professor Id": 22},
        {"Id": 10,"Descrição": "Ambientes Aperacionais", "Ativa": False, "Professor Id": 24}
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
    def __init__(self, msg= "Erro, Turma inexistente"):
        self.msg = msg
        super().__init__(*msg)

class CadastroDeTurmaFalhado(Exception):
    def __init__(self, msg = "Erro, cadastro de turma falhado, verifique os capos preenchidos"):
        self.msg = msg
        super().__init__(*msg)

class AtualizacaoTurma(Exception):
    def __init__(self, msg = "Erro, não foi possível atualizar os dados de turma, reveja todos os campos digitados"):
        self.msg = msg
        super().__init__(*msg)

class ValorBoll(Exception):
    def __init__(self, msg = "Erro, digite um valor Boll correto: True ou False"):
        self.msg = msg
        super().__init__(*msg)

class AlunoNaoIdentificado(Exception):
    def __init__(self, msg = "Erro, aluno mão identificado ou inexistente"):
        self.msg = msg
        super().__init__(*msg)

#Funções Auxiliares:

def ListarTurma():
    return dadosTurma["Turma"]

def ListarProfessor():
    return dadosProfessor["Professor"]

def ListarAlunos():
    return dados["Alunos"]

def ProcurarTurmaPorId(Id_Turma):
    for dict in dadosTurma["Turma"]:
        if dict["Id"] == Id_Turma:
            return dict
    raise TurmaNaoIdentificada()

def ProcurarProfessorPorId(Id_Pro):
    for dict in dadosProfessor["Professor"]:
        if dict["Id"] == Id_Pro:
            return dict
    raise ProfessorNaoIdentificado()

def ProcurarAlunoPorId(Id_Aluno):
    for dict in dados["Alunos"]:
        if dict["Id"] == Id_Aluno:
            return dict
    raise AlunoNaoIdentificado()

def CriarNovaTurma(nv_dict):
    dadosTurma["Turma"].append(nv_dict)
    return

def CriarNovoProfessor(nv_dict):
    dadosProfessor["Professor"].append(nv_dict)
    return

def CriarNovoAluno(nv_dict):
    dados["Alunos"].append(nv_dict)
    return

def DeletarTurma(Id_turma):
    turmas = dadosTurma["Turma"]

    for indice, turma in enumerate(turmas):
        if turma["Id"] == Id_turma:
            turmas.pop(indice)
            return {"Resultado": "Turma deleta com êxito!"}
    raise TurmaNaoIdentificada()
    
def DeletarProfessor(Id_pro):
    professores = dadosProfessor

    for indice, professor in enumerate(professores):
        if professor["Id"] == Id_pro:
            professores.pop(indice)
            return {"Resultado": "Professor deletado com êxito"}
    raise ProfessorNaoIdentificado()

def DeletarAluno(Id_Aluno):
    alunos = dados

    for indice, aluno in enumerate(alunos):
        if aluno["Id"] == Id_Aluno:
            alunos.pop(indice)
            return {"Resultado": "Aluno deletado com êxito"}
    raise AlunoNaoIdentificado

def ResetarAlunos():
    dados["Alunos"] = []
    return {"Resultado": "Lista de Alunos resetada!"}

def ResetarTurma():
    dadosTurma["Turma"] = []
    return {"Resultado": "Lista de Turma resetada!"}

def ResetarProfessor():
    dadosProfessor["Professor"] = []
    return {"Resultado":"Lista de Professor resetada!"}

def TurmaExiste(Id_turma):
    for turma in dadosTurma["Turma"]:
        if turma["Id"] == Id_turma:
            return True
    return False

def ProfessorExiste(Id_pro):
    for professor in dadosProfessor["Professor"]:
        if professor["Id"] == Id_pro:
            return True
    return False

def AlunoExiste(Id_aluno):
    for aluno in dados["Alunos"]:
        if aluno["Id"] == Id_aluno:
            return True
    return False

def ValorBuleano(ValorBooll):
    if ValorBooll is False or ValorBooll is True:
        return True
    return False



def AlterarTurma(Id_turma, Descricao, Ativa, Id_pro ):
    nv_dict = dadosTurma["Turma"]
    try:
        for turma in nv_dict["Turma"]:
            if turma["Id"] == Id_turma:

                if not TurmaExiste(Id_turma):
                    return ({
                        "Erro": "Requisição inválida",
                        "Descrição": "Id de Turma inexistente"
                    }), 400
                
                if not ValorBoll(Ativa):
                    return ({
                        "Erro": "Requisição inválida",
                        "Descrição": "Valor de ativa incorreto. Digite True ou False"
                    }), 400 
                
                nv_dict["Descrição"] = Descricao
                nv_dict["Ativa"] = Ativa
                nv_dict["Professor Id"] = Id_pro

                return {"Detalhes": "Turma alterada com sucessor"}, 200
        
        return ({
            "Erro": "Requisição inválida",
            "Descrição": "Id da Turma inexistente ou incorreto"
        }), 400
    
    except Exception as e:
        return ({
            "Erro": "Não foi possível fazer a requsição",
            "Decrição": str(e)
        }),500 

def AlterarProfessor(Id_pro, Materia, Obs):
    nv_dict = dadosProfessor

    for professor in nv_dict["Turma"]:
        if nv_dict["Id"] == Id_pro:
            if not ProfessorExiste(Id_pro):
                return ({
                    "Erro": "Requisição inválida",
                    "Descrição": "Professor inexistente"
                }), 400
            nv_dict["Matéria"] = Materia
            nv_dict["Observação"] = Obs
    return ({
        "Erro": "Requisição inválida",
        "Descrição":"Id do professor não encontrado"
    })




if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)