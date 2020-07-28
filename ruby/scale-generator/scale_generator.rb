class Scale

  CHROMATIC_SHARPS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'].freeze
  CHROMATIC_FLATS = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'].freeze

  def initialize(tonic, scale, pattern=nil)
    @tonic = tonic
    @scale = scale
    @pattern = pattern
  end

  def name
    "#{@tonic.upcase} #{@scale.to_s}"
  end

  def pitches
    if use_flat
      tonic_index = CHROMATIC_FLATS.index(@tonic.capitalize)
      raw_pitches = CHROMATIC_FLATS[tonic_index..-1] + CHROMATIC_FLATS[0..(tonic_index-1)]
    else
      tonic_index = CHROMATIC_SHARPS.index(@tonic.capitalize)
      raw_pitches = CHROMATIC_SHARPS[tonic_index..-1] + CHROMATIC_SHARPS[0..(tonic_index-1)]
    end

    if @pattern
      offset = 0
      pitches_ = []
      @pattern.chars.each do |patt|
        pitches_ << raw_pitches[offset]
        offset += ( patt == 'M' ? 2 : ( patt == 'A' ? 3 : 1 ) )
      end

      return pitches_
    end

    raw_pitches
  end

  def use_flat
    # ['G', 'D', 'A', 'E', 'B', 'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#'].freeze
    @use_flat ||= ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb'].include? @tonic
  end

end

module BookKeeping
  VERSION = 1
end

# major = Scale.new('G', :enigma, 'mAMMMmM')
# p major.pitches
# minor = Scale.new('bb', :minor, 'MmMMmMM')
# p minor.pitches
