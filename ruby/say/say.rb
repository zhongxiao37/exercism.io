class Say
  NUM = {
    0 => 'zero',
    1 => 'one',
    2 => 'two',
    3 => 'three',
    4 => 'four',
    5 => 'five',
    6 => 'six',
    7 => 'seven',
    8 => 'eight',
    9 => 'nine',
    10 => 'ten',
    11 => 'eleven',
    12 => 'twelve',
    13 => 'thirteen',
    14 => 'fourteen',
    15 => 'fifteen',
    16 => 'sixteen',
    17 => 'seventeen',
    18 => 'eighteen',
    19 => 'nineteen',
    20 => 'twenty',
    30 => 'thirty',
    40 => 'forty',
    50 => 'fifty',
    60 => 'sixty',
    70 => 'seventy',
    80 => 'eighty',
    90 => 'ninety',
    100 => 'hundred',
    1000 => 'thousand',
    1_000_000 => 'million',
    1_000_000_000 => 'billion'
  }

  def initialize(num)
    @num = num
  end

  def in_english
    raise ArgumentError if @num < 0 || @num > 999_999_999_999
    return NUM[@num] if @num == 0
    num_list = @num.to_s.chars
    # sections for every 3 numbers, e.g. sections for 987,654,321 are 2, 1, 0
    section_index = 0
    num_list_in_english = []
    until num_list.empty?
      three_eles_in_english = []
      three_eles = num_list.pop(3).join.to_i
      hundred_num = three_eles / 100
      under_hundred_num = three_eles % 100

      three_eles_in_english.push(NUM[hundred_num] + ' hundred') if hundred_num > 0
      three_eles_in_english.push(say_under_hundred_num(under_hundred_num)) if under_hundred_num > 0

      num_list_in_english.unshift NUM[1000**section_index] if section_index > 0 && three_eles > 0
      num_list_in_english.unshift three_eles_in_english
      section_index += 1
    end
    num_list_in_english.flatten.join(' ')
  end

  def say_under_hundred_num(under_hundred_num)
    return NUM[under_hundred_num]  unless NUM[under_hundred_num].nil?
    (under_hundred_num / 10 == 0 ? '' : NUM[under_hundred_num / 10 * 10]) + '-' +
    (under_hundred_num % 10 == 0 ? '' : NUM[under_hundred_num % 10])
  end

end

module BookKeeping
  VERSION = 1
end



