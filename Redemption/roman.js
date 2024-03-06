const Symbols = {
  I: 1,
  IV: 4,
  V: 5,
  IX: 9,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
  XL: 40,
  XC: 90,
  CD: 400,
  CM: 900,
  Z: 0,
};

var intToRoman = function (num) {
  let sum = 0;
  let sum2 = 0;
  let y = 1;
 
  for (const [key, value] of Object.entries(Symbols)){
    for (let z of num) {

      if (z == key && z + num[y] != key) {
        sum += value;
      } else if (z + num[y] == key) {
        console.log(key, value);
        sum2 += value;
      }
     
      y++;

      if (y >= num.length) {
        y = 0;
      }
    }
  }

  let result = sum - sum2;

  
  return `${sum} - ${sum2} ${result}`;
};

// console.log(check("IIIV"));
// console.log(check("LVIII"));
// console.log(intToRoman("MCMXCIV"));
console.log(intToRoman("VI")); //9 4 10 5 1 = 29 correcto

