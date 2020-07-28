class Garden
  DEFAULT_STUDENTS = %w(alice bob charlie david eve fred ginny harriet ileana joseph kincaid larry)

  PLANTS = {
    'R' => :radishes,
    'C' => :clover,
    'G' => :grass,
    'V' => :violets
  }

  def initialize(plants, students=DEFAULT_STUDENTS)
    @plants = plants
    @students = students.sort
    distribute_plants
  end

  def distribute_plants
    # 将两行plants拆分成每两个一组，并对每个plant进行映射转换('R'=>:radishes)
    plants_grouped = @plants.split("\n")
                            .map { |r| r.chars #每一行plants
                                        .each_slice(2) #每两个一组
                                        .map { |plants|
                                          plants.map { |plant| PLANTS[plant] } #每个plant转换一次
                                            }
                                          }
    # 给每个student分配plants
    @students.each_with_index do |s, i|
      break if plants_grouped.first.size < i + 1 # plants不够，就不再分配给student了
      #创建singleton method，因为每个garden对应的plants分配是不一样的。define_method是对整个Class创建实例方法
      define_singleton_method(s.downcase) do
        plants_grouped.map { |e| e[i] }.flatten # 通过索引i，找到student对应的那组plant
      end
    end
  end

end