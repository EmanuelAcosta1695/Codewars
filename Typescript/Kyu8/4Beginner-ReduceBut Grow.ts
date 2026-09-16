export function grow(arr: number[]): number {
  return arr.reduce((acc, value) => acc * value, 1);
}

grow([1, 2, 3]) //6

// Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
// [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24