class SecretHandshake
  ANSWER_LIST = ['wink', 'double blink', 'close your eyes', 'jump']
  def initialize(input)
    @input = input
  end

  def commands
    answers = []
    answer_indexes = @input.to_s(2).chars.reverse.map.with_index { |e, i| e == '1' ? i : nil }.compact rescue nil
    return answers if answer_indexes.nil?
    answer_indexes = answer_indexes.reverse if answer_indexes[-1] == 4
    answer_indexes.each { |e| answers << ANSWER_LIST[e] }
    answers.compact
  end

end
