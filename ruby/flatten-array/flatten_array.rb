module FlattenArray
  VERSION = 1

  def self.flatten(arr)
    flatten_list = []
    arr.each do |e|
      next if e.nil?
      if e.class == Array
        flatten_list += FlattenArray.flatten(e)
      else
        flatten_list += [*e]
      end
    end
    flatten_list
  end
end