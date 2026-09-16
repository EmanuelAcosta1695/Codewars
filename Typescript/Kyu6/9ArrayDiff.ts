
export function arrayDiff(a: number[], b: number[]): number[] {
    if (a.length === 0 || b.length === 0) return a
    const resultA = a.filter(value_a => !b.includes(value_a))

    return []
}

arrayDiff([], [4, 5]) // [], 'a was [], b was [4,5]'
arrayDiff([3, 4], [3]) // [4], 'a was [3, 4], b was [3]'
arrayDiff([1, 8, 2], []) // [1, 8, 2], 'a was [1, 8, 2], b was []'
arrayDiff([1, 2, 3], [1, 2]) // [3], 'a was [1, 2, 3], b was [1, 2]'
arrayDiff([1, 2, 2], [2]) // [1], 'a was [1, 2, 3], b was [1, 2]'

// https://www.codewars.com/kata/523f5d21c841566fde000009/train/typescript
/* Implement a function that computes the difference between two lists. 
The function should remove all occurrences (a|(g)ké|rren|c(e)is) of elements from the first list (a) that are present in the second list (b). 
The order of elements in the first list should be preserved in the result.

Examples
If a = [1, 2] and b = [1], the result should be [2].

If a = [1, 2, 2, 2, 3] and b = [2], the result should be [1, 3].

If a = [1, 2, 2, 2, 3] and b = [1, 2], the result should be [3]. */