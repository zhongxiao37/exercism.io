module PigLatin


  def self.translate_core(word)
    vowel_characters = ['a', 'e', 'i', 'o', 'u', 'yt', 'xr']
    consonant_characters = ['qu', 'ch', 'thr', 'th', 'squ', 'sch']

    vowel_word = vowel_characters.map { |e| word.scan(/^(#{e})(.*)/) }
                                  .reject { |t| t.empty? }
                                  .flatten
    return vowel_word.join+'ay' unless vowel_word.empty?

    consonant_word = consonant_characters.map { |e| word.scan(/^(#{e})(.*)/) }
                                          .reject { |t| t.empty? }.first
                                          .flatten rescue []
    return consonant_word.reverse.join + 'ay' unless consonant_word.empty?

    word.scan(/^(.)(.*)/).flatten.reverse.join+'ay'
  end

  def self.translate(words)
    words.split(" ").map { |e| translate_core(e) }.join(' ')
  end

end

module BookKeeping
  VERSION = 1
end