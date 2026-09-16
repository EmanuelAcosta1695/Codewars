/** return the output array and ignore all non-op characters */
export function parse(data: string): number[] {
  let value: number = 0
  let values: number[] = []

  ;[...data].forEach((char: string) => {
    if (char === 'i') value += 1
    if (char === 'd') value -= 1
    if (char === 's') value **= 2
    if (char === 'o') values.push(value)
  })

  return values
} // My solution was similar to the best

parse('iiisdoso') // [ 8, 64 ]
parse('iiisxxxdoso') // [ 8, 64 ]

/*
Create a parser to interpret and execute the Deadfish language.

Deadfish operates on a single value in memory, which is initially set to 0.

It uses four single-character commands:

i: Increment the value
d: Decrement the value
s: Square the value
o: Output the value to a result array
All other instructions are no-ops and have no effect.

Examples
Program "iiisdoso" should return numbers [8, 64].
Program "iiisdosodddddiso" should return numbers [8, 64, 3600].
*/