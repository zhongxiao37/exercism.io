module Brackets
  PAIRED_BRACKETS = {']'=>'[', '}'=>'{', ')'=>'('}

  def self.paired?(input)

    paired_stack = []
    return true if input.empty?

    input.each_char do |char|
      if PAIRED_BRACKETS.value?(char)
        paired_stack.push(char)
      elsif PAIRED_BRACKETS.key?(char)
        return false if paired_stack.last != PAIRED_BRACKETS[char]
        paired_stack.pop
      end
    end

    paired_stack.empty?
  end
end

module BookKeeping
  VERSION = 4
end