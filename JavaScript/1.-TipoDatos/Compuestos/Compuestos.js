
// LISTAS

let myList = ["Ojo", "Danny", 20]
console.log(typeof myList) // Todo lo que no sea una variable primitiva es un objeto
console.log(myList)
console.log(myList[0])

// CONJUNTOS

let mySet = new Set(["Ojo", "Danny", 20, "Ojo"]) // En un conjunto no hay valores repetidos
mySet.add(20)
console.log(mySet)

// MAPA O DICCIONARIO

let myDic = new Map([["Dann" , 20], ["Ojo", "Si"]]) // Un mapa no admite claves repetidas
myDic.set("NO", 24)
console.log(myDic)
console.log(myDic.get("Ojo"))

// ENUM

let myEnum = {
    Hola : "Adios",
    Hol : "Adios",
    Ho : "Adios",
    H : "Adios"
}