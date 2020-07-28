module Acronym
  def self.abbreviate(input)
    input.scan(/\w+/).map { |e| e[0].upcase }.join
  end
end

module BookKeeping
  VERSION = 4
end