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

const Symbols2 = {
    IV: 4,
    IX: 9,
}
function check (arg) {
    let sum = 0;
    let sum2 = 0;
    for (const [key, value] of Object.entries(Symbols)) {
        // console.log(key, value);
        for (let z of arg) {
            if (key == z) {
                sum += value;
            }
        }

    }
    
    for (const [key2, value2] of Object.entries(Symbols2)) {
        for (let ii in arg) {
            for (let q = 1; q < (arg.length); q++) {
                if (arg[ii] + arg[q] == key2) {
                    console.log(arg[ii], arg[q]);
                    sum2 += value2;
                }
                
            }
        }
    }

    return sum2;    
}

// console.log(check("IIIV"));
// console.log(check("LVIII"));
// console.log(check("MCMXCIV"));
console.log(check("IXIV"));


