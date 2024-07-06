
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
    
    if ((operador == "+" || operador == "-" || operador == "/" || operador == "*") && !isNaN(op1) && !isNaN(op2)) {
        let resultado = 0.0;

        switch (operador) {
            case "+":
                resultado = op1 + op2
                break;

            case "-":
                resultado = op1 - op2
                break;

            case "*":
                resultado = op1 * op2
                break;

            case "/":
                resultado = op1 / op2
                break;

        }
        
        pResultado.style = "color:black"
        pResultado.innerText = "= " + resultado

    } else {
        pResultado.style = "color:red"
        pResultado.innerText = "Calculo imposible"
    }
}