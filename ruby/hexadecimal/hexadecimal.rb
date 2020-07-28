class Hexadecimal

  HEX_HASH = {
    '0' => 0,
    '1' => 1,
    '2' => 2,
    '3' => 3,
    '4' => 4,
    '5' => 5,
    '6' => 6,
    '7' => 7,
    '8' => 8,
    '9' => 9,
    'a' => 10,
    'b' => 11,
    'c' => 12,
    'd' => 13,
    'e' => 14,
    'f' => 15
  }

  def initialize(input)
    @input = input
  end

  def to_decimal
    return 0 unless @input.downcase.scan(/[^\dabcdef]/).empty?
    position_index = 0
    decimal_result = 0
    input_list = @input.chars
    until input_list.empty?
      ele = input_list.pop
      decimal_result += HEX_HASH[ele] * (16**position_index)
      position_index += 1
    end
    decimal_result
  end

end
