class Proverb
  def initialize(*consequences, qualifier: nil)
    @qualifier = (qualifier.nil? ? '' : qualifier+' ') + [*consequences][0]
    @consequences = [*consequences]
  end

  def to_s
    to_string = ''
    @consequences.each_cons(2) do |a, b|
      to_string << "For want of a #{a} the #{b} was lost.\n"
    end
    to_string << "And all for the want of a #{@qualifier}."
  end

end