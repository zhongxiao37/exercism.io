class Deque

  attr_reader :first_node

  def push(element)
    new_node = Node.new(element)
    if @first_node.nil?
      @first_node = new_node
    else
      new_node.previous = @first_node.last
      new_node.previous.next = new_node
    end
  end

  def unshift(element)
    new_node = Node.new(element)
    if @first_node.nil?
      @first_node = new_node
    else
      new_node.next = @first_node
      new_node.next.previous = new_node
      @first_node = new_node
    end
  end


  def pop
    last_node = @first_node.last
    if @first_node.next.nil?
      @first_node = nil
    else
      # break relationships
      last_node.previous.next = nil
      last_node.previous = nil
    end
    last_node.value
  end

  def shift
    first_node = @first_node
    if @first_node.next.nil?
      @first_node = nil
    else
      # break relationships
      @first_node = first_node.next
      first_node.next.previous = nil
      first_node.next = nil
    end
    first_node.value
  end


  class Node
    attr_accessor :value, :next, :previous
    def initialize(value)
      @value = value
    end

    def last
      return self if @next.nil?
      pointer = @next
      pointer = pointer.next until pointer.next.nil?
      pointer
    end

  end
end
