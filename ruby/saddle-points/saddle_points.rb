class Matrix

  def initialize(matrix_text)
    @matrix = matrix_text.split("\n").map { |e| e.split(' ').map { |k| k.to_i } }
  end

  def rows
    @matrix
  end

  def columns
    @matrix[0].map.with_index { |e, i| @matrix.map { |r| r[i] } }
  end

  def saddle_points
    max_index_per_row = []
    min_index_per_col = []
    rows.each_with_index { |row, i| row.map.with_index { |c, k| c == row.max ? k : nil }.compact.each { |m| max_index_per_row << [i, m] } }
    columns.each_with_index { |col, i| col.map.with_index { |c, k| c == col.min ? k : nil }.compact.each { |m| min_index_per_col << [m, i] } }

    max_index_per_row & min_index_per_col

  end

end