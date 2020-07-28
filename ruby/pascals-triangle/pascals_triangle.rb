class Triangle
  attr_reader :rows
  def initialize(row_cnt)
    @rows = [[1]]
    populate_rows(row_cnt)
  end

  def populate_rows(row_cnt)
    (row_cnt-1).times do
      last_row = @rows.last.clone
      last_row.push 0
      last_row.unshift 0
      @rows << last_row.each_cons(2).map { |a, b| a + b }
    end
  end
end