let myChart1 = null;
let myChart2 = null;
let myChart3 = null;

const plot1 = (kLen, p_k, w_s, packagesInQueue, queueEventTimes) => {

	plot2(w_s);
	plot3(packagesInQueue, queueEventTimes)

	kLen = +kLen + 1
	const k = Array(kLen);

	let regex = /\d+\.\d+/g;
	p_k = p_k.match(regex);

	for(let i = 0; i < kLen; i++){
		k[i] = i;
	}

	const coordinates = Array(kLen);

	for(let i = 0; i < kLen; i++){
		coordinates[i] = {
			x: k[i],
			y: p_k[i]
		}
	}

	const data = {
		datasets: [{
			label: 'x = k, y = Pk',
			data: coordinates,
			backgroundColor: '#37a2eb'
		}],
	};

	const config = {
		type: 'scatter',
		data: data,
		options: {
			responsive: true,
			scales: {
				x: {
					display: true,
					title: {
						display: true,
						text: 'k',
						font: {
							family: 'JetBrains Mono',
							size: 20,
							weight: 'bold',
							lineHeight: 1.2,
						},
						padding: {top: 20, left: 0, right: 0, bottom: 0}
					}
				},
				y: {
					display: true,
					title: {
					display: true,
					text: 'Pk',
					font: {
						family: 'JetBrains Mono',
						size: 20,
						style: 'normal',
						lineHeight: 1.2
					},
					padding: {top: 30, left: 0, right: 0, bottom: 0}
					}
				}
			}
		}
	}

	const ctx = document.getElementById('queueChart1').getContext('2d');

	if(myChart1 != null){
		myChart1.destroy();
	}
	myChart1 = new Chart(ctx, config);
}

const plot2 = (w_s) => {

	let regex = /\d+\.\d+/g;
	w_s = w_s.match(regex);

	const coordinates = Array(100);

	for(let i = 0; i < 100; i++){
		coordinates[i] = {
			x: i / 100,
			y: w_s[i]
		}
	}

	const data = {
		datasets: [{
			label: 'x = rho, y = Ws * μTot',
			data: coordinates,
			backgroundColor: '#ff6384'
		}],
	};

	const config = {
		type: 'scatter',
		data: data,
		options: {
			responsive: true,
			scales: {
				x: {
					display: true,
					title: {
						display: true,
						text: 'rho',
						font: {
							family: 'JetBrains Mono',
							size: 20,
							weight: 'bold',
							lineHeight: 1.2,
						},
						padding: {top: 20, left: 0, right: 0, bottom: 0}
					}
				},
				y: {
					display: true,
					title: {
					display: true,
					text: 'Ws * μTot',
					font: {
						family: 'JetBrains Mono',
						size: 20,
						style: 'normal',
						lineHeight: 1.2
					},
					padding: {top: 30, left: 0, right: 0, bottom: 0}
					}
				}
			}
		}
	}

	const ctx = document.getElementById('queueChart2').getContext('2d');

	if(myChart2 != null){
		myChart2.destroy();
	}
	myChart2 = new Chart(ctx, config);
}

const plot3 = (packagesInQueue, queueEventTimes) => {

	let regex1 = /\d/g;
	let regex2 = /\d+\.\d+/g;
	packagesInQueue = packagesInQueue.match(regex1);
	queueEventTimes = queueEventTimes.match(regex2);

	console.log(queueEventTimes)

	const coordinates = Array(packagesInQueue.length);

	for(let i = 0; i < coordinates.length; i++){
		coordinates[i] = {
			x: queueEventTimes[i],
			y: packagesInQueue[i]
		}
	}

	const data = {
		labels: queueEventTimes,
		datasets: [{
			label: 'x = time(seconds), y = packages in the queue',
			data: packagesInQueue,
			borderColor: '#537bc4',
			fill: false,
			stepped: true,
		}],
	};

	
	const config = {
		type: 'line',
		data: data,
		options: {
			responsive: true,
		 	interaction: {
				intersect: false,
				axis: 'x'
			},
			plugins: {
				title: {
					display: true
				}
			}
		}
	};

	const ctx = document.getElementById('queueChart3').getContext('2d');

	if(myChart3 != null){
		myChart3.destroy();
	}
	myChart3 = new Chart(ctx, config);
}

const closePlot = () => {
	myChart1.destroy();
	myChart2.destroy();
	myChart3.destroy();
}