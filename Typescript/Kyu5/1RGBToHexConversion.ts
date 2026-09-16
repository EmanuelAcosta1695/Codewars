export function rgb(r: number, g: number, b: number): string {
  return [r, g, b]
    .map((str) =>
      (str <= 0
        ? '00'
        : str > 255
        ? 'FF'
        : str.toString(16).length === 1
        ? '0' + str.toString(16)
        : str.toString(16)
      ).toUpperCase()
    )
    .join('')
}

export const rgb = (r: number, g: number, b: number): string =>
  [r, g, b]
    .map((str) =>
      (str <= 0
        ? '00'
        : str > 255
        ? 'FF'
        : str.toString(16).length === 1
        ? '0' + str.toString(16)
        : str.toString(16)
      ).toUpperCase()
    )
    .join('')

// because the join('') at the end, it converts to string the array

rgb(0, 0, 0) // "000000"
rgb(0, 0, -20) // "000000"
rgb(300, 255, 255) // "FFFFFF"
rgb(173, 255, 47) // "ADFF2F"

/*
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a 
hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that 
fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"

*/
