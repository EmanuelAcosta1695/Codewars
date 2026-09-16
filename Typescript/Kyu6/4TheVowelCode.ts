// turn vowels into numbers
export function encode(string: string): string {
  return [...string]
    .map((char) => {
      return char === 'a'
        ? 1
        : char === 'e'
        ? 2
        : char === 'i'
        ? 3
        : char === 'o'
        ? 4
        : char === 'u'
        ? 5
        : char
    })
    .join('')
}

// turn numbers back into vowels
export function decode(string: string): string {
  return [...string]
    .map((char) => {
      return char === '1'
        ? 'a'
        : char === '2'
        ? 'e'
        : char === '3'
        ? 'i'
        : char === '4'
        ? 'o'
        : char === '5'
        ? 'u'
        : char
    })
    .join('')
}

encode('hello') // 'h2ll4'
encode('How are you today?') // 'H4w 1r2 y45 t4d1y?'
encode('This is an encoding test.') // 'Th3s 3s 1n 2nc4d3ng t2st.'

decode('h2ll4') // 'hello'
decode('H4w 1r2 y45 t4d1y?') // 'How are you today?'
decode('Th3s 3s 1n 2nc4d3ng t2st.') // 'This is an encoding test.'

/*
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.
*/