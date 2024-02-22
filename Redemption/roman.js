const Symbols = {
    I:1,
    V:5,
    X:10,
    L:50,
    C:100,
    D:500,
    M:1000,
}

let sum = 0;

function check (arg) {
    
    for (let x of Object.entries(Symbols)) {
        let i = 0;
        for (const [key, value] of Object.entries(Symbols)) {
            i++;
            if (i > (String(arg).length) - 1) {
                i = 0;
            }
            console.log(arg[i]);
        }
        // console.log(i, arg.length);
        // i++;
        // if (i == arg.length) {
        //     i = 0;
        // }
    }
    return '';    
}

console.log(check("IVL"));


