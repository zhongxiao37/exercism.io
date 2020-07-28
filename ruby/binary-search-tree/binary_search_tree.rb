class Bst

  include Enumerable

  attr_reader :left, :right, :data

  def initialize(new_data)
    @data = new_data
  end

  def insert(new_data)
    if new_data <= @data
      @left ? @left.insert(new_data) : @left = Bst.new(new_data)
    else
      @right ? @right.insert(new_data) : @right = Bst.new(new_data)
    end
    self
  end

  def each(&block)
    return to_enum unless block_given?

    @left&.each(&block)
    yield @data
    @right&.each(&block)

    self
  end

  def <=>(other)
    @data <=> other.data
  end

  def predecessor(key)
    self.each_cons(2).select { |e| e.last == key }.map(&:first)[0]
  end

  def successor(key)
    self.each_cons(2).select { |e| e.first == key }.map(&:last)[0]
  end

end

module BookKeeping
  VERSION = 1
end


