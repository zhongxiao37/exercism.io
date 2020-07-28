class Scrabble

  SCORE_LIST = ['AEIOULNRSTDGBCMPFHVWYKJX', '111111111122333344444588']

  def initialize(input)
    @input = input
  end
  
  def score
    return 0 if @input.nil?
    return 0 if @input.scan(/\w/).empty?
    instance_eval(@input.scan(/\w/).map { |e| e.upcase }.join('+').tr(SCORE_LIST[0], SCORE_LIST[1]).gsub(/[QZ]/, '10'))
  end

  def self.score(input)
    new(input).score
  end
  
end