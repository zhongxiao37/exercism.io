class RunLengthEncoding
  def self.encode(str)
    str.gsub(/(\D)\1+/) { $&.length.to_s + $1 }
  end

  def self.decode(str)
    str.gsub(/(\d+)(\D)/) { $2 * $1.to_i }
  end
end

module BookKeeping
  VERSION = 3
end