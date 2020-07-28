class Queens
  attr_reader :queens

  def initialize(*queens)
    @queens = queens.map { |queen| queen.map { |k, v| Queen.new(k, v) } }.flatten
  end

  def attack?
    @queens.each_slice(2).any? { |e| e[0].position[0] == e[1].position[0] || e[0].position[1] == e[1].position[1] || (e[0].position[0] - e[1].position[0]).abs == (e[0].position[1] - e[1].position[1]).abs }
  end

  class Queen
    attr_reader :name, :position
    def initialize(name, position)
      raise ArgumentError if position.any? { |e| e < 0 || e > 7 }
      @name = name
      @position = position
    end
  end

end

module BookKeeping
  VERSION = 2
end