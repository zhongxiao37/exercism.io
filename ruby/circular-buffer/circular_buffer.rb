class CircularBuffer

  class BufferEmptyException < StandardError ; end
  class BufferFullException < StandardError ; end

  def initialize(size)
    @size = size
    clear
  end

  def clear
    @data = Array.new(@size)
    @read_pt_index, @write_pt_index = 0, 0
  end

  def read
    raise BufferEmptyException if @data.compact.empty?
    data = @data[@read_pt_index]
    @data[@read_pt_index] = nil
    move_pt_index(:reader)
    data
  end

  def write!(element)
    write(element, true)
  end

  def write(element, override=false)
    # when data is not empty, reader pointer meets writer pointer and in non-overrride mode
    raise BufferFullException if !override && @read_pt_index == @write_pt_index && !@data.compact.empty?
    @data[@write_pt_index] = element
    # move reader pointer in override mode
    move_pt_index(:reader) if override && @read_pt_index == @write_pt_index
    move_pt_index(:writer)
    self
  end

  private

  def move_pt_index(pt_type)
    pt_type == :reader ? @read_pt_index = (@read_pt_index + 1) % @size
                       : @write_pt_index = (@write_pt_index + 1) % @size
  end

end