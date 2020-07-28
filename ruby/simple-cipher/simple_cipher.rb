class Cipher
  attr_reader :key

  LETTERS = ('a'..'z').to_a

  def initialize(key = nil)
    raise ArgumentError if !key.nil? && key.empty?
    raise ArgumentError if !key.nil? && key.downcase.scan(/[a-z]/).join != key
    @key = key || new_key
  end

  def new_key
    100.times.reduce('') { |sum, n| sum << rand(97..122).chr }
  end

  def encode(plain_text)
    plain_text.chars.map.with_index do |e,i|
      ((LETTERS.index(e) + LETTERS.index(@key[i])) % 26 + 97).chr
    end.join
  end

  def decode(cipher_text)
    cipher_text.chars.map.with_index do |e,i|
      ((LETTERS.index(e) - LETTERS.index(@key[i])) % 26 + 97).chr
    end.join
  end

end
