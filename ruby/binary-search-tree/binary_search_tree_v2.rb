require 'ostruct'
require 'forwardable'

class Bst
  extend Forwardable

  attr_reader :data
  def_delegators :@branches, :left, :right

  def initialize(value)
    @data = value
    @branches = OpenStruct.new
  end

  def insert(value)
    if value <= @data
      insert_to_branch(:left, value)
    else
      insert_to_branch(:right, value)
    end
  end

  def each(&blk)
    return to_enum unless block_given?

    @branches.left&.each(&blk)
    blk.call(@data)
    @branches.right&.each(&blk)
  end

  private
  def insert_to_branch(side, value)
    if @branches[side]
      @branches[side].insert(value)
    else
      @branches[side] = Bst.new(value)
    end
  end
end

