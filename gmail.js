document.getElementById('waterForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);
    const location = formData.get('location');
    const temperature = formData.get('temperature');
    const ph = formData.get('ph');
    const turbidity = formData.get('turbidity');
    const dissolvedOxygen = formData.get('dissolvedOxygen');
    const hardness = formData.get('hardness');
    const solids = formData.get('solids');
    const chloramines = formData.get('chloramines');
    const sulfate = formData.get('sulfate');
    const organicCarbon = formData.get('organicCarbon');
    const conductivity = formData.get('conductivity');

    const response = await fetch('/predictWaterPortability', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ location, temperature, ph, turbidity, dissolvedOxygen, hardness, solids, chloramines, sulfate, organicCarbon, conductivity })
    });

    if (response.ok) {
        const predictionResult = await response.text();
        const portabilityMessage = predictionResult === 'potable' ? 'Water is Potable' : 'Water is Not Potable';
        document.getElementById('predictionResult').textContent = portabilityMessage;
    } else {
        console.error('Prediction request failed');
    }
});
