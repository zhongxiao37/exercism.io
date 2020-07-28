require 'date'

class Meetup

  WEEKDAYS = {
    :monday => 1,
    :tuesday => 2,
    :wednesday => 3,
    :thursday => 4,
    :friday => 5,
    :saturday => 6,
    :sunday => 0
  }

  def initialize(month, year)
    @year = year
    @month = month
  end

  def first_wday(wday)
    (1..7).map { |e| Date.new(@year, @month, e) }.find { |e| e.wday == WEEKDAYS[wday] }
  end

  def weekdays(wday)
    (0..4).map { |e| first_wday(wday) + 7 * e }.reject { |e| e.month != @month }
  end

  def day(wday, schedule)
    case schedule
    when :teenth
      weekdays(wday).find { |e| e.day > 12 && e.day < 20 }
    when :first
      weekdays(wday)[0]
    when :second
      weekdays(wday)[1]
    when :third
      weekdays(wday)[2]
    when :fourth
      weekdays(wday)[3]
    when :last
      weekdays(wday)[-1]
    end
  end

end