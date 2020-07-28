module Alphametics
  def self.solve(input)
    words = input.scan(/\w+/)
    uniq_characters = words.join.chars.uniq
    answer_list = []
    (0..9).to_a.permutation(uniq_characters.size).each do |e|
      next if words.any? { |word| word.tr(uniq_characters.join, e.join(''))[0] == '0' }
      if instance_eval(input.tr(uniq_characters.join, e.join('')))
        answer_list = e
        break
      end
    end
    return {} if answer_list.empty?
    Hash[Hash[uniq_characters.zip answer_list].sort]
  end
end

module BookKeeping
  VERSION = 4
end

time = Time.now

input = 'SEND + MORE == MONEY'
p Alphametics.solve(input)

puts "#{Time.now - time}"