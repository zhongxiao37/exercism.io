module Grains
  # from the pattern like
  # index number
  # 1     1
  # 2     2
  # 3     4
  # 4     8
  # ...
  # for index i, the number should be 2 ** (i - 1)
  def self.square(square_index)
    raise ArgumentError if square_index > 64 or square_index < 1
    2 ** (square_index - 1)
  end


  # if total = K, then total * 2 = K * 2
  # then 2K - K = K = (the last element of 2K) - (the first element of K)
  # then K = 2 * (2 ** 63) - 1
  def self.total
    2 ** 64 - 1
  end
end

module BookKeeping
  VERSION = 1
end