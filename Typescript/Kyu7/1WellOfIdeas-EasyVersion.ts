export function well(x: string[]): string{
    return (x.filter(item => item === 'bad').length === x.length) ? 'Fail!' : (x.filter(item => item === 'good').length <= 2) ? 'Publish!' : 'I smell a series!'
  }

//   For every good kata idea there seem to be quite a few bad ones!
//   In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. 
//   If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. 
//   If there are no good ideas, as is often the case, return 'Fail!'.

// describe("Well of Ideas - Easy Version", () => {
//   it("Fixed tests", () => {
//     assert.strictEqual(well(['bad', 'bad', 'bad']), 'Fail!');
//     assert.strictEqual(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!');
//     assert.strictEqual(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!');
//   });
// });