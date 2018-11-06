#!/bin/bash

file="homework.db"
#remove the database if it already exists
if [ -f $file ] ; then
    rm $file
fi

#unzip file
#remove the tsv header
#remove all double quotes
#remove all non utf8 char
#add line number for row ids
echo "processing tsv file..."
tmp_file="rm_header_quotes_tmp.tsv"
unzip -a -p $1 | tail -n +2 | awk '{gsub(/\"/,"")};1' | iconv -f utf-8 -t utf-8 -c | cat -n > $tmp_file

#import tsv file into a sqlite db
echo "loading tsv file..."
sqlite3 ./app/homework.db <<EOF
.mode csv
.separator \t
CREATE TABLE variant (
    id INTEGER,
    gene  TEXT,
    nucleotide_change  TEXT,
    protein_change  TEXT,
    other_mappings  TEXT,
    alias  TEXT,
    transcripts  TEXT,
    region  TEXT,
    reported_classification  TEXT,
    inferred_classification  TEXT,
    source  TEXT,
    last_evaluated  TEXT,
    last_updated  TEXT,
    url  TEXT,
    submitter  TEXT,
    assembly  TEXT,
    chr  TEXT,
    genomic_start  TEXT,
    genomic_stop  TEXT,
    ref  TEXT,
    alt  TEXT,
    accession  TEXT,
    reported_ref  TEXT,
    reported_alt  TEXT
);
.import $tmp_file variant
CREATE INDEX gene_idx ON variant(gene);
EOF

#delete the temp file
rm $tmp_file