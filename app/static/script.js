
function startSimulation() {
    let generations = document.getElementById('generation-input').value;
    fetch('/start_simulation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ generations: generations }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById('simulation-data').innerText = 
            'Simulation started for ' + data.generations + ' generations.';
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
