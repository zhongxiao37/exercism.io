RNA_MAP = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}

def to_rna(dna_strand):
    return str.join('', map(lambda k: RNA_MAP[k], list(dna_strand)))

