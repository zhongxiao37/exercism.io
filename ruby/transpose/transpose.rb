module Transpose
  def self.transpose(input)
    input_data = input.split("\n")
                      .map { |e| e.chars }
    length = input_data.map { |e| e.size }.max

    return "" if length.nil?

    ouput_data = []
    length.times { |col_index| ouput_data << input_data.map { |e| e[col_index].nil? ? '$' : e[col_index] }.join }
    p ouput_data
    ouput_data.map { |e| e.gsub(/\$+$/, '').gsub('$', ' ') }
              .join("\n")
  end
end

lines = [
            "The longest line.",
            "A long line.",
            "A longer line.",
            "A line."
        ]

p Transpose.transpose(lines.join("\n"))