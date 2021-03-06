from flask import Flask, request, jsonify, render_template

import re

def create_app(test_config=None):
    app = Flask(__name__, static_folder = '../client/dist', template_folder = '../client/dist', static_url_path='')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///homework.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config is not None:
        app.config.update(test_config)
    
    from .variant import db, Variant
    db.app = app
    db.init_app(app)

    from flask_cors import CORS
    CORS(app)


    @app.route('/')
    def index():
        return render_template("index.html")


    @app.route('/variant')
    def variants():
        """Return list of variants with gene equal to query parameter 'gene'"""
        genes = request.args.get('gene')
        response = {'attributes': Variant.attributes(), 'hits': 0, 'results': []}

        if genes is not None:
            genes = genes.split(',')
            variants = Variant.query.filter(Variant.gene.in_(genes)).all()
            response['hits'] = len(variants)
            response['results'] = [var.as_dict() for var in variants]

        return jsonify(response)

    @app.route('/suggest')
    def suggest_genes():
        """Return a list of genes that start with the letters in query parameter 'gene'"""
        genes = [v[0] for v in Variant.query.with_entities(Variant.gene).distinct().all()]
        gene_query = request.args.get('gene')
        
        if gene_query is not None and gene_query != '':
            suggested_genes = [g for g in genes if bool(re.match(gene_query, g, re.I))]
            suggested_genes.sort()
            return jsonify(suggested_genes)

        return jsonify([])

    return app
