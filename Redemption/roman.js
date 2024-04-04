const Symbols = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

var romanToInt = function (s) {
  let result = 0;
  for (let i = 0; i < s.length; i++) {
    const currentSymbolValue = Symbols[s[i]];
    const nextSymbolValue = Symbols[s[i + 1]];

    if (nextSymbolValue && currentSymbolValue < nextSymbolValue) {
      result += nextSymbolValue - currentSymbolValue;
      i++;
    } else {
      result += currentSymbolValue;
    }
  }
  return result;
};

console.log(romanToInt("III")); // Output: 3
console.log(romanToInt("LVIII")); // Output: 58
console.log(romanToInt("MCMXCIV")); // Output: 1994
