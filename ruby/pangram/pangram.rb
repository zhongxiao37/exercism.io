module Pangram
  def self.pangram?(sentence)
    (('a'..'z').to_a - sentence.downcase.chars).empty?
  end
end

module BookKeeping
  VERSION = 4
end