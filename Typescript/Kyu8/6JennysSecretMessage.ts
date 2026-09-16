export function greet(name:string): string {
  return name === "Johnny" ? 'Hello, my love!' : `Hello, ${name}!`
}

// 'should greet some people normally'
greet('Jim') //'Hello, Jim!'
greet('Jane') //'Hello, Jane!'
greet('Simon') //'Hello, Simon!'
  
//'should greet Johnny a little bit more special'
greet('Johnny') //'Hello, my love!'

/*
Jenny has written a function that returns a greeting for a user. 
However, she's in love with Johnny, and would like to greet him slightly different. 
She added a special case to her function, but she made a mistake.

Can you help her?
*/