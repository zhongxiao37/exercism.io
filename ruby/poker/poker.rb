class Poker

  RANKING_CATEGORIES = {
    :straight_flush => 9,
    :square => 8,
    :full => 7,
    :flush => 6,
    :straight => 5,
    :three => 4,
    :two_pairs => 3,
    :one_pair => 2,
    :high_card => 1
  }

  CARD_RANKING = {
    '1' => 1,
    '2' => 2,
    '3' => 3,
    '4' => 4,
    '5' => 5,
    '6' => 6,
    '7' => 7,
    '8' => 8,
    '9' => 9,
    '10' => 10,
    'J' => 11,
    'Q' => 12,
    'K' => 13,
    'A' => 14
  }

  def initialize(hands)
    @hands = hands.map { |e| Hand.new(e).tap(&:hand_nubmer_groups) }
  end

  def best_hand
    largest_rank_hands = @hands.group_by { |e| e.rank }.sort.last.last #get the largest rank hands
    return largest_rank_hands.map(&:hand) if largest_rank_hands.size == 1
    largest_rank_hands.group_by { |e| e.point }.sort.last.last.map(&:hand)
  end


  class Hand
    attr_reader :hand
    def initialize(hand)
      @hand = hand
    end

    # 找出最高的rank，比如同花顺，既是同花，又是顺子，但只能够取最高rank的，即同花顺
    def rank
      RANKING_CATEGORIES.map { |k, v| self.send(:"#{k}?") ? v : 0 }.max
    end

    # 根据不同牌型，返回对应的点数以便后面比点。比如，四条就会返回是4张相同牌的数字，三条/葫芦就会范围3张相同牌的点数
    # 两对的时候，就需要将点数顺序颠倒一次，大的放到前面
    # 顺子就返回最小的那个点，因为‘A2345'是小于'910JQK'
    # 同花或者散牌，就直接将点数顺序颠倒，在比点
    def point
      return hand_nubmer_groups.find { |k, v| v.size == 4 }.first if square? # #find will convert Hash to Array
      return hand_nubmer_groups.find { |k, v| v.size == 3 }.first if three? || full?
      return hand_nubmer_groups.select { |k, v| v.size == 2 }.keys.reverse if two_pairs? || one_pair?
      return hand_nubmers.min if straight? # straight, compare the lowest number to avoid 'A2345' > '910JQK'
      hand_nubmers.reverse # flush or high card, compare the points from high to low
    end

    # e[0..-2]是为了避免'10S'这种情况
    def hand_nubmers
      @hand_nubmers ||= @hand.map { |e| CARD_RANKING[e[0..-2]] }.sort
    end

    # 将手里的牌进行分组，相同点数的分到一组，方便统计是否为对子/三条/四条
    def hand_nubmer_groups
      @hand_nubmer_groups ||= hand_nubmers.group_by { |i| i }
    end

    def straight_flush?
      straight? && flush?
    end

    def flush?
      @hand.map { |e| e[-1] }.uniq.size == 1
    end

    def straight?
      all_5_different_values? && ((hand_nubmers.max - hand_nubmers.min == 4) || ( hand_nubmers == [2,3,4,5,14] ))
    end

    def square?
      hand_nubmer_groups.any? { |k, v| v.size == 4 }
    end

    def full?
      hand_nubmer_groups.any? { |k, v| v.size == 3 } && hand_nubmer_groups.any? { |k, v| v.size == 2 }
    end

    def three?
      hand_nubmer_groups.any? { |k, v| v.size == 3 } && hand_nubmer_groups.keys.size == 3
    end

    def two_pairs?
      hand_nubmer_groups.any? { |k, v| v.size == 2 } && hand_nubmer_groups.keys.size == 3
    end

    def one_pair?
      hand_nubmer_groups.keys.size == 4
    end

    def high_card?
      all_5_different_values? && !straight?
    end

    def all_5_different_values?
      hand_nubmers.uniq.size == 5
    end

  end

end

module BookKeeping
  VERSION = 2
end
