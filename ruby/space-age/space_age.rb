class SpaceAge

  def initialize(seconds)
    @seconds = seconds
  end

  def self.planets
    earth_obital_seconds = 31557600
    @planets = {earth: earth_obital_seconds,
      mercury: 0.2408467 * earth_obital_seconds,
      venus: 0.61519726 * earth_obital_seconds,
      mars: 1.8808158 * earth_obital_seconds,
      jupiter: 11.862615 * earth_obital_seconds,
      saturn: 29.447498 * earth_obital_seconds,
      uranus: 84.016846 * earth_obital_seconds,
      neptune: 164.79132 * earth_obital_seconds
    }
  end

  planets.each do |k, v|
    define_method :"on_#{k}" do
      (@seconds / v.to_f).round(2)
    end
  end

end

module BookKeeping
  VERSION = 1
end


