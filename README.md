
# MLsim Web Application

## Overview
The MLsim web application is a Flask-based tool designed for running simulations involving genetic or genomic data. It offers a user-friendly web interface and is equipped with essential components for basic simulation tasks.

## Requirements
- Python 3.6 or later
- Flask 2.1.2

## Installation
1. Ensure Python 3.6+ is installed on your system.
2. Install Flask using pip:
   ```
   pip install Flask==2.1.2
   ```

## Setup
1. Clone the repository or extract the provided zip file to your desired location.
2. Navigate to the root directory of the application.
3. Run the following command to start the Flask server:
   ```
   python app/routes.py
   ```

## Usage
- Access the web application by navigating to `http://localhost:5000` in your web browser.
- Utilize the interface to interact with the simulation features provided.

## Structure
- `app/`:
  - `routes.py`: Flask routes for web interactions.
  - `static/`: Contains CSS and JavaScript files for the web interface.
  - `templates/`: HTML templates for the web interface.
  - `utils/`: Python scripts for simulation logic (genome.py, individual.py, simulator.py).

## Contribution
Feel free to contribute to the development of MLsim. To contribute, fork the repository, make your changes, and submit a pull request.

## License
MIT
