class Main {
	v
	c
	mu
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
	p_queue
	p_queueField
	l_q
	l_qField
	l_s
	l_sField
	w_q
	w_qField
	w_s
	w_sField
	myInterval
	i
	callSpeedUp

	constructor(v, c, mu, k, mu_k, rho, p_0, p_k, p_queue, l_q, l_s, w_q, w_s){
		this.i = 0
		this.v = v;
		this.firstV = v;
		this.c = c;
		this.mu = mu;
		this.k = k;
		this.mu_k = mu_k;
		this.rho = rho;
		this.p_0 = p_0;
		this.p_k = p_k;
		this.p_queue = p_queue;
		this.l_q = l_q;
		this.l_s = l_s;
		this.w_q = w_q;
		this.w_s = w_s;

		this.kField = NaN;
		this.mu_kField = NaN;
		this.rhoField = NaN;
		this.p_0Field = NaN;
		this.p_kField = NaN
		this.p_queueField = NaN;
		this.l_qField = NaN;
		this.l_sField = NaN;
		this.w_qField = NaN;
		this.w_sField = NaN;

		this.myInterval = NaN;
		this.callSpeedUp = false;
	}

	canCalculate(){
		if(this.c == 0 || this.mu == 0 || this.rho == 1){
			return false;
		}
	}

	speedUp(){
		this.callSpeedUp = true;
		clearInterval(this.myInterval);

		this.myInterval = setInterval(() => {

			if(this.i == this.k){
				clearInterval(this.myInterval);
				document.getElementById('print').disabled = false;
			}

			this.kField.innerHTML = this.i;
			this.mu_kField.innerHTML = this.mu_k[this.i];
			this.rhoField.innerHTML = this.rho;
			this.p_0Field.innerHTML = this.p_0;
			this.p_kField.innerHTML = this.p_k[this.i];
			this.p_queueField.innerHTML = this.p_queue;
			this.l_qField.innerHTML = this.l_q;
			this.l_sField.innerHTML = this.l_s;
			this.w_qField.innerHTML = this.w_q;
			this.w_sField.innerHTML = this.w_s;
			this.i++;

		}, 0)

		this.i = 0;
	}

	printResult(){

		if(this.canCalculate() == false){
			alert("Valori non validi")
			return false;
		}

		this.kField = document.getElementById('k');
		this.mu_kField = document.getElementById('mu_k');
		this.rhoField = document.getElementById('rho');
		this.p_0Field = document.getElementById('p_0');
		this.p_kField = document.getElementById('p_k')
		this.p_queueField = document.getElementById('p_queue');
		this.l_qField = document.getElementById('l_q');
		this.l_sField = document.getElementById('l_s');
		this.w_qField = document.getElementById('w_q');
		this.w_sField = document.getElementById('w_s');

		document.getElementById('print').disabled = true;
		console.log(this.kField);

		if (this.callSpeedUp == true){
			this.i = 0;
			this.callSpeedUp = false;
		}

		this.myInterval = setInterval(() => {

			if(this.i == this.k){
				clearInterval(this.myInterval);
				document.getElementById('print').disabled = false;
			}

			this.kField.innerHTML = this.i;
			this.mu_kField.innerHTML = this.mu_k[this.i];
			this.rhoField.innerHTML = this.rho;
			this.p_0Field.innerHTML = this.p_0;
			this.p_kField.innerHTML = this.p_k[this.i];
			this.p_queueField.innerHTML = this.p_queue;
			this.l_qField.innerHTML = this.l_q;
			this.l_sField.innerHTML = this.l_s;
			this.w_qField.innerHTML = this.w_q;
			this.w_sField.innerHTML = this.w_s;
			this.i++;

		}, this.v)
	}

	stopInterval(){
		document.getElementById('print').disabled = false;
		clearInterval(this.myInterval);
	}

	refresh(){
		this.i = 0;
		this.kField.innerHTML = '';
		this.mu_kField.innerHTML = '';
		this.rhoField.innerHTML = '';
		this.p_0Field.innerHTML = '';
		this.p_kField.innerHTML = '';
		this.p_queueField.innerHTML = '';
		this.l_qField.innerHTML = '';
		this.l_sField.innerHTML = '';
		this.w_qField.innerHTML = '';
		this.w_sField.innerHTML = '';
		this.v = this.firstV;

		document.getElementById('print').disabled = false;
		clearInterval(this.myInterval);
	}
}


const data = document.currentScript.dataset;
const v = parseInt(data.v);
const k = parseInt(data.k);
const mu_k = JSON.parse(data.mu_k);
const rho = parseFloat(data.rho);
const p_0 = parseFloat(data.p_0);
const p_k = JSON.parse(data.p_k);
const p_queue = parseFloat(data.p_queue);
const l_s = parseFloat(data.l_s);
const l_q = parseFloat(data.l_q);
const w_s = parseFloat(data.w_s);
const w_q = parseFloat(data.w_q);
const c = parseInt(data.c);
const mu = parseFloat(data.mu);
const myLambda = parseFloat(data.myLambda);

console.log("k: ", k)
console.log("mu_k: ", mu_k);
console.log("rho", rho);
console.log("p_0: ", p_0);
console.log("p_k: ", p_k)
console.log("p_queue: ", p_queue);

let main = new Main(v, c, mu, k, mu_k, rho, p_0, p_k, p_queue, l_q, l_s, w_q, w_s); 