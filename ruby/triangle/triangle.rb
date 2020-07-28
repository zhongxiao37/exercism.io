class Triangle
  attr_reader :invalid_triangle
  def initialize(sides)
    @sides = sides
    @invalid_triangle = invalid_triangle
  end

  def equilateral?
    return false if @invalid_triangle
    @sides[0] == @sides[1] ? @sides[0] == @sides[2] : false
  end

  def isosceles?
    return false if @invalid_triangle
    @sides[0] == @sides[1] || @sides[1] == @sides[2] || @sides[0] == @sides[2]
  end

  def scalene?
    return false if @invalid_triangle
    !isosceles?
  end

  private

  def invalid_triangle
    return true if @sides.any? { |e| e <= 0 }
    return true if @sides[0] + @sides[1] < @sides[2]
    (@sides[0] - @sides[1]).abs > @sides[2]
  end

end

module BookKeeping
  VERSION = 1
end