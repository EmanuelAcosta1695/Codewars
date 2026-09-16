// 2815 ms
export const listSquared = (m:number, n:number):number[][] => {
    const results: number[][] = [];
    
    for (let i = m; i <= n; i++) {
        const divisors: number[] = getDivisors(i)

        const squares: number[] = divisors.map((divisor) => divisor**2)

        const sum: number = squares.reduce((accumulator, current) => accumulator+current)

        const sqrt: number | null = Number.isInteger(Math.sqrt(sum)) ? Math.sqrt(sum) : null;
    
        if (sqrt != null) {
            results.push([i, sum])
        }
    }

    return results
}

function getDivisors(n:number): number[] {
    const divisors: number[] = [];
    const sqrt = Math.sqrt(n);

    for (let i = 1; i <= sqrt; i++) {
        if (n % i === 0) {
            divisors.push(i);
            const counterpart = n / i;
            if (counterpart !== i) {
                divisors.push(counterpart);
            }
        }
    }

    return divisors.sort((a, b) => a - b);
}

listSquared(1, 250) // [[1, 1], [42, 2500], [246, 84100]];
// listSquared(42, 250) // [[42, 2500], [246, 84100]];
// listSquared(250, 500) // [[287, 84100]];
// listSquared(300, 600) // [];

/*
1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246.

Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681.

The sum of these squares is 84100 which is 290 * 290.

Task
Find all integers between m and n (m and n are integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.

We will return an array of subarrays or of tuples (in C an array of Pair) or a string.

The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.

Example:
m =  1, n = 250 --> [[1, 1], [42, 2500], [246, 84100]]
m = 42, n = 250 --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see "Sample Tests".

Note
In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.


*/