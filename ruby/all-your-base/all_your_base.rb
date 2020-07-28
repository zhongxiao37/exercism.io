module BaseConverter
  def self.convert(input_base, digits, output_base)
    raise ArgumentError if input_base <= 1 || output_base <= 1
    raise ArgumentError if digits.any? { |e| e < 0 || e >= input_base }
    return digits if digits.empty?
    num = digits.reverse
                .map
                .with_index { |e, i| e * input_base ** i }
                .reduce(:+)
    data = []
    until num < output_base
      data << num % output_base
      num = num / output_base
    end
    data << num
    data.reverse
  end
end


p BaseConverter.convert(7, [0, 6, 0], 10)