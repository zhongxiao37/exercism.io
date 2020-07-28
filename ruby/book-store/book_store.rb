class BookStore
  BOOK_PRICES = {
    1 => 8.0,
    2 => 15.2,
    3 => 21.6,
    4 => 25.6,
    5 => 30.0
  }

  # 1. splite the basket by duplicate books. E.g. [2,2] will be splited into basket [2] and n 2.
  # 2. figure out the single books. E.g. [1,1,2,2,3] will return [3]
  # 3. figure out the multiple books size info. E.g. [1,1,2,2,3] will return [[2,2]]. This means two groups [1,2] and [1,2]
  # 4. calculate the possible combinations. E.g. [1,1,2,2,3] will return [[3,2], [2,3]]

  def self.calculate_price(basket)
    return 0.0 if basket.empty?

    basket, n = divide_basket_by_duplicates(basket)
    single_books = parse_single_books(basket)
    multi_books = parse_multi_books(basket - single_books)
    multi_books = possible_combinations(single_books, multi_books)
    figure_out_best_price(multi_books) * n
  end

  def self.divide_basket_by_duplicates(basket)
    groups = basket.group_by { |e| e }
                   .sort_by { |k, v| v.size }
                   .map { |_, v| v }
    min_size = groups[0].size
    return basket, 1 unless groups.all? { |v| v.size % min_size == 0 } || min_size == 1

    basket = groups.map do |e|
      i = e.size / groups[0].size
      e[0...i]
    end.flatten

    return basket, min_size
  end


  def self.parse_single_books(basket)
    group = basket.group_by { |e| e }
                  .map { |k, v| v }
    group.select { |e| e.size == 1 }.flatten
  end

  def self.parse_multi_books(basket)
    group = basket.group_by { |e| e }
                  .map { |k, v| v }
    return [] if group.empty?

    if group.size == 1
      group.map { |e| e.map { |t| 1 } }
    else
      multi_books = group.shift
      group.each do |e|
        multi_books = multi_books.zip(e)
        multi_books.map!(&:flatten)
      end
      [multi_books.map { |e| e.compact.size }]
    end
  end

  def self.possible_combinations(single_books, multi_books)
    return [[single_books.size]] if multi_books.empty?

    single_books.size.times do |_|
      multi_books = multi_books.each_with_object([]) do |group, sum|
        group.size.times do |i|
          tmp = group.clone
          tmp[i] += 1
          sum << tmp
        end
      end
    end
    multi_books
  end

  def self.figure_out_best_price(multi_books)
    multi_books.map do |comb|
      comb.map { |e| BOOK_PRICES[e] }
          .reduce(:+)
    end.min.round(2)
  end

end
