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

