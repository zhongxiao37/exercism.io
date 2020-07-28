class Palindromes

  def initialize(factor_range)
    @min_factor = factor_range[:min_factor] || 1
    @max_factor = factor_range[:max_factor]
  end

  def generate
    return self unless @palindrome_products.nil?
    @palindrome_products = []
    (@min_factor..@max_factor).to_a.repeated_permutation(2).each do |a, b|
      if is_palindrome(a*b)
        existing_palindrome = @palindrome_products.find { |e| e.value == a*b } rescue nil
        existing_palindrome.nil? ? @palindrome_products << PalindromeProduct.new(a*b, [[a,b]]) : existing_palindrome.factors << [a,b]
      end
    end
    return self
  end

  def largest
    @palindrome_products.find { |e| e.value == @palindrome_products.map(&:value).max }
  end

  def smallest
    @palindrome_products.find { |e| e.value == @palindrome_products.map(&:value).min }
  end

  class PalindromeProduct
    attr_reader :value, :factors
    def initialize(value, factors)
      @value = value
      @factors = factors
    end
  end

  private
  def is_palindrome(num)
    num.to_s.reverse.to_i == num
  end
end