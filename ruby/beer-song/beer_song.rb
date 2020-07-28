class BeerSong

  def verse(*nums)
    @num_range = ([*nums].min .. [*nums].max)
    @num_range.to_a.reverse.map { |e| generate_bottle_lyric_for_line(e) }.join("\n")
  end

  alias verses verse

  def generate_bottle_lyric_for_line(line_index)
    return "#{line_index} bottles of beer on the wall, #{line_index} bottles of beer.\nTake one down and pass it around, #{line_index-1} bottles of beer on the wall.\n" if line_index > 2
    return "#{line_index} bottles of beer on the wall, #{line_index} bottles of beer.\nTake one down and pass it around, #{line_index-1} bottle of beer on the wall.\n" if line_index == 2
    return "1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n" if line_index == 1
    return "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n"
  end


end

module BookKeeping
  VERSION = 3
end