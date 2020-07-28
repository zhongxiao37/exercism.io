module OcrNumbers
  OCR_NUMS = {
    " _ \n| |\n|_|\n   "=>"0",
    "   \n  |\n  |\n   "=>"1",
    " _ \n _|\n|_ \n   "=>"2",
    " _ \n _|\n _|\n   "=>"3",
    "   \n|_|\n  |\n   "=>"4",
    " _ \n|_ \n _|\n   "=>"5",
    " _ \n|_ \n|_|\n   "=>"6",
    " _ \n  |\n  |\n   "=>"7",
    " _ \n|_|\n|_|\n   "=>"8",
    " _ \n|_|\n _|\n   "=>"9"
  }

  def self.convert_core(ocr_numbers)
    ocr_numbers = ocr_numbers.map { |e| e.chars.each_slice(3).map { |t| t.join } }
    raise ArgumentError if ocr_numbers.size != 4
    raise ArgumentError if ocr_numbers.any? { |e| e.any? { |t| t.size != 3 } }
    # solution #1
    # numbers_arr = []
    # ocr_numbers[0].size.times { |n| numbers_arr << ocr_numbers.map { |e| e[n] }.join("\n") }
    # solution #2
    numbers_arr = ocr_numbers.transpose.map { |e| e.join("\n") }
    numbers_arr.map {|n| (OCR_NUMS.key?(n) ? OCR_NUMS[n] : '?')}.join
  end

  def self.convert(ocr_numbers)
    ocr_numbers.split("\n").each_slice(4).map { |r| convert_core(r) }.join(',')
  end

end

module BookKeeping
  VERSION = 1
end