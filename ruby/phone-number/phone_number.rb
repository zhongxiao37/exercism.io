module PhoneNumber
  def self.clean(orig_phone_num)
    cleaned_phone = orig_phone_num.scan(/\d/)
    cleaned_phone = cleaned_phone[1..-1] if cleaned_phone[0] == '1'
    return nil if cleaned_phone[0].to_i < 2 || cleaned_phone[3].to_i < 2
    cleaned_phone = cleaned_phone.join
    return nil if cleaned_phone.length != 10
    cleaned_phone
  end
end


module BookKeeping
  VERSION = 2
end