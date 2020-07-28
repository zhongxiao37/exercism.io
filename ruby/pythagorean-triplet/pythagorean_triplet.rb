class Triplet
  def initialize(*nums)
    raise ArguementError if nums.flatten.size != 3
    @nums = nums.flatten
  end

  def sum
    @nums.reduce(:+)
  end

  def product
    @nums.reduce(:*)
  end

  def pythagorean?
    @nums[0..1].inject(0) { |sum, ele| sum = sum + ele ** 2 } == @nums[2] ** 2
  end

  def self.where(max_factor:, min_factor: 1, sum: nil)
    triplets = (min_factor..max_factor).to_a.combination(3).map { |e| Triplet.new(e) }.select { |e| e.pythagorean? }
    return triplets.select { |e| e.sum == sum } if sum
    triplets
  end

end