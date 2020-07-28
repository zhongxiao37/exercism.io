
class Array
  def accumulate(&block)
    return self.to_enum(:each) unless block_given?

    result = []
    each do |element|
      result << yield(element)
    end
    result
  end
end

module BookKeeping
  VERSION = 1
end
