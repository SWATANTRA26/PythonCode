/* In JS it is slightly issue in conversion 
    when we are taking data to front end of backend we don't know from where vlaue is coming 
    To convert values we can use Number, Boolean, String 
*/
let score = "33ab"
console.log(typeof score)
console.log(typeof(score))
//change score from 33 to "33" output will be string
let newNumber = Number(score)
console.log(typeof newNumber)
console.log(newNumber)
// Change score 33ab this will change newNumber into number but its value will be null

let isLogin = 1
let booleanIsLoggedIn = Boolean(isLogin)
console.log(booleanIsLoggedIn)

/*
**********************Operations*****************************
Addition, Subtraction 
+ - * **(power) /, %(reminder)
*/

let value = 3
let negValue = -value
console.log(negValue)

let str1 = "Hello"
let str2 = "Swatantra"
let str3 = str1 + str2
console.log(str3)
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment
//https://tc39.es/ecma262/#sec-object-environment-records
