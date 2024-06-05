//console.log(2>1)
//console.log(2 == 1)

//*******When we compare two different DT */
console.log("2">1);
console.log("02"<1);
// Most of time we should avoide such comparision.
//*********** */
console.log(null >0)
console.log(null >= 0)
console.log(null == 0)
console.log(null >=0)

// Strict comparision 
console.log("2" === 2)

/*In JS DT are either "Primitive" & "Non primitive" This classification is done based on how data is being stored in memory and how to access the same. 
    primitive: String,Number, Boolean, null, undefined, Symbol, BigInt(for very big number)
    Non primitive/refrence type: Array, Objects, Functions

    Call by value: primitive; 
    call by refrence: Non primitive;
    Is Js is dynamic type or static: So JS is dynamic language 
*/

// Declare symbol 
const id = Symbol("123")
console.log(id)

// Declare Array's
const heros = ["Shaktiman","GangMaster GOGO", "Tony Stark"]
let myObj = {
    name : "Swatantra",
    age : 32
}

// Declare Function
const myFunction = function(){
    console.log("Hello World")
}
myFunction()
console.log(typeof myObj)
console.log(typeof heros)
console.log(typeof myFunction)