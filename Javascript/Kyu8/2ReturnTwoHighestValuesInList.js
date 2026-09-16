function twoHighest(arr) {

    if (!arr.length || arr.length == 1) {
        return arr
    };

    let highestNum = Math.max(...arr);

    let highestNumTwo = 0;

    arr.forEach(element => {
        if (element > highestNumTwo && element < highestNum) {
            highestNumTwo = element;
        }
    });

    return [highestNum, highestNumTwo];
}

twoHighest([15, 20, 20, 17]) // [20, 17]


/* 
In this kata, your job is to return the two distinct highest values in a list. 
If there're less than 2 unique values, return as many of them, as possible.

The result should also be ordered from highest to lowest.

Examples:
[4, 10, 10, 9]  =>  [10, 9]
[1, 1, 1]  =>  [1]
[]  =>  []
*/