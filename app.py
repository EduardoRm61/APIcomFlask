from flask import Flask, request, jsonify
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

        {"Id": 9,
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
        {"Id":11,"Descrição": "Eng. de Requisitos","Ativa": True, "Professor Id": 12},
        {"Id": 10,"Descrição": "Ambientes Aperacionais", "Ativa": False, "Professor Id": 15}
]}

# Aqui estarão as classes de exceção:

class TurmaNaoIdentificada(Exception):
    def __init__(self, msg="Erro, Turma não identificada"):
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

def listarTurma():
    return dadosTurma["Turma"]

def listarProfessor():
    return dadosProfessor["Professor"]

def listarAlunos():
    return dados["Alunos"]

def procurarTurmaPorId(Id_Turma):
    for dict in dadosTurma["Turma"]:
        if dict["Id"] == Id_Turma:
            return dict
    raise TurmaNaoIdentificada()

def procurarProfessorPorId(Id_Pro):
    for dict in dadosProfessor["Professor"]:
        if dict["Id"] == Id_Pro:
            return dict
    raise ProfessorNaoIdentificado()

def procurarAlunoPorId(Id_Aluno):
    for dict in dados["Alunos"]:
        if dict["Id"] == Id_Aluno:
            return dict
    raise AlunoNaoIdentificado()

def criarNovaTurma(nv_dict):
    dadosTurma["Turma"].append(nv_dict)
    return

def criarNovoProfessor(nv_dict):
    dadosProfessor["Professor"].append(nv_dict)
    return

def criarNovoAluno(nv_dict):
    dados["Alunos"].append(nv_dict)
    return

def deletarTurma(Id_turma):
    turmas = dadosTurma["Turma"]

    for indice, turma in enumerate(turmas):
        if turma["Id"] == Id_turma:
            turma_deltada = turma["Id"]
            turmas.pop(indice)
            return turma_deltada,200
    raise TurmaNaoIdentificada()
    
def deletarProfessor(Id_pro):
    professores = dadosProfessor["Professor"]

    for indice, professor in enumerate(professores):
        if professor["Id"] == Id_pro:
            dict_deletado = professor
            professores.pop(indice)
            return dict_deletado,200
    raise ProfessorNaoIdentificado()

def deletarAluno(Id_Aluno):
    alunos = dados

    for indice, aluno in enumerate(alunos):
        if aluno["Id"] == Id_Aluno:
            alunos.pop(indice)
            return {"Resultado": "Aluno deletado com êxito"},200
    raise AlunoNaoIdentificado

def resetarAlunos():
    dados["Alunos"] = []
    return {"Resultado": "Lista de Alunos resetada!"},200

def resetarTurma():
    dadosTurma["Turma"] = []
    return {"Resultado": "Lista de Turma resetada!"},200

def resetarProfessor():
    dadosProfessor["Professor"] = []
    return {"Resultado":"Lista de Professor resetada!"},200

def turmaExiste(Id_turma):
    for turma in dadosTurma["Turma"]:
        if turma["Id"] == Id_turma:
            return True
    return False

def professorExiste(Id_pro):
    for professor in dadosProfessor["Professor"]:
        if professor["Id"] == Id_pro:
            return True
    return False

def alunoExiste(Id_aluno):
    for aluno in dados["Alunos"]:
        if aluno["Id"] == Id_aluno:
            return True
    return False

def valorBuleano(ValorBooll):
    if ValorBooll is False or ValorBooll is True:
        return True
    return False

def alterarTurma(Id_turma, Descricao, Ativa, Id_pro ):
    nv_dict = dadosTurma["Turma"]
    try:
        for turma in nv_dict["Turma"]:
            if turma["Id"] == Id_turma:

                if not turmaExiste(Id_turma):
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

def alterarProfessor(Id_pro, Materia, Obs):
    nv_dict = dadosProfessor

    for professor in nv_dict["Turma"]:
        if professor["Id"] == Id_pro:
            if not professorExiste(Id_pro):
                return ({
                    "Erro": "Requisição inválida",
                    "Descrição": "Professor inexistente"
                }), 400
            nv_dict["Matéria"] = Materia
            nv_dict["Observação"] = Obs

            return ({"Descrição":"Professor alterado com sucesso"}),200
    return ({
        "Erro": "Requisição inválida",
        "Descrição":"Id do professor não encontrado"
    }),400

def alterarAluno(id_aluno, Turma_Id, NotaSm01, NotaSm02 ):
    nv_dict = dados
    try:
        for aluno in nv_dict["Alunos"]:
            if aluno["Id"] == id_aluno:
                
                if not turmaExiste(Turma_Id):
                    return ({
                        "Erro": "Requisição inválida",
                        "Descrição": "Turma inexistente ou inválida"
                    }), 400
                nv_dict['Id'] = Turma_Id
                nv_dict['Nota_primeiro_semestre'] = NotaSm01 
                nv_dict['Nota_primeiro_semestre'] = NotaSm02
                
                return ({"Detalhes":"Aluno alterado com sucesso"}),200
    except Exception as e:
        return ({
            "Erro": "Não foi possível fazer a requisição",
            "Descrição": str(e)
        }),500
    
#Aqui estão todas as rotas

@app.route('/Aluno', methods=['GET'])
def lista_de_alunos():
    try:
        turmas = listarAlunos()
        return jsonify(turmas),200
    except Exception as e:
        return jsonify({
            "Erro": "Requisição inválida",
            "Descrição": str(e)
        }),400
    
@app.route('/Turma', methods=['GET'])
def listar_turmas():
    try:
        turmas = listarTurma()
        return jsonify(turmas), 200
    except Exception as e:
        return jsonify({
            "Erro": "Requisição inválida",
            "Descrição": str(e)
        }), 400

@app.route('/Professor', methods=['GET'])
def listar_professores():
    try:
        dados = listarProfessor()
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({
            "Erro": "Requisição inválida",
            "Descrição": str(e)
        }), 400
    
@app.route('/Aluno/<int:Id>', methods=['GET'])
def listar_aluno_por_id(Id):
    try:
        aluno = procurarAlunoPorId(Id)
        return jsonify(aluno),200
    except AlunoNaoIdentificado as a:
        return jsonify({
            "Erro": str(a)
        }), 400

@app.route('/Professor/<int:Id>', methods=['GET'])
def listar_professor_por_id(Id):
    try:
        professor = procurarProfessorPorId(Id)
        return jsonify(professor),200
    except ProfessorNaoIdentificado as prf:
        return jsonify({
            "Erro": str(prf)
        }), 400
    
@app.route('/Turma/<int:Id>', methods=['GET'])
def listar_turma_por_id(Id):
    try:
        turma = procurarTurmaPorId(Id)
        return jsonify({
            "Turma Deletada!": turma
        }),200
    except TurmaNaoIdentificada as trm:
        return jsonify ({
            "Erro": str(trm)
        }),400
    
@app.route('/Aluno/Deletar/Id', methods=['DELETE'])
def deletar_aluno_id(Id):
    try:
        #deletarAluno(Id)
        aluno = listarAlunos()
        return jsonify ({
            "Professor Deletado!": aluno
        }),200
    except AlunoNaoIdentificado as aln:
        return jsonify ({
            "Erro": str(aln)
        }),400

@app.route('/Professor/Deletar/<int:Id_pro>', methods=['DELETE'])
def deletar_professor_id(Id_pro):
    try:
        professor = deletarProfessor(Id_pro)
        return ({
            "Professor Deletado!": professor
        }),200
    except ProfessorNaoIdentificado as prf:
        return jsonify({
            "Erro": str(prf)
        }),400
    
@app.route('/Turma/Deletar/Id', methods=['DELETE'])
def deletar_turma_por_id(Id):
    try:
        #deletarTurma(Id)
        turma = deletarTurma(Id)
        return jsonify ({
            "Turma Deletada!": turma
        }),200
    except TurmaNaoIdentificada as trm:
        return jsonify ({
            "Erro": str(trm)
        }),400
    
@app.route('/Turma/Deletar/<int:Id>', methods=['DELETE'])
def deletar_turma_por_id(Id):
    try:
        #deletarTurma(Id)
        turma = deletarTurma(Id)
        return jsonify (turma),200
    except TurmaNaoIdentificada as trm:
        return jsonify ({
            "Erro": str(trm)
        }),400

# @app.route('/Aluno/Resetar', methods = ['DELETE'])
# def resetar_aluno():
#     try:
#         resetarAlunos()
#         alunos = listarAlunos()
#         return jsonify(alunos),

    

if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)