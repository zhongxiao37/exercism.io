class Board
  attr_reader :board
  def initialize(board)
    @board = board.map { |e| e.scan(/\S/) }
    @row_cnt = @board.size
    @col_cnt = @board[0].size
  end

  # just check if the last slot of any path is on right/bottom, then win
  def winner
    return 'X' if calculate_path('X').map(&:path).any? { |slot| slot[-1][1] == (@col_cnt - 1) }
    return 'O' if calculate_path('O').map(&:path).any? { |slot| slot[-1][0] == (@row_cnt - 1) }
    ''
  end

  private

  # paths will hold all the possible paths
  # for each path, find all the adjacent slots for last slot
  # append the new slot to the path, or create a new path if more slots are found
  # until no more adjacent slots can be found
  def calculate_path(player)
    paths = start_slots(player).map { |slot| Path.new([slot]) }

    paths.each do |pth|

      while true
        last_slot = pth.path[-1]
        adjacent_slots = find_adjacent_slots(last_slot).select { |e| @board[e[0]][e[1]] == player } - pth.path

        break if adjacent_slots.empty?

        if adjacent_slots.size > 1
          # clone current path
          adjacent_slots[1..-1].each do |new_slot|
            new_path = Path.new(pth.path.clone)
            new_path.add(new_slot)
            paths << new_path
          end
        end

        # update current path
        pth.add(adjacent_slots[0])

      end
      # break if any path reaches the opposite
      break if pth.path[-1][0] == (@col_cnt - 1) || pth.path[-1][0] == (@row_cnt - 1)
    end

    paths
  end

  # find all the adjacent slots except slots from top-left to bottom-right
  def find_adjacent_slots(slot)
    [-1,0,1].product([-1,0,1])
            .select { |x,y| x != y }
            .map { |m, n| [slot[0]+m, slot[1]+n] }
            .select { |e| e[0] >= 0 && e[1] >= 0 && e[0] < @row_cnt && e[1] < @col_cnt }
  end

  # get the starting slots. X will starts from left, O will start from top
  # find all the mapping slots from left/top
  def start_slots(player)
    player == 'O' ? @board[0].map.with_index { |e, i| [e, i] }
                             .select { |e| e[0] == player }
                             .map { |e| [0, e[1]] }
                  : @board.map.with_index { |e, i| [e, i] }
                             .select { |e| e[0][0] == player }
                             .map { |e| [e[1], 0] }
  end


  class Path
    attr_accessor :path
    def initialize(path)
      @path = path
    end

    def add(slot)
      @path << slot
    end

  end

end

module BookKeeping
  VERSION = 2
end
