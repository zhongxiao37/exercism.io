class InvalidCodonError < StandardError ; end

class Translation

  PROTEIN_CODONS = {
    "Methionine"    => ['AUG'],
    "Phenylalanine" => ['UUU', 'UUC'],
    "Leucine"       => ['UUA', 'UUG'],
    "Serine"        => ['UCU', 'UCC', 'UCA', 'UCG'],
    "Tyrosine"      => ['UAU', 'UAC'],
    "Cysteine"      => ['UGU', 'UGC'],
    "Tryptophan"    => ['UGG'],
    "STOP"          => ['UAA', 'UAG', 'UGA']
  }.freeze

  def self.of_codon(codon)
    protein = PROTEIN_CODONS.find { |k, v| v.include? codon }
    raise InvalidCodonError if protein.nil?
    protein[0]
  end

  def self.of_rna(rna)
    rna.scan(/\w{3}/)
       .map { |codon| Translation.of_codon(codon) }
       .take_while { |e| e != 'STOP' }
  end

end