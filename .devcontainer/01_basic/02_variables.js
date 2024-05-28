const accountID = 144553  
//Variable defined as const can't be modified, if accountID is declared with other value compiler will give error.
let accountEmail ="swatantra@google.com"
var accountPassword = "123"
accountCity = "Bhopal"
accountState = {};  // Output in console will be blank.
let accState;       // Output will be undefined.
/*Note:
    In JS variable can be declared in 2 way by using let & var; 
    Scope {} curly bracess is also known as scope. So using var can create with scope. thus let is recommnded to use.
    In JS we have "block scope" and "functional scope"
*/
console.log([accountID,accountEmail, accountPassword])
console.table([accountID,accountEmail, accountPassword, accountCity, accountState, accState])// Give output in tebuler form.