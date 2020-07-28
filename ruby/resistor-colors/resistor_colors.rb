class ResistorColors

  RESISTOR_COLOR_VALUES = {
    black: 0,
    brown: 1,
    red: 2,
    orange: 3,
    yellow: 4,
    green: 5,
    blue: 6,
    violet: 7,
    grey: 8,
    white: 9
  }

  def self.value(colors)
    colors.map { |e| RESISTOR_COLOR_VALUES[e.to_sym] }.join.to_i
  end
end
