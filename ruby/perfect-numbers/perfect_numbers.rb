class PerfectNumber
  def self.classify(num)
    raise RuntimeError if num < 0
    factor_sum = PerfectNumber.parse_factors(num).reduce(:+)
    factor_sum > num ? 'abundant'
                     : (factor_sum < num ? 'deficient'
                                         : 'perfect'
                       )
  end

  private

  def self.parse_factors(num)
    sum = [1]
    (2..Math.sqrt(num)).select { |e| num % e == 0 }
               .each { |e| sum << e; sum << num/e }
    sum.uniq
  end
end

module BookKeeping
  VERSION = 1
end
