from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import select
import re

app = Flask(__name__, static_folder = './client/dist', template_folder = './client/dist', static_url_path='')
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///homework.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Variant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gene = db.Column(db.Text)
    nucleotide_change = db.Column(db.Text)
    protein_change = db.Column(db.Text)
    other_mappings = db.Column(db.Text)
    alias = db.Column(db.Text)
    transcripts = db.Column(db.Text)
    region = db.Column(db.Text)
    reported_classification = db.Column(db.Text)
    inferred_classification = db.Column(db.Text)
    source = db.Column(db.Text)
    last_evaluated = db.Column(db.Text)
    last_updated = db.Column(db.Text)
    url = db.Column(db.Text)
    submitter = db.Column(db.Text)
    assembly = db.Column(db.Text)
    chr = db.Column(db.Text)
    genomic_start = db.Column(db.Text)
    genomic_stop = db.Column(db.Text)
    ref = db.Column(db.Text)
    alt = db.Column(db.Text)
    accession = db.Column(db.Text)
    reported_ref = db.Column(db.Text)
    reported_alt = db.Column(db.Text)

    @classmethod
    def attributes(cls):
        return cls.__table__.columns.keys()

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return "<Variant (id=%s, gene='%s')>" % (self.id, self.gene)

@app.route('/')
def index():
    return render_template("index.html")

# return list of variants with gene equal to query parameter 'gene'
@app.route('/variant')
def variants():
    genes = request.args.get('gene')
    response = {'attributes': Variant.attributes(), 'hits': 0, 'results': []}
    if genes is not None:
        genes = genes.split(',')
        variants = Variant.query.filter(Variant.gene.in_(genes)).all()
        response['hits'] = len(variants)
        response['results'] = [var.as_dict() for var in variants]
    return jsonify(response)

# suggest list of genes with query parameter 'gene'
genes = [v[0] for v in Variant.query.with_entities(Variant.gene).distinct().all()]
@app.route('/suggest')
def suggest_genes():
    gene = request.args.get('gene')
    suggested_genes = [g for g in genes if bool(re.match(gene, g, re.I))]
    suggested_genes.sort()
    return jsonify(suggested_genes)