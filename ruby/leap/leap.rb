module Year
  def self.leap?(year)
    return year % 400 == 0 if year % 100 == 0
    return year % 4 == 0 if year % 100 != 0
    false
  end
end

module BookKeeping
  VERSION = 3
end