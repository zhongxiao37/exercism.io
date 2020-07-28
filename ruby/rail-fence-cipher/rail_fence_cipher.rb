module RailFenceCipher

  VERSION = 1

  class InvalidRailsNum < StandardError ; end

  def self.encode(input, num)
    raise InvalidRailsNum if num < 1
    return input if num == 1
    input_characters = input.chars
    result = arrange_characters_on_rails(input_characters, num)
    result.join
  end

  def self.decode(input, num)
    raise InvalidRailsNum if num < 1
    return input if num == 1
    input_characters = input.chars

    prefill_question_marks = arrange_characters_on_rails(('?'*input_characters.count).chars, num)

    filled_characters = []
    prefill_question_marks.each do |line|
      filled_characters << line.map { |e| e=='?' ? input_characters.shift : nil }
    end

    rail_index = 0
    direction = true
    decrypted_result = []
    input.chars.each_with_index do |v,i|
      decrypted_result << filled_characters[rail_index][i]
      rail_index += 1 if direction
      rail_index -= 1 if !direction
      direction = !direction if rail_index == 0 || rail_index == (num-1)
    end

    decrypted_result.join
  end

  private

  def self.arrange_characters_on_rails(input_characters, num)
    result = []
    num.times { |n| result << input_characters.map { |e| nil } }
    rail_index = 0
    direction = true
    input_characters.each_with_index do |v,i|
      # p [v,i,rail_index,direction]
      result[rail_index][i] = v
      rail_index += 1 if direction
      rail_index -= 1 if !direction
      direction = !direction if rail_index == 0 || rail_index == (num-1)
    end
    result
  end

end
