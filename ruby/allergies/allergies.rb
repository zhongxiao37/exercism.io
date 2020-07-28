class Allergies

ALLERGIES = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']


  def initialize(allergies)
    @allergies = allergies
  end

  def allergic_to?(item)
    list.include? item
  end

  def list
    @list ||= @allergies.to_s(2).chars.reverse.map.with_index { |e, i| e == '1' ? ALLERGIES[i] : nil }.compact
  end

end