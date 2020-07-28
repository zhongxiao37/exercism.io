module Binary
  def self.to_decimal(binary)
    raise ArgumentError if binary.chars.any? { |e| e != '0' && e != '1' }
    binary.chars.reverse.each_with_index.reduce(0) { |sum, (e, i)| sum + e.to_i * (2 ** i) }
  end
end

module BookKeeping
  VERSION = 3
end