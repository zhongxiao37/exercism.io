class Trinary
  def initialize(trinary_str)
    @trinary_str = trinary_str
  end

  def to_decimal
    return 0 if @trinary_str.chars.any? { |e| e != '0' && e != '1' && e!= '2' }
    @trinary_str.chars.reverse.each_with_index.reduce(0) { |sum, (e, i)| sum + e.to_i * (3 ** i) }
  end

end


module BookKeeping
  VERSION = 1
end
