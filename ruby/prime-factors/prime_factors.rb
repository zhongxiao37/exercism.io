module PrimeRefinements

  refine Integer do
    def prime?
      return false if self < 2
      return self == 2 if (self % 2).zero?
      return self == 3 if (self % 3).zero?
      return true if self < 9
      5.step(Math.sqrt(self).floor, 2) do |num|
        return false if (self % num).zero?
      end
      true
    end
  end

end

class PrimeFactors

  using PrimeRefinements

  def self.for(num)
    return [] if num < 2
    return [num] if num.prime?
    prime_factors = []
    last_prime = 2
    while last_prime <= Math.sqrt(num)
      if num % last_prime == 0
        prime_factors << last_prime
        num = num / last_prime
      else
        last_prime += 1
        last_prime += 1 if last_prime.even?
        last_prime += 1 until last_prime.prime?
      end
    end
    prime_factors << num
  end

end
