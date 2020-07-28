module Atbash

  REVERSED_LETTERS = ('a'..'z').to_a.reverse.join

  def self.encode(plain_text)
    plain_text.downcase.scan(/\w/).join.tr('a-z', REVERSED_LETTERS).scan(/\w{1,5}/).join(' ')
  end

end