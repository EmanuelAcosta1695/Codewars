export function findShort(s: string): number {
    return [...s.split(" ")].reduce((longestWord, word) => {
        return longestWord.length == 0 ? word : word.length < longestWord.length ? word : longestWord;
    }, "").length;
}

// Simple, given a string of words, return the length of the shortest word(s).

// String will never be empty and you do not need to account for different data types.