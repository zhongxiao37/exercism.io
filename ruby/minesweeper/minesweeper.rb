class ValueError < StandardError ; end

class Board

  def self.transform(inp)
    @input = inp.map { |e| e.chars }
    @height = inp.size
    @length = @input[0].size

    raise ValueError if @input.any? { |e| e.size != @length }
    raise ValueError unless @input[1..-2].map { |e| e[1..-2] }.flatten.all? { |e| [' ', '*'].include? e }
    raise ValueError if @input[1..-2].any? { |e| e[0] != '|' || e[-1] != '|' }
    raise ValueError if @input[0].join.scan(/^\+\-+\+$/).empty? || @input[-1].join.scan(/^\+\-+\+$/).empty?

    @input.each_with_index do |r, h|
      r.each_with_index do |c, l|
        if c == ' '
          cnt = get_mine_count(h, l)
          @input[h][l] = cnt if cnt > 0
        end
      end
    end

    @input.map { |e| e.join }
  end

  def self.get_mine_count(h, l)
    min_h = [0, h-1].max
    max_h = [@height, h+1].min
    min_l = [0, l-1].max
    max_l = [@length, l+1].min

    cnt = 0
    (min_h..max_h).each do |m|
      (min_l..max_l).each do |n|
        cnt += 1 if @input[m][n] == '*'
      end
    end

    cnt
  end

end