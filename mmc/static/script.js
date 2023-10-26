class Main {
    k
    kField
    mu_k
    mu_kField
    rho
    rhoField
    p_0
    p_0Field
    p_k
    p_kField
    myInterval

    constructor(k, mu_k, rho, p_0, p_k){
        this.k = k;
        this.kField = NaN;
        this.mu_k = mu_k;
        this.mu_kField = NaN;
        this.rho = rho;
        this.rhoField = NaN;
        this.p_0 = p_0;
        this.p_k = p_k;
        this.p_kField = NaN
        this.p_0Field = NaN;
        this.myInterval = NaN;
    }

    printResult(){
        let i = 0;

        this.kField = document.getElementById('k');
        this.mu_kField = document.getElementById('mu_k');
        this.rhoField = document.getElementById('rho');
        this.p_0Field = document.getElementById('p_0');
        this.p_kField = document.getElementById('p_k')

        document.getElementById('print').disabled = true;
        console.log(this.kField);

        this.myInterval = setInterval(() => {

            if(i == this.k){
                clearInterval(this.myInterval);
                document.getElementById('print').disabled = false;
            }

            this.kField.innerHTML = i;
            this.mu_kField.innerHTML = this.mu_k[i];
            this.rhoField.innerHTML = this.rho;
            this.p_0Field.innerHTML = this.p_0;
            this.p_kField.innerHTML = this.p_k[i];
            console.log(mu_k[i]);
            i++;
        }, 500)
    }

    clearContent(){
        document.getElementById('print').disabled = false;
        this.kField.innerHTML = '';
        this.mu_kField.innerHTML = '';
        this.rhoField.innerHTML = '';
        this.p_0Field.innerHTML = '';
        this.p_kField.innerHTML = '';
        clearInterval(this.myInterval);
    }
}

const data = document.currentScript.dataset;
const k = parseInt(data.k);
const mu_k = JSON.parse(data.mu_k);
const rho = parseFloat(data.rho);
const p_0 = parseFloat(data.p_0);
const p_k = JSON.parse(data.p_k)

console.log("k: ", k)
console.log("mu_k: ", mu_k);
console.log("p_0: ", p_0);
console.log("p_k", p_k)
let main = new Main(k, mu_k, rho, p_0, p_k);