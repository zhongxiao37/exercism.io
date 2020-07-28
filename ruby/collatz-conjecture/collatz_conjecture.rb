class CollatzConjecture
  def self.steps(num)
    raise ArgumentError if num <= 0
    step_counter = 0

    while true
      break if num == 1
      num = num.odd? ? num * 3 + 1 : num / 2
      step_counter += 1
    end

    step_counter
  end

end