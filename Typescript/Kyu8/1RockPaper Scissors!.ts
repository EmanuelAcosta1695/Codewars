export function rps(p1: string, p2: string): string{
    const plays: string[] = ['scissors', 'paper', 'rock']

    if (p1 === plays[0] && p2 === plays[1] ||
        p1 === plays[1] && p2 === plays[2] ||
        p1 === plays[2] && p2 === plays[0]) {
        return 'Player 1 won!'
    } else if (p1 === p2) {
        return 'Draw!'
    } else {
        return 'Player 2 won!'
    }
}


//   Rock Paper Scissors
//   Let's play! You have to return which player won! In case of a draw return Draw!.
  
//   Examples(Input1, Input2 --> Output):
  
//   "scissors", "paper" --> "Player 1 won!"
//   "scissors", "rock" --> "Player 2 won!"
//   "paper", "paper" --> "Draw!"



// import { assert } from "chai";

// import { rps } from "./solution";

// describe("Beginner - Lost Without a Map", () => {
  
//   const getMsg = (n: number): string => `Player ${n} won!`;  
 
//   it('player 1 win', () => {
//     assert.strictEqual(rps('rock', 'scissors'), getMsg(1));
//     assert.strictEqual(rps('scissors', 'paper'), getMsg(1));
//     assert.strictEqual(rps('paper', 'rock'), getMsg(1));
//   });

//   it('player 2 win', () => {
//     assert.strictEqual(rps('scissors', 'rock'), getMsg(2));
//     assert.strictEqual(rps('paper', 'scissors'), getMsg(2));
//     assert.strictEqual(rps('rock', 'paper'), getMsg(2));
//   });

//   it('draw', () => {
//     assert.strictEqual(rps('rock', 'rock'), 'Draw!');
//     assert.strictEqual(rps('scissors', 'scissors'), 'Draw!');
//     assert.strictEqual(rps('paper', 'paper'), 'Draw!');
//   }); 
// });