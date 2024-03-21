const Symbols = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
  Z: 0,
};

const SymbolsR = {
  IV: 4,
  IX: 9,
  XL: 40,
  XC: 90,
  CD: 400,
  CM: 900,
};

var intToRoman = function (num) {
  let sum = 0;
  let sum2 = 0;
  let y = 1;

  for (const [key, value] of Object.entries(Symbols)) {
    for (let z of num) {
      if (z == key) {
        sum += value;
      }

      // else if (z + num[y] == key) {
      // console.log(key, value);
      // sum2 += value;
      // }
    }

    for (const [a, b] of Object.entries(SymbolsR)) {
      console.log(num);
    }
  }

  return `${sum} - ${sum2}`;
};

console.log(intToRoman("VI"));
// console.log(check("LVIII"));
// console.log(intToRoman("MCMXCIV"));
