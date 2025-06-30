let mypromises = new Promise((resolve, reject) => {
    const success = false 
    if (success) {
        resolve("Promise resolved successfully!");
    } else {
        reject("Promise rejected!");
    }
});

mypromises.then(
    resolve => console.log(resolve),
    error => console.log(error)
)


// fetch api 

fetch('https://jsonplaceholder.typicode.com/posts')
.then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
    


// Task 1 :
 // write a promise with Error handling 
// Write a Promise that resolves if a number is even and  rejects if it is odd

function checkEvenOrOdd(number) {
    return new Promise((resolve, reject) => {
        if (number % 2 === 0) {
            resolve(`${number} is even.`);
        } else {
            reject(`${number} is odd.`);
        }
    });
}

console.log(checkEvenOrOdd(2))




// Task -2 
// Post a new comment by Using the POST method to add a new comment using fetch API 


// TAsk -3 
 // Fetch Data (Mock)
 // create a mock API fetch function and use async/ await to retrive and display the data 


 // Task -4
// Fetch and display the User data from the JSONPlaceholder API using async/await
     // Use free API: https://jsonplaceholder.typicode.com/users and display the user and email 


async function fetchData() {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts');
        if(!response.ok) {('failed to fetch');
            let car = await response.json();
            console.log(car);
        }
    }
        catch(error) {
            {
                console.error('Error fetching data:', error);
            }
        }
    }
fetchData()