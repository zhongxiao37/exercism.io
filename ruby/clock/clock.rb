class Clock

  attr_accessor :hour, :minute
  def initialize(hour, minute)
    @hour = hour
    @minute = minute
  end

  def self.at(hour, minute)
    Clock.new(hour, minute)
  end

  def +(minute)
    self.minute = self.minute + minute
    self
  end

  def to_s
    "%02d:%02d" % exact_time
  end

  def ==(other_clock)
    self.exact_time == other_clock.exact_time
  end

  def exact_time
    hour = (@hour + @minute / 60) % 24
    hour = hour + 24 if hour < 0
    minute = ( @minute % 60 < 0 ? @minute % 60 + 60 : @minute % 60)
    return hour, minute
  end

end

module BookKeeping
  VERSION = 2
end