class Matrix
  attr_reader :matrix
  def initialize(matrix_text)
    @matrix = matrix_text.split("\n").map { |e| e.split(' ').map { |k| k.to_i } }
  end

  def rows
    @matrix
  end

  def columns
    @columns ||= rows.transpose
  end

end