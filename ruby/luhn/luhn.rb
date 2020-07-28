module Luhn
  def self.valid?(str)
    numbers = str.scan(/\d/)
    return false if str.scan(/\D/).any? { |e| e != ' ' }
    return false if numbers.size <= 1

    numbers.reverse.map.with_index do |e, i|
      doubling_num = e.to_i * 2
      i.odd? ? (doubling_num > 9 ? doubling_num - 9 : doubling_num) : e.to_i
    end.reduce(:+) % 10 == 0

  end
end

module BookKeeping
  VERSION = 1
end