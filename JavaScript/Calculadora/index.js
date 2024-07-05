
console.log("Script conectado exitosamente")

const txtOp1 = document.getElementById("op1")
const txtOperador = document.getElementById("operador")
const txtOp2 = document.getElementById("op2")
const bttCalcular = document.getElementById("calcular")
const pResultado = document.getElementById("resultado")


function calcular() {
    const operador = txtOperador.value
    const op1 = parseFloat(txtOp1.value)
    const op2 = parseFloat(txtOp2.value)
    
    if (operador == "+" || operador == "-" || operador == "/" || operador == "*") {
        let resultado

        switch (operador) {
            case "+":
                resultado = op1 + op2

            case "-":
                resultado = op1 - op2

            case "*":
                resultado = op1 * op2

            case "/":
                resultado = op1 / op2

        }

        pResultado.innerText = "=" + resultado

    } else {
        pResultado.innerText = "Calculo imposible"
    }
}