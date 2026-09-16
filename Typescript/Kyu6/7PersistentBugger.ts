export function persistence(num: number): number {
  return num < 10
    ? 0
    : 1 +
        persistence(
          num
            .toString()
            .split('')
            .reduce((acc, current) => acc * parseInt(current), 1)
        )

  // the last 1 set the value of acc (accumulator)
}

/*
For num = 39, let's go step by step:

First call:

num = 39, it's not a single digit, so it goes to the recursive case:
ts
Copiar código
persistence(27) // num = 39, after multiplying digits: 3 * 9 = 27
It adds 1 to whatever result comes from persistence(27).
Second call:

num = 27, it's not a single digit, so it goes to the recursive case:
ts
Copiar código
persistence(14) // num = 27, after multiplying digits: 2 * 7 = 14
It adds 1 to whatever result comes from persistence(14).
Third call:

num = 14, it's not a single digit, so it goes to the recursive case:
ts
Copiar código
persistence(4) // num = 14, after multiplying digits: 1 * 4 = 4
It adds 1 to whatever result comes from persistence(4).
Fourth call:

num = 4, it's a single digit, so it returns 0 because no more multiplications are needed.
Final Computation:
The fourth call returns 0 (because 4 is already a single digit).
The third call adds 1 to that result, so it returns 1.
The second call adds 1 to that result, so it returns 2.
The first call adds 1 to that result, so it returns 3.
Thus, the persistence of 39 is 3.

In each recursive call, the 1 + in the return statement doesn’t lose its value because recursion builds a call stack. 
Each call to the function is "waiting" for the result of the next recursive call before it can finish its own computation.

When a function calls itself (recursion), each function call is pushed onto the call stack. 
The current function pauses and waits for the result of the next recursive call to return. 
Once the deepest call returns, each call on the stack finishes one by one in reverse order, adding 1 at each step.
*/

persistence(39) // 3
persistence(4) // 0
persistence(25) // 2
persistence(999) // 4

/*
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
*/