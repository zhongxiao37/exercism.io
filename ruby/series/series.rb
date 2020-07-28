class Series
  attr_reader :str
  def initialize(str)
    @str = str
  end

  def slices(num)
    raise ArgumentError if num > @str.length
    @str.chars.each_cons(num).reduce([]) { |sum, e| sum << e.join }
  end

end
