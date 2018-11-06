from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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