class Affine
  ALPHABET = ('a'..'z').to_a
  ALPHABET_LEN = 26

  def initialize(a, b)
    raise ArgumentError if a.gcd(ALPHABET_LEN) != 1
    @a = a
    @b = b
    @mmi = mmi
  end

  def encode(plaintext)
    plaintext.downcase
             .scan(/\w/)
             .map(&method(:encode_char))
             .each_slice(5)
             .map(&:join)
             .join(' ')
  end

  def decode(ciphertext)
    ciphertext.scan(/\w/)
              .map(&method(:decode_char))
              .join
  end


  private

  def encode_char(letter)
    x = ALPHABET.index(letter)
    return letter if x.nil?
    y = (@a*x + @b) % ALPHABET_LEN
    ALPHABET[y]
  end

  def decode_char(letter)
    y = ALPHABET.index(letter)
    return letter if y.nil?
    x = @mmi * (y - @b) % ALPHABET_LEN
    ALPHABET[x]
  end

  def mmi
    (1..ALPHABET_LEN).detect { |n| @a * n % ALPHABET_LEN == 1 }
  end

end