class Phrase
  def initialize(str)
    @str = str
  end
  
  def word_count
    count_hash = Hash.new(0)
    @str.scan(/[\d\w]+(?:'?[\w\d]+)?/).each do |e|
      count_hash[e.downcase] += 1
    end
    count_hash
  end

end

module BookKeeping
  VERSION = 1
end
