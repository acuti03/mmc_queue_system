class Main {
    k;
    kField
    myInterval

    constructor(k){
        this.k = k;
        this.kField = NaN
        this.myInterval = NaN;
    }

    printResult(){
        let i = 0;
        this.kField = document.getElementById('k');
        document.getElementById('print').disabled = true;
        console.log(this.kField);

        this.myInterval = setInterval(() => {

            if(i == this.k + 100){
                clearInterval(this.myInterval);
                document.getElementById('print').disabled = false;
            }

            this.kField.innerHTML = i;
            console.log(i);
            i++;
        }, 1000)
    }

    clearContent(){
        document.getElementById('print').disabled = false;
        this.kField.innerHTML = '';
        clearInterval(this.myInterval);
    }
}

const data = document.currentScript.dataset;
const k = parseInt(data.c);
console.log(k);
let main = new Main(k);