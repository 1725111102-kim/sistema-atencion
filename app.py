from flask import Flask, render_template, request

app = Flask(__name__, template_folder="views")

fila = []


@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = None

    if request.method == "POST":
        accion = request.form.get("accion")

        if accion == "agregar":
            estudiante = {
                "matricula": request.form["matricula"],
                "nombre": request.form["nombre"],
                "carrera": request.form["carrera"],
                "tramite": request.form["tramite"],
            }
            fila.append(estudiante)
            mensaje = f"{estudiante['nombre']} se agrego a la fila"

        elif accion == "atender":
            if len(fila) == 0:
                mensaje = "La fila esta vacia"
            else:
                estudiante = fila.pop(0)
                mensaje = f"Se atendio a: {estudiante['nombre']}"

        elif accion == "siguiente":
            if len(fila) == 0:
                mensaje = "La fila esta vacia"
            else:
                mensaje = f"El siguiente es: {fila[0]['nombre']}"

    return render_template("index.html", fila=fila, mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)