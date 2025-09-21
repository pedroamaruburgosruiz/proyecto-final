from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Variable global única
peso_total = 0.0

def agregar_peso(medida):
    """Suma cualquier número (int o float) al peso total"""
    global peso_total
    peso_total += float(medida)
    # siempre lo guardamos como float redondeado
    peso_total = round(peso_total, 2)
    return peso_total

@app.route('/')
def index():
    return render_template("index.html", peso=peso_total)

# --- CARTÓN ---
@app.route('/carton')
def carton():
    return render_template("carton.html", peso=peso_total)

@app.route('/carton/caja')
def caja():
    return render_template("caja.html", peso=peso_total)

@app.route('/carton/plegadiza')
def plegadiza():
    return render_template("plegadiza.html", peso=peso_total)

@app.route('/caja/<medida_caja>')
def medida_caja(medida_caja):
    nuevo_peso = agregar_peso(medida_caja)
    return render_template(
        "carton_resultado.html",
        medida_caja=medida_caja,
        peso=nuevo_peso,
        peso_final=nuevo_peso
    )

@app.route('/plegadiza/<float:medida_plegadiza>')
def medida_plegadiza(medida_plegadiza):
    nuevo_peso = agregar_peso(medida_plegadiza)
    return render_template(
        "carton_resultado.html",
        medida_plegadiza=medida_plegadiza,
        peso=nuevo_peso,
        peso_final=nuevo_peso
    )

# --- PAPEL ---
@app.route('/papel')
def papel():
    return render_template("papel.html", peso=peso_total)

@app.route('/papel/<float:medida_papel>')
def medida_papel(medida_papel):
    nuevo_peso = agregar_peso(medida_papel)
    return render_template(
        "papel_resultado.html",
        medida_papel=medida_papel,
        peso=nuevo_peso,
        peso_final=nuevo_peso
    )

# --- PLÁSTICO ---
@app.route('/plastico')
def plastico():
    return render_template("plastico.html", peso=peso_total)

@app.route('/plastico/pet')
def pet():
    return render_template("pet.html", peso=peso_total)

@app.route('/plastico/pasta')
def pasta():
    return render_template("pasta.html", peso=peso_total)

@app.route('/pet/<float:medida_pet>')
def medida_pet(medida_pet):
    nuevo_peso = agregar_peso(medida_pet)
    return render_template(
        "plastico_resultado.html",
        medida_pet=medida_pet,
        peso=nuevo_peso,
        peso_final=nuevo_peso
    )

@app.route('/pasta/<float:medida_pasta>')
def medida_pasta(medida_pasta):
    nuevo_peso = agregar_peso(medida_pasta)
    return render_template(
        "plastico_resultado.html",
        medida_pasta=medida_pasta,
        peso=nuevo_peso,
        peso_final=nuevo_peso
    )

# --- LATAS ---
@app.route('/latas')
def latas():
    return render_template("latas.html", peso=peso_total)

@app.route('/latas/<float:medida_latas>')
def medida_latas(medida_latas):
    nuevo_peso = agregar_peso(medida_latas)
    return render_template(
        "latas_resultado.html",
        medida_latas=medida_latas,
        peso=nuevo_peso,
        peso_final=nuevo_peso
    )

# --- RESET ---
@app.route('/reset')
def reset():
    global peso_total
    peso_total = 0.0
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
