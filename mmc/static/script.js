class Main {
    k
    kField
    mu_k
    mu_kField
    rho
    rhoField
    myInterval

    constructor(k, mu_k, rho){
        this.k = k;
        this.kField = NaN;
        this.mu_k = mu_k;
        this.mu_kField = NaN;
        this.rho = rho;
        this.rhoField = NaN;
        this.myInterval = NaN;
    }

    printResult(){
        let i = 0;

        this.kField = document.getElementById('k');
        this.mu_kField = document.getElementById('mu_k');
        this.rhoField = document.getElementById('rho');

        document.getElementById('print').disabled = true;
        console.log(this.kField);

        this.myInterval = setInterval(() => {

            if(i == this.k){
                clearInterval(this.myInterval);
                document.getElementById('print').disabled = false;
            }

            this.kField.innerHTML = i;
            this.mu_kField.innerHTML = mu_k[i];
            this.rhoField.innerHTML = this.rho;
            console.log(mu_k[i]);
            i++;
        }, 500)
    }

    clearContent(){
        document.getElementById('print').disabled = false;
        this.kField.innerHTML = '';
        this.mu_kField.innerHTML = '';
        this.rhoField.innerHTML = '';
        clearInterval(this.myInterval);
    }
}

const data = document.currentScript.dataset;
const k = parseInt(data.k);
const mu_k = JSON.parse(data.mu_k);
const rho = parseFloat(data.rho)

console.log(k)
console.log(mu_k);
let main = new Main(k, mu_k, rho);