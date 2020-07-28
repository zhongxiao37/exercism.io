class Game

  attr_reader :score_list

  class BowlingError < StandardError; end

  def initialize
    @score_list = []
  end

  def roll(pins)
    # a pins should between 0 to 10
    raise BowlingError if pins > 10 || pins < 0

    # split the pins for each frame, special case for 10th frame
    if @score_list.empty?
      @score_list << [*pins]
    elsif @score_list[-1].length < 2 && @score_list[-1].reduce(:+) < 10 #spare or open frame
      @score_list[-1] << pins
    elsif @score_list[-1].length == 2 || @score_list[-1].reduce(:+) == 10 #previous frame is finished
        @score_list << [*pins]
    end

    raise BowlingError if @score_list.any? { |e| e.reduce(:+) > 10 } #ignore the 10th frame
    #frame count would be 11 or 12 if 10th frame is a strike/spare
    raise BowlingError if @score_list.length > 10 && @score_list[9].reduce(:+) != 10

  end

  def score
    frame_scores = []
    score_list_dup = @score_list.dup

    # unfinished game could not be scored
    raise BowlingError if @score_list.length < 10

    # exactly check the bonus frame
    if score_list_dup[9].reduce(:+) == 10
      raise BowlingError if score_list_dup[10].nil? || score_list_dup[9..-1].flatten.count != 3
    end

    while frame_scores.count < 10
      current_frame = score_list_dup.shift
      if current_frame.reduce(:+) == 10
        if current_frame.count == 1
          # strike, add next two throws
          frame_scores << 10 + score_list_dup.flatten[0..1].reduce(:+)
        else
          # spare, add next one throw
          frame_scores << 10 + score_list_dup.flatten[0]
        end
      else
        frame_scores << current_frame.reduce(:+)
      end
    end

    frame_scores.reduce(:+)

  end

end


module BookKeeping
  VERSION = 3
end

