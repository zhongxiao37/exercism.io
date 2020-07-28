module Bob
  def self.hey(str)
    response_list = ['Whoa, chill out!', 'Sure.', 'Fine. Be that way!', 'Whatever.']
    str.strip!
    str = str.split("\n").join(" ")

    all_upcase_list = str.scan(/[a-zA-Z]+/)
    return response_list[2] if str.empty?
    return response_list[0] if !all_upcase_list.empty? && all_upcase_list.all? { |e| e == e.upcase rescue false }
    return response_list[1] if !str.scan(/.*\?$/m).empty?

    response_list[3]
  end
end

module BookKeeping
  VERSION = 1
end
