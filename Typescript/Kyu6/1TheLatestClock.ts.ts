export function latestClock(a: number, b: number, c: number, d: number):string {
  const validTime: number = 2359;
  let hour: number = -1
  let hourStr: string = ''

  if (a < 10 && b < 10 && c < 10 && d < 10) {
    const numbers: number[][] = [
      [a, b, c, d],
      [a, b, d, c],
      [a, c, b, d],
      [a, c, d, b],
      [a, d, b, c],
      [a, d, c, b],
      [b, a, c, d],
      [b, a, d, c],
      [b, c, a, d],
      [b, c, d, a],
      [b, d, a, c],
      [b, d, c, a],
      [c, a, b, d],
      [c, a, d, b],
      [c, b, a, d],
      [c, b, d, a],
      [c, d, a, b],
      [c, d, b, a],
      [d, a, b, c],
      [d, a, c, b],
      [d, b, a, c],
      [d, b, c, a],
      [d, c, a, b],
      [d, c, b, a]
    ];

    for (let i = 0; i < numbers.length; i++) {
      let numberString: string = numbers[i].join("");
      let num: number = parseInt(numberString);

      if (num <= validTime && hour === 0) {
        hour = num
      } else {
        if (num <= validTime && num >= hour) {
          if (parseInt(`${numbers[i][2]}${numbers[i][3]}`) <= 59) {
            hour = num;
            hourStr = `${numbers[i][0]}${numbers[i][1]}:${numbers[i][2]}${numbers[i][3]}`;
          }
        }
      }
    }

    return hourStr;
  
  } else {
    return "00:00"
  }
}

// describe("Example tests", () => {
//   it("latestClock(1, 9, 8, 3) should return '19:38'", () => {
//       assert.strictEqual(latestClock(1, 9, 8, 3), "19:38");
//   });

//   it("latestClock(9, 1, 2, 5) should return '21:59'", () => {
//       assert.strictEqual(latestClock(9, 1, 2, 5), "21:59");
//   });
// });


// DESCRIPCION
// Write a function which receives 4 digits and returns the latest time of day that can be built with those digits.

// The time should be in HH:MM format.

// Examples:

// digits: 1, 9, 8, 3 => result: "19:38"
// digits: 9, 1, 2, 5 => result: "21:59" (19:25 is also a valid time, but 21:59 is later)
// Notes
// Result should be a valid 24-hour time, between 00:00 and 23:59.
// Only inputs which have valid answers are tested.