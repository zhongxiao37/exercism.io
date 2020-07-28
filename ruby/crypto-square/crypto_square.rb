class Crypto

  attr_reader :normalize_plaintext

  class InvalidColAndRow < StandardError ; end

  def initialize(orig_text)
    @orig_text = orig_text
    @normalize_plaintext = orig_text.scan(/\w/).join.downcase
  end

  def size
    text_length = @normalize_plaintext.length
    cols = Math.sqrt(text_length).ceil
    @rows = text_length / cols
    @rows = @rows + 1 if @rows * cols <= text_length
    raise InvalidColAndRow if cols - @rows > 1
    cols
  end

  def plaintext_segments
    @normalize_plaintext.chars.each_slice(size).reduce([]) {|sum, e| sum << e.join}
  end

  def ciphertext
    ciphertext_ = []
    size.times { |n| ciphertext_ = ciphertext_ + plaintext_segments.map { |e| e.chars[n] } }
    ciphertext_.join
  end

  def normalize_ciphertext
    normalize_ciphertext_ = []
    size.times { |n| normalize_ciphertext_ << plaintext_segments.map { |e| e.chars[n].nil? ? ' ' : e.chars[n] }.join.strip }
    normalize_ciphertext_.join(' ').strip
  end

end
