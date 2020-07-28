PROTEIN_CODONS = {
    "Methionine": ['AUG'],
    "Phenylalanine": ['UUU', 'UUC'],
    "Leucine": ['UUA', 'UUG'],
    "Serine": ['UCU', 'UCC', 'UCA', 'UCG'],
    "Tyrosine": ['UAU', 'UAC'],
    "Cysteine": ['UGU', 'UGC'],
    "Tryptophan": ['UGG'],
    "STOP": ['UAA', 'UAG', 'UGA']
  }


def proteins(strand):
    codons = []
    strand_len = len(strand)
    for i in range(0,strand_len,3):
        codon = of_codon(strand[i:min(strand_len, i+3)])
        if codon == 'STOP':
            break
        codons.append(codon)
    return codons

def of_codon(strand):
    codon = ''
    for k, v in PROTEIN_CODONS.items():
        if strand in v:
            codon = k
            break
    return codon
