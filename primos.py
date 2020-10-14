import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route('/')
def nao_entre_em_panico():
    x = []

    divisores = 0
    cont = 1
    numero = 1

    while len(x) < 100:
        divisores = 0
        cont = 1

        while cont <= numero:
            if (numero % cont) == 0:
                divisores += 1
            cont += 1

        if divisores == 2:
            m = str(numero)
            x.append(m)

        numero += 1

    def convert(s):
        m = " "
        return m.join(s)

    primos = convert(x)

    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
