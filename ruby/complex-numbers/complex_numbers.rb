class ComplexNumber
  include Comparable
  attr_reader :real, :imaginary

  def initialize(real, imaginary)
    @real = real
    @imaginary = imaginary
  end

  def *(other)
    self.class.new(@real * other.real - @imaginary * other.imaginary, @real * other.imaginary + @imaginary * other.real)
  end

  def /(other)
    real = (@real * other.real + @imaginary * other.imaginary) * 1.00 / (other.real ** 2 + other.imaginary ** 2)
    imaginary = (@imaginary * other.real - @real * other.imaginary) * 1.00 / (other.real ** 2 + other.imaginary ** 2)
    self.class.new(real, imaginary)
  end

  def +(other)
    self.class.new(@real + other.real, @imaginary + other.imaginary)
  end

  def -(other)
    self.class.new(@real - other.real, @imaginary - other.imaginary)
  end

  def <=>(other)
    (@real <=> other.real) && (@imaginary <=> other.imaginary)
  end

  def abs
    Math.sqrt(@real ** 2 + @imaginary ** 2)
  end

  def conjugate
    self.class.new(@real, -1 * @imaginary)
  end

  def exp
    if @imaginary == Math::PI
      real = Math::E ** @real * -1
      imaginary = Math::E ** @real * 0
      self.class.new(real, imaginary)
    elsif @imaginary == 0
      real = Math::E ** @real * 1
      imaginary = Math::E ** @real * 0
      self.class.new(real, imaginary)
    end
  end
end