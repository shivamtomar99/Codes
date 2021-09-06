

let a=7;
printNumbers(a);

function printNumbers(a){
    if(a==1){
        console.log(a);
        return;
    }
    printNumbers(a-1);
    console.log(a);
}