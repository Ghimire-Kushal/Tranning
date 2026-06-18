// console.log("Hello, World!");
// let rate = 0.13;
// console.log("rate is ", rate);
// rate = 0.15;
// const user = {
//   name: "Kushal",
//   age: 22,
 
// };
//     console.log(user.name);




// let a= 50;
// let b= 50;
// b = 100;
// console.log("The sum of a and b is: ", a);
// console.log("The sum of b and b is: ", b);



// console.log("5" +1);
// console.log("5" -1);
// console.log(0 =="");
// console.log(0 === "");



//function declaration

// function add(a, b) {
//   return a + b;
// }
// console.log(add(5, 10));




// console.log(add(1000, 10));


// const greet = function(name) {
//   return "Hello, " + name + "!";
// }
// console.log(greet("Kushal"));


// function doTwice(action){
//     action();
//     action();
// }



//arrau methods
// const price = [10, 20, 30, 40, 50];
// const withVAT = price.map(p => p * 1.13);
// console.log("with 13% VAT: ", withVAT);
// const big = price.filter(p => p > 90);
// console.log("above 90: ", big);


//local and variable scope
// let outer = "i am outside!";
// function test() {
//   let inner = "i am inside!";
//   console.log(outer);
//   console.log(inner);
// }
// test();
// console.log(inner); // This will cause an error because 'inner' is not defined in this scope




// console.log("requesting .....");
// fetch("https://api.github.com/ghimire-kushal/github")
//   .then(response => response.json())
//   .then(data => console.log(data))
//   .catch(error => console.error("Error fetching data: ", error));



//one element
const title = document.querySelector("self-info h1");
console.log(title);

//multiple elements
const listItems = document.querySelectorAll("self-info li");
console.log(listItems);   

