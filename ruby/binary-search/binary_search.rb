class BinarySearch
  attr_reader :list, :middle
  def initialize(list)
    raise ArgumentError if list.sort != list
    @list = list
    @middle = @list.size / 2
  end

  def search_for(ele)
    data = search_for_core(ele)
    raise RuntimeError if data.nil?
    data
  end

  private

  def search_for_core(ele)
    return @middle if ele == @list[@middle]
    return nil if @list.size == 1
    ele < @list[@middle] ? BinarySearch.new(@list[0..@middle-1]).search_for(ele)
                                     : @middle + BinarySearch.new(@list[@middle..-1]).search_for(ele)
  end

end
