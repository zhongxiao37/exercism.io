class Diamond
  def self.make_diamond(char)
    characters = ('A'..char).to_a
    length = characters.size * 2 - 1

    data = []
    length.times do |n|
      char_index = n >= characters.size ? length - n - 1 : n
      data << (char_index == 0 ? characters[char_index]
                               : ( characters[char_index] + ' '*(char_index*2-1) + characters[char_index] )
              )
    end

    data.map { |e| space_wrapper(e, length) }.join("")
  end

  def self.space_wrapper(line, length)
    space_cnt = ( length - line.chars.size ) / 2
    ' ' * space_cnt + line + ' ' * space_cnt + "\n"
  end
end