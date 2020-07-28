class Squares
  def initialize(args)
    @num = args
  end

  def square_of_sum
    (1..@num).to_a.reduce(:+)**2
  end

  def sum_of_squares
     (1..@num).reduce(0) { |sum, e| sum + e*e }
  end

  def difference
    square_of_sum - sum_of_squares
  end
end

module BookKeeping
    VERSION = 4
end