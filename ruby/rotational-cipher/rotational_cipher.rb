module RotationalCipher
  def self.rotate(plain_text, key)
    plain_text.tr('a-zA-Z', (('a'..'z').to_a[key..-1] +
                             ('a'..'z').to_a[0...key] +
                             ('A'..'Z').to_a[key..-1] +
                             ('A'..'Z').to_a[0...key]
                            ).join)
  end
end

module BookKeeping
  VERSION = 1
end