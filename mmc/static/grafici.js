let myChart = null;

const plot = (kLen, p_k) => {

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

	const ctx = document.getElementById('queueChart').getContext('2d');

	if(myChart != null){
		myChart.destroy();
	}
	myChart = new Chart(ctx, config);
}

const closePlot = () => {
	myChart.destroy();
}