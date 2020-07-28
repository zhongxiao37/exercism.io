module Complement
  def self.of_dna(input)
    input.chars.reduce('') { |sum, i| sum = sum + {'C'=>'G', 'G'=>'C', 'T'=>'A', 'A'=>'U'}[i] } rescue ''
  end
end

module BookKeeping
    VERSION = 4
end
