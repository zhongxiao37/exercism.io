class WordProblem

  OPERATIONS = {
    'plus' => '+',
    'minus' => '-',
    'multiplied by' => '*',
    'divided by' => '/'
  }

  def initialize(question)
    @question = question
  end

  def answer
    question_words = @question.scan(/-?\d+.*-?\d+/).join.split(' ')
    raise ArgumentError if question_words.size < 3
    answer = []
    while question_words.size > 0
      operation = []
      curr_ele = question_words.shift
      if curr_ele =~ /-?\d+/
        answer << curr_ele
      else
        operation << curr_ele
        operation << question_words.shift until question_words[0] =~ /-?\d+/
        raise ArgumentError if OPERATIONS[operation.join(' ')].nil?
        answer << OPERATIONS[operation.join(' ')]
      end

      # calculate every 3 elements
      if answer.size == 3
        answer = [instance_eval(answer.join(' '))]
      end
    end
    answer[0]
  end

end

module BookKeeping
  VERSION = 1
end