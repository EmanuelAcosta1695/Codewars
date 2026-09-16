export function multiplicationTable(size: number): number[][] {
  return Array.from({ length: size }, (_, x) =>
    Array.from({ length: size }, (_, z) => (x + 1) * (z + 1))
  )
}

/*
Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9
For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]
*/