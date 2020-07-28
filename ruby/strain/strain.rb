class Array
  def keep(&block)
    return self.to_enum(:each) unless block_given?

    result = []
    each do |element|
      result << element if yield(element)
    end
    result
  end

  def discard(&block)
    return self.to_enum(:each) unless block_given?

    result = []
    each do |element|
      result << element if !yield(element)
    end
    result
  end
end

