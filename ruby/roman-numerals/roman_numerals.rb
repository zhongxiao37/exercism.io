class Fixnum
  def to_roman
    original_num = self
    roman_num_dict = {'M'=>1000, 'D'=>500, 'C'=>100, 'L'=>50, 'X'=>10, 'V'=>5, 'I'=>1}
    quotient_list = []
    formatted_quotient_list = []

    roman_num_dict.each do |k, v|
      quotient = (original_num / v)
      if quotient > 0
        quotient_list << k * quotient
        original_num = original_num - v * quotient
      end

    end

    while quotient_list.any?
      current_item = quotient_list.pop
      if current_item.chars.count > 3
        current_item_ = quotient_list.pop
        if !current_item_.nil?
          # for case IIII, if one item is found before IIII
          idx = roman_num_dict.keys.index(current_item[0])
          idx_ = roman_num_dict.keys.index(current_item_[0])

          if idx - idx_ > 1
            # for case IIII, if X is found before IIII, we need to change it to XIV
            ahead_key = roman_num_dict.keys[idx-1]
            quotient_list.push(current_item_)
          else
            # for case IIII, if V is found before IIII, we need to change it to IX
            ahead_key = roman_num_dict.keys[idx_-1]
          end
          formatted_quotient_list.unshift(ahead_key)
          formatted_quotient_list.unshift(current_item[0])
        else
          # for case IIII, if no item is found before IIII, we need to change it to IV
          idx = roman_num_dict.keys.index(current_item[0])
          ahead_key = roman_num_dict.keys[idx-1]
          formatted_quotient_list.unshift(ahead_key)
          formatted_quotient_list.unshift(current_item[0])
        end
      else
        formatted_quotient_list.unshift(current_item)
      end

    end

    formatted_quotient_list.join
  end
end

module BookKeeping
    VERSION = 2
end