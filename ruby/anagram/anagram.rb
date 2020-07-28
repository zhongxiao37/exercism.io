class Anagram
  def initialize(src_str)
    @src_str = src_str
  end

  def match(candidates)
    candidates = candidates.reject { |e| e.downcase == @src_str.downcase }
    # # 1
    match_indexes = candidates.map { |e| e.downcase.chars.sort.join }.each_with_index.select { |v, i| v == @src_str.downcase.chars.sort.join }
    candidates.each_with_index.select { |e, i| match_indexes.map(&:last).include? i }.map(&:first)

    # # 2
    # result = []
    # candidates.each do |e|
    #   result << e if e.downcase.chars.sort.join == @src_str.downcase.chars.sort.join
    # end
    # result
  end

end

module BookKeeping
  VERSION = 2
end