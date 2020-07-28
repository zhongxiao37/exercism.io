module FoodChain
  def self.song
    food_chain = ['fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse']
    eaten_food_chain = []
    song = ''
    song_line_2 = [
      '',
      '',
      'How absurd to swallow a ',
      'Imagine that, to swallow a ',
      'What a hog, to swallow a ',
      'Just opened her throat and swallowed a ',
      'I don\'t know how she swallowed a '
    ]


    food_chain.each_with_index do |f, i|
      song << "I know an old lady who swallowed a #{f}.\n"
      song << "#{song_line_2[i]}#{f}!\n" if i > 1 && i + 1 < food_chain.size
      eaten_food_chain << f
      if i + 1 < food_chain.size
        song << remaining_song(eaten_food_chain, i)
      else
        song << "She's dead, of course!\n"
      end
    end

    song
  end

  private

  def self.remaining_song(eaten_food_chain, index)
    partial_song = []
    previouse_eaten_food = nil

    eaten_food_chain.each_with_index do |f, i|

      partial_song.unshift("She swallowed the #{f} to catch the #{previouse_eaten_food}#{i==2 ? '' : ".\n"}") if i > 1

      partial_song.unshift("#{eaten_food_chain.size > 2 ? ' that' : "It"} wriggled and jiggled and tickled inside her.\nShe swallowed the #{f} to catch the #{previouse_eaten_food}.\n") if i == 1

      partial_song << "I don't know why she swallowed the #{f}. Perhaps she'll die.\n" if i == 0

      previouse_eaten_food = f
    end

    partial_song << "\n"
    partial_song.join
  end
end

module BookKeeping
  VERSION = 2
end