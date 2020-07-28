class Nucleotide


  def initialize(input)
    raise ArgumentError unless input.scan(/[^ATCG]/).empty?
    @input = input
  end

  def self.from_dna(input)
    new(input)
  end

  def histogram
    hist_data = { 'A' => 0, 'T' => 0, 'C' => 0, 'G' => 0 }
    return hist_data if @input.empty?
    char_count = @input.chars.group_by {|w| w}.map {|k, v| [k, v.count]}
    Hash[char_count].each { |k, v| hist_data[k] = v }
    hist_data
  end

  def count(char)
    histogram[char]
  end

end
