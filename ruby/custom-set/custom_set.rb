class CustomSet
  attr_reader :data
  def initialize(data)
    @data = data.sort
  end
  
  def empty?
    @data.empty?
  end

  def member?(ele)
    @data.include? ele
  end

  def add(ele)
    @data << ele unless @data.include? ele
    @data.sort!
    self
  end

  def subset?(another_set)
    (@data - another_set.data).empty?
  end

  def disjoint?(another_set)
    (@data & another_set.data).empty?
  end

  def intersection(another_set)
    @data = @data & another_set.data
    self
  end

  def difference(another_set)
    @data = @data - another_set.data
    self
  end

  def union(another_set)
    @data = (@data + another_set.data).uniq.sort
    self
  end

  def ==(another_set)
    @data == another_set.data
  end

  def <=>(another_set)
    @data <=> another_set.data
  end
end

module BookKeeping
  VERSION = 1
end