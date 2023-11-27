
from flask import Flask, render_template, request, jsonify
from .utils.simulator import Simulator

app = Flask(__name__)
simulator = Simulator(population_size=50, environment=[0, 0, 0])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_simulation', methods=['POST'])
def start_simulation():
    generations = request.json.get('generations', 100)
    simulator.run_simulation(generations)
    return jsonify({'status': 'Simulation started', 'generations': generations})

@app.route('/get_population_data', methods=['GET'])
def get_population_data():
    population_data = {'population_size': len(simulator.population)}
    return jsonify(population_data)

@app.route('/adjust_parameters', methods=['POST'])
def adjust_parameters():
    new_params = request.json
    simulator.environment = new_params.get('environment', simulator.environment)
    return jsonify({'status': 'Parameters adjusted'})

if __name__ == '__main__':
    app.run(debug=True)
