from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class GenomeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genes = db.Column(db.PickleType)  # Storing list of genes as a pickled object

    def __repr__(self):
        return f'<Genome {self.id}>'

class IndividualModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genome_id = db.Column(db.Integer, db.ForeignKey('genome_model.id'))
    genome = db.relationship('GenomeModel', backref='individuals')
    fitness = db.Column(db.Float)
    energy = db.Column(db.Integer)
    health = db.Column(db.Integer)

    def __repr__(self):
        return f'<Individual {self.id}>'

class SimulationResultModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    individual_id = db.Column(db.Integer, db.ForeignKey('individual_model.id'))
    individual = db.relationship('IndividualModel', backref='results')
    simulation_data = db.Column(db.String)  # Placeholder for simulation result data

    def __repr__(self):
        return f'<SimulationResult {self.id}>'