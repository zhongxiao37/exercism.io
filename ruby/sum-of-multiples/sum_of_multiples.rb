class SumOfMultiples
  attr_reader :init_nums, :smallest_init_num
  def initialize(*init_nums)
    @init_nums = [*init_nums]
    @smallest_init_num = @init_nums.min
  end

  def to(up_to_num)
    return 0 if @init_nums.empty? || up_to_num < @smallest_init_num
    (@smallest_init_num...up_to_num).select { |e| @init_nums.any? { |i| e % i == 0 } }.reduce(:+)
  end

end

module BookKeeping
  VERSION = 1
end