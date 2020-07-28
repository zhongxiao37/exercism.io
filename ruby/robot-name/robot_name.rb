class Robot

  attr_reader :name

  def initialize
    @name = generate_new_name
  end

  def reset
    @name = generate_new_name
  end

  def self.forget
    @@assigned_names = Hash.new(0)
  end

  private

  def generate_new_name
    new_name = new_name_core
    new_name = new_name_core while @@assigned_names.key?(new_name)
    @@assigned_names[new_name] += 1
    new_name
  end

  def new_name_core
    rand(65..90).chr << rand(65..90).chr << rand(48..57).chr << rand(48..57).chr << rand(48..57).chr
  end

end

module BookKeeping
  VERSION = 3
end
