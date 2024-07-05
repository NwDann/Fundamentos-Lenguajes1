
let myList = ["Ojo", "Danny", 20]

for (const value of myList) {
    console.log(value)
}

for (let i = 0; i < 10; i++){
    console.log(i)
}

let myCounter = 0

while(myCounter < myList.length) {
    console.log(myList[myCounter])
    myCounter++
}