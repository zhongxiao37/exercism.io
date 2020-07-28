class Isogram
  def self.isogram?(string)
    characters = string.downcase.scan(/\w/)
    characters.size == characters.uniq.size
  end
end