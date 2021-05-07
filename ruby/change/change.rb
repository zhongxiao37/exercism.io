class Change

 def self.generate(coins, amount, results = [])
    return [] if amount == 0

    coins.sort! { |a, b| a <=> b }

    optimal_change = Hash.new do |hash, key|

      if key < coins.min
        hash[key] = []
      elsif coins.include?(key)
        hash[key] = [key]
      else
        hash[key] = coins
            .reject { |coin| coin > key }
            .map { |coin| [coin] + hash[key - coin] }
            .reject { |change| change.inject(&:+) != key }
            .min { |a, b| a.size <=> b.size } || []
      end

      puts hash
      hash[key]
    end

    optimal_change[amount].empty? ? -1 : optimal_change[amount].sort
end


end

module BookKeeping
  VERSION = 2
end

# p Change.generate([2, 5, 10, 20, 50], 21)


coins = [2, 5, 10, 11]
amount = 20
m = [[]] + [nil] * amount
coins.size
     .times
     .to_a
     .product((1..amount).to_a)
     .each { |c, t|
       p [c, t]
       if coins[c] == t
         m[t] = [coins[c]]
       else
         (1..t - 1).select { |t2| coins[c] + t2 == t }.tap { |x| puts "select:    #{x}" }
                   .reject { |t2| m[t2].nil? }.tap { |x| puts "reject:    #{x}" }
                   .each { |t2|
                     m[t] = m[t2] + [coins[c]] if m[t].nil? || m[t2].size + 1 < m[t].size 
                   }
       end
       p m
     }
p m