from flask import Flask, render_template, request
from database import conectar

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nova-visita")
def nova_visita():
    return render_template("nova-visita.html")

@app.route("/visitas")
def visitas():
    return render_template("visitas.html")


@app.route("/visitas", methods=["POST"])
def criar_visita():
    dados = request.form

    cliente = dados.get("clienteNome")
    turma = dados.get("turmaNome")
    tecnico = dados.get("tecnico")
    data = dados.get("data")
    horario = dados.get("horario")
    endereco = dados.get("endereco")
    observacoes = dados.get("observacoes")

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO visita
        (cliente, tecnico, data, horario, motivo, observacoes, turma, endereco)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        cliente,
        tecnico,
        data,
        horario,
        "Visita técnica",
        observacoes,
        turma,
        endereco
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    return """
        <script>
            alert("Visita agendada com sucesso!");
            window.location.href = "/";
        </script>
    """

if __name__ == "__main__":
    app.run(debug=True)