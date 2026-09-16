export function transposeTwoStrings(arr:string[]):string{
    let stringResult: string = "";
    let i: number = 0;

    const arrA = arr[0]
    const arrB = arr[1]

    while (i < arrA.length || i < arrB.length) {
        stringResult += (arrA[i] !== undefined ? arrA[i] : ' ') + ' '
        stringResult += (arrB[i] !== undefined ? arrB[i] : ' ')
        
        if (arrB.length !== 0 && i <= arrB.length-2) {
            stringResult += '\n'
        } else if (arrB.length === 0 && i <= arrA.length-2) {
            stringResult += '\n'
        } else if (arrB.length !== 0 && i >= arrB.length-1 && i < arrA.length-1) {
            stringResult += '\n'
        } else {
            stringResult += ''
        }
        
        i += 1
    }

    return stringResult
}


transposeTwoStrings(['Hello','World']) // "H W\ne o\nl r\nl l\no d", "Should return H W\ne o\nl r\nl l\no d"
// transposeTwoStrings(['joey','louise']) // "j l\no o\ne u\ny i\n  s\n  e", "Should return j l\no o\ne u\ny i\n  s\n  e"
// transposeTwoStrings(['a','cat']) // "a c\n  a\n  t", "Should return a c\n  a\n  t"
// transposeTwoStrings(['cat','']) // "c  \na  \nt  ", "Should return c  \na  \nt  "
// transposeTwoStrings(['!a!a!','?b?b']) // "! ?\na b\n! ?\na b\n!  ", "Should return ! ?\na b\n! ?\na b\n!  "

/* https://www.codewars.com/kata/581f4ac139dc423f04000b99
You will be given an array that contains two strings. Your job is to create a function that will take those two strings and transpose them, so that the strings go from top to bottom instead of left to right.

Formatting:

There should be one space in between the two characters
If one string is longer than the other, there should be a space where the character would be
Lines should be separated by a newline character. The last line should not contain a trailing newline.
Examples
['Hello','World']

-->
`
H W
e o
l r
l l
o d`

// or, with escape sequences:
"H W\ne o\nl r\nl l\no d"
Mismatched lengths:

['ab', '123'] -->
`
a 1
b 2
  3`
  
// or, with escape sequences:
"a 1\nb 2\n  3"
*/