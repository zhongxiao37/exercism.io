class Series
  def initialize(str)
    @str = str
  end

  def largest_product(num)
    return 1 if num == 0
    raise ArgumentError if num < 0 || num > @str.size || @str.empty? || !@str.scan(/\D/).empty?
    @str.chars.map { |e| e.to_i }.each_cons(num).map { |e| e.reduce(:*) }.max
  end

end

module BookKeeping
  VERSION = 3
end