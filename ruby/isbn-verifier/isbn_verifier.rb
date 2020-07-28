class IsbnVerifier
  def self.valid?(isbn)
    scanned_isbn = isbn.scan(/[\dX]/)
    return false if scanned_isbn.size != 10
    if scanned_isbn.last == 'X'
      return false unless scanned_isbn[0..-2].join =~ /\A\d+\z/
    else
      return false unless scanned_isbn[0..-1].join =~ /\A\d+\z/
    end
    scanned_isbn.map { |e| e == 'X' ? 10 : e.to_i }
                .each_with_index
                .reduce(0) do |sum, pair|
                  e, i = pair
                  sum = sum + (10 - i) * e
                end % 11 == 0
  end

end
