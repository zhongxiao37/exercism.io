module ETL
  def self.transform(old_data)
    new_data = {}
    old_data.each { |k, v| v.each { |e| new_data[e.downcase] = k } }
    new_data
  end
end

module BookKeeping
  VERSION = 1
end