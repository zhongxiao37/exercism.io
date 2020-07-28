class Dominoes
  def self.chain(input_dominoes)
    return input_dominoes if input_dominoes.empty?
    return nil if input_dominoes.flatten
                  .group_by { |e| e }
                  .any? { |k, v| v.size % 2 != 0 }

    first_domino = input_dominoes[0]
    chains = [] << Chain.new([first_domino], input_dominoes[1..-1])

    # `chains` holds all the possible chains
    # for each chain
    # if more possible chains are found, they will be added to `chains`
    # meanwhile, maintain the remaining dominoes for next pick up
    # break if no more candidate or remaining is empty
    chains.each do |chn|
      until chn.remaining_dominoes.empty?
        last_ele = chn.chain.last.last
        candidate_eles = chn.remaining_dominoes.map.with_index { |e, i| [e, i] }
                            .select { |e| e[0].include? last_ele }

        break if candidate_eles.empty?

        if candidate_eles.size > 1
          # more than one possibles
          candidate_eles[1..-1].each do |cand|

            new_remaining_dominoes = chn.remaining_dominoes.clone

            new_remaining_dominoes.delete_at(cand[1])

            chains << Chain.new(chn.chain.clone << (cand[0].last == last_ele ? cand[0].reverse : cand[0]), new_remaining_dominoes)
          end
        end

        chn.remaining_dominoes.delete_at(candidate_eles[0][1])
        chn.chain << ( candidate_eles[0][0].last == last_ele ? candidate_eles[0][0].reverse : candidate_eles[0][0] )

      end
    end

    chains.find { |e| e.remaining_dominoes.empty? }.chain rescue nil
  end

  class Chain
    attr_accessor :chain, :remaining_dominoes
    def initialize(chain, remaining_dominoes)
      @chain = chain
      @remaining_dominoes = remaining_dominoes
    end

  end
end

