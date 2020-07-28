class ListOps
  
  def self.arrays(array)
    cnt = 0
    array.each { |e| cnt += 1 }
    cnt
  end

  def self.reverser(array)
    data = []
    array.each { |e| data.unshift e }
    data
  end

  def self.concatter(*arrays)
    data = []
    arrays.each { |e| data += e }
    data
  end
  
  def self.mapper(array, &block)
    data = []
    array.each { |e| data << block.call(e) }
    data
  end

  def self.filterer(array, &block)
    data = []
    array.each { |e| data << e if block.call(e) }
    data
  end

  def self.sum_reducer(array)
    sum = 0
    array.each { |e| sum += e }
    sum
  end

  def self.factorial_reducer(array)
    sum = 1
    array.each { |e| sum *= e }
    sum
  end

  
end