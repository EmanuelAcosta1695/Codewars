// 2618 ms
export function humanReadable(seconds:number):string {
  if (seconds <= 0 || seconds > 359999) return '00:00:00';

  if (seconds < 60) return `00:00:${seconds.toString().padStart(2, '0')}`;

  // 1 hours = 3600 seconds
  if (seconds === 60) return '00:01:00';

  const hour_rest = seconds % 3600

  const hours = Math.floor(seconds/3600)
  const minutes = Math.floor((hour_rest)/60)
  const second = Math.floor((hour_rest)%60)

  console.log(`${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${second.toString().padStart(2, '0')}`)
  return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${second.toString().padStart(2, '0')}`;
}

humanReadable(0)// '00:00:00', 'humanReadable(0)'
humanReadable(5)// '00:00:05', 'humanReadable(5)'
humanReadable(60)// '00:01:00', 'humanReadable(60)'
humanReadable(86399)// '23:59:59', 'humanReadable(86399)'
humanReadable(359999)// '99:59:59', 'humanReadable(359999)'

/*
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
*/


/*
Hours: Divide the total number of seconds by 3,600 (since 1 hour = 3,600 seconds) and take the whole number part.
Minutes: Take the remainder from the hours calculation, divide it by 60 (since 1 minute = 60 seconds), and take the whole number part.
Seconds: Take the final remainder after subtracting the minutes.
*/