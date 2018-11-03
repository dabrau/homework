#!/bin/bash

file="homework.db"

#remove the database if it already exists
if [ -f $file ] ; then
    rm $file
fi

#remove the tsv header
#remove all double quotes
#remove all non utf8 char
#add line number for row ids
tmp_file="rm_header_quotes_tmp.tsv"
tail -n +2 $1 | awk '{gsub(/\"/,"")};1' | iconv -f utf-8 -t utf-8 -c | cat -n > $tmp_file

#import tsv file into a sqlite db
sqlite3 homework.db <<EOF
.mode csv
.separator \t
CREATE TABLE variant (
    id INTEGER,
    gene  TEXT,
    nucleotide_change  TEXT,
    protien_change  TEXT,
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
    Chr  TEXT,
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