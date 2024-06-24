
// STRINGS

var myString = "Como le va compañero" // var define variables globales
console.log(myString)

let myString2 = "Que tal te va" // let define variables dentro del espacio donde se creo
myString2 = "No te la esperabas"

// Cambio de tipo de variable
console.log(myString2)
console.log(typeof myString2)

myString2 = 6
console.log(myString2)
console.log(typeof myString2)

// NUMBERS

let myNumber = 7
myNumber += 4
console.log(myNumber)
console.log(myNumber + 1)

// Mezcla de dos tipos de datos

console.log(myNumber + " " + myString)

let myNumber2 = 2.5
console.log(typeof myNumber2)

// BOOLEANS

let myBool = false
console.log(myBool)
console.log(typeof myBool)

// NULL

myBool = null
console.log(myBool)
console.log(myBool + myNumber2) //null + 2.5 = 2.5

// UNDEFINED (No es una buena practica)

myBool = undefined
console.log(undefined)
let myUndefined
console.log(myUndefined)

// CONSTANTES 

const MY_CONST = "No me puedes cambiar"
// MY_CONST = "Seguro?"   ERROR
console.log(MY_CONST)

