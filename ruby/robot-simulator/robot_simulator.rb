class Robot

  attr_reader :bearing, :coordinates
  DIRECTIONS = [:west, :north, :east, :south].freeze

  def orient(direction)
    raise ArgumentError unless DIRECTIONS.include? direction
    @bearing = direction
  end

  [:right, :left].each do |direction|
    define_method("turn_#{direction}") do
      @bearing = direction == :right ? DIRECTIONS[(DIRECTIONS.index(@bearing) + 1)%4]
                                     : DIRECTIONS[(DIRECTIONS.index(@bearing) - 1)%4]
    end
  end

  def at(x, y)
    @coordinates = [x, y]
  end

  def advance
    bearing_index = DIRECTIONS.index(@bearing)
    bearing_index.even? ? @coordinates[0] = @coordinates[0] + (bearing_index-1)
                        : @coordinates[1] = @coordinates[1] - (bearing_index-2)
  end

end

class Simulator

  INSTRUCTIONS = {
    'L' => :turn_left,
    'R' => :turn_right,
    'A' => :advance
  }.freeze

  def instructions(commands)
    commands.chars.map { |e| INSTRUCTIONS[e] }
  end

  def place(robot, x:, y:, direction:)
    robot.at(x, y)
    robot.orient(direction)
  end

  def evaluate(robot, commands)
    instructions(commands).each do |cmnd|
      robot.send(cmnd)
    end
  end

end