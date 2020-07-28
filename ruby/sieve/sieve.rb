class Sieve

  def initialize(limit)
    @limit = limit
  end

  def primes
    numbers = (2..@limit).to_a
    Array.new.tap do |primes|
      while numbers.any?
        current_prime = numbers.shift
        numbers.reject! {|x| x % current_prime == 0}
        primes << current_prime
      end
    end
  end
end

module BookKeeping
    VERSION = 1
end


require 'benchmark'

numbers = (2..100).to_a

p Benchmark.measure {
  50_000.times do
    Array.new.tap do |primes|
      while numbers.any?
        current_prime = numbers.shift
        numbers.reject! {|x| x % current_prime == 0}
        primes << current_prime
      end
    end
  end
}

numbers = (2..100).to_a

p Benchmark.measure {
  50_000.times do
    numbers.map do |current_prime|
      numbers.reject! { |x, i| x % current_prime == 0 and x != current_prime }
      current_prime
    end
  end
}

numbers = (2..100).to_a

p Benchmark.measure {
  50_000.times do
    @primes = []
    while numbers != []
      @primes.push(numbers[0])
      numbers = numbers.reject { |number| (number % numbers[0]).zero? }
    end
  end
}