const Symbols = {
    I:1,
    IV:4,
    IX:9,
    V:5,
    X:10,
    L:50,
    C:100,
    D:500,
    M:1000,
}

// const Symbols2 = {
    // IV: 4,
    // IX: 9,
// }

function check (arg) {
    let sum = 0;
    let q = 0;
    let y = 1;
    for (const [key, value] of Object.entries(Symbols)) {
        // console.log(key, value);
        for (let z in arg) {
            if (key == z) {
                sum += value;
            }
            if (q < arg.length) {
                q++; 
                y++;
            }
        }
    }


 
    return sum;    
}

// console.log(check("IIIV"));
// console.log(check("LVIII"));
// console.log(check("MCMXCIV"));
console.log(check("IXIV"));


