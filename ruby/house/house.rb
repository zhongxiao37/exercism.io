class House



  def self.recite

    suffix = ['horse and the hound and the horn',
      'farmer sowing his corn',
      'rooster that crowed in the morn',
      'priest all shaven and shorn',
      'man all tattered and torn',
      'maiden all forlorn',
      'cow with the crumpled horn',
      'dog',
      'cat',
      'rat',
      'malt',
      'house that Jack built'
    ]

    prefix = [
      'belonged to',
      'kept',
      'woke',
      'married',
      'kissed',
      'milked',
      'tossed',
      'worried',
      'killed',
      'ate',
      'lay in'
    ]

    recite = []

    suffix.reverse.each_with_index do |e, i|
      recite_ = []

      (i + 1).times do |t|
        prefix_ =  (t == i ? 'This is the ' : "that #{prefix.reverse[t]} the " )
        recite_.unshift(prefix_ + suffix.reverse[t] + (t == 0 ? '.' : '' ) + "\n")
      end

      recite << recite_.join
    end

    recite.join("\n")
  end
end