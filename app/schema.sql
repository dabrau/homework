DROP TABLE IF EXISTS variant;

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