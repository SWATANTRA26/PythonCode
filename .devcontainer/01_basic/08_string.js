/**In JS string is written in single quote or double, double quote is prefered 
  1. Old way of concatenate 
  2. New way concatenate: String interpolation, placeholder 
 */
const name1 = "Swatantra"
const repocount = 50
console.log(name1 + repocount +" PC") //1
//2* Moden way of writing code, 
console.log(`Hello my name is ${name1} and my repo count is ${repocount}`)
//2* below code will not work
console.log('Hello my name is ${name1} and my repo count is ${repocount}')

/* String declare
1. const name =  "Hello"
2. const name1 = new String("Hello")
*/

const str1 = "Hello"
const str2 = new String("Hello") //
console.log(str1[2],str2[2])
console.log(str1.length,str2.length)
console.log(str1.toUpperCase,str2.toUpperCase)