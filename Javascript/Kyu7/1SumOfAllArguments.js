function sum(...args) {

    let sum_arguments = 0 

    for (let i = 0; i < args.length; i++) {
        sum_arguments += args[i];
    };

    return sum_arguments
}


sum(5, 7, 9) // 21

/*
Write a function that finds the sum of all its arguments.

eg:

sum(1, 2, 3) // => 6
sum(8, 2) // => 10
sum(1, 2, 3, 4, 5) // => 15
*/