from flask import Flask, render_template, request
app = Flask(__name__)

bd={"usuario":"flavio.ken13@gmail.com","senha":"250900"}

def usuario_existe(usuario):
	return  usuario == bd["usuario"]

def verifica_senha(usuario,senha):
	return usuario == bd["usuario"] and senha==bd["senha"]

@app.route("/saque")
def saque():
	return render_template("saque.html")

@app.route("/saqueresult")
def saqueresult():
	return render_template("saqueresult.html")

@app.route("/saldo")
def saldo():
	return render_template("saldo.html")

@app.route("/deposito")
def deposito():
	return render_template("deposito.html")

@app.route("/depositoresult",methods=['POST'])
def depositoresult():
	if request.method == "POST":
		response = request.form
		print("response")
		print(response)
	return render_template("depositoresult.html")

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/aluno")
def student():
	return render_template("aluno.html")

@app.route("/corrente")
def corrente():
	return render_template("corrente.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/saqueresult",methods=['POST'])
def saque_result():

	if request.method == "POST":
		response = request.form
		print("response")
		print(response)
		return render_template("saqueresult.html")

@app.route("/loginresult",methods=['POST'])
def login_result():

	if request.method == "POST":
		response = request.form
		print("response")
		print(response)

		result={"status":"correto"}
		if usuario_existe(response["email"]):

			if verifica_senha(response["email"],response["senha"]):
				return render_template("loginresult.html",result=result)
			else:
				result["status"]="senha_incorreta"
				return render_template("loginresult.html",result=result)
		else:
			result["status"]="usuario_incorreto"
			return render_template("loginresult.html",result=result)

@app.route("/result",methods=['POST'])
def result():
	if request.method == "POST":
		result = request.form
		print("result")
		print(result)
		return render_template("result.html")

if __name__== "__main__":
	app.run(host="0.0.0.0",debug= True)

