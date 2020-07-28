class Zipper
  include Comparable

  def initialize(root_tree)
    @root_tree = root_tree
    @current_node = @root_tree
    @parents = []
  end

  def to_tree
    @root_tree
  end

  def left
    @parents << @current_node
    @current_node = @current_node.left
    @current_node.nil? ? nil : self
  end

  def right
    @parents << @current_node
    @current_node = @current_node.right
    @current_node.nil? ? nil : self
  end

  def up
    return nil if @parents.empty?
    @current_node = @parents.pop
    self
  end

  def value
    @current_node.value
  end

  def set_value(value)
    @current_node.value = value
    self
  end

  def set_left(left)
    @current_node.left = left
    self
  end

  def set_right(right)
    @current_node.right = right
    self
  end

  def <=>(other)
    to_tree <=> other.to_tree
  end

  def self.from_tree(nodes)
    self.new(nodes)
  end
end

class Node
  include Comparable

  attr_accessor :value, :left, :right

  def initialize(value, left, right)
    @value = value
    @left = left
    @right = right
  end

  def <=>(other)
    @value <=> other.value
  end
end