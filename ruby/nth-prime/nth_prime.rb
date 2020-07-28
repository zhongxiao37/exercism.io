module Prime
  def self.nth(index)
    raise ArgumentError if index == 0
    prime_list = [2]
    last_prime = prime_list[-1]
    while prime_list.count < index
      last_prime = last_prime + 1
      if last_prime % 2 == 0
        next
      elsif prime_list.any? { |e| last_prime % e == 0 }
        next
      else
        prime_list << last_prime
      end
    end

    prime_list[-1]
  end
end

module BookKeeping
    VERSION = 1
end



# module PrimeRefinements

#   refine Integer do
#     def prime?
#       return false if self < 2
#       return self == 2 if (self % 2).zero?
#       return self == 3 if (self % 3).zero?
#       return true if self < 9
#       5.step(Math.sqrt(self).floor, 2) do |num|
#         return false if (self % num).zero?
#       end
#       true
#     end
#   end

# end


# class Prime
#   include Enumerable
#   using PrimeRefinements

#   def self.nth(n)
#     raise ArgumentError if n < 1
#     new.take(n).last
#   end

#   def initialize
#     @last_prime = nil
#   end

#   def succ
#     if @last_prime.nil?
#       @last_prime = 2
#     else
#       num = @last_prime + 1
#       num += 1 if num.even?
#       num += 2 until num.prime?
#       @last_prime = num
#     end
#   end
#   alias next succ

#   def each
#     loop do
#       yield succ
#     end
#   end

# end

# module BookKeeping
#   VERSION = 1
# end
