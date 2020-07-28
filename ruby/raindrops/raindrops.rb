module Raindrops
  def self.convert(num)
    mapping_data = {'3'=>'Pling', '5'=>'Plang', '7'=>'Plong'}
    num_factors = (1..num).select { |e| num%e == 0 }.select { |t| mapping_data.keys.include? t.to_s }
    return num.to_s if num_factors.empty?
    num_factors.map { |e| mapping_data[e.to_s] }.join
  end
end

module BookKeeping
    VERSION = 3
end