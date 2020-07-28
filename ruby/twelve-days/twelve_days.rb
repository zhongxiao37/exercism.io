class TwelveDays

  def self.song
    weekdays = %w(first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth)
    lyrics = []

    weekdays.each_with_index do |w, i|
      lyrics << lyric_for_line(w, i)
    end
    lyrics.join("\n")
  end

  def self.lyric_for_line(weekday, line_number)
    items = ["twelve Drummers Drumming", "eleven Pipers Piping", "ten Lords-a-Leaping", "nine Ladies Dancing", "eight Maids-a-Milking", "seven Swans-a-Swimming", "six Geese-a-Laying", "five Gold Rings", "four Calling Birds", "three French Hens", "two Turtle Doves", "a Partridge in a Pear Tree"].reverse

    lyric = ["On the #{weekday} day of Christmas my true love gave to me, "]
    current_line_items = items.select.with_index { |e, i| i <= line_number }
    current_line_items.reverse.each_with_index do |item, i|
      lyric << ( i + 1 == current_line_items.size ? (current_line_items.size > 1 ? "and " : '') + item + ".\n"
                                                  : item + ", " )
    end
    lyric.join
  end

end

module BookKeeping
  VERSION = 2
end