require 'minitest/autorun'
require_relative 'collatz_conjecture'

# Common test data version: 1.1.1 25c4479
class CollatzConjectureTest < Minitest::Test
  def test_zero_steps_for_one
    # skip
    assert_equal 0, CollatzConjecture.steps(1)
  end

  def test_divide_if_even
    assert_equal 4, CollatzConjecture.steps(16)
  end

  def test_even_and_odd_steps
    assert_equal 9, CollatzConjecture.steps(12)
  end

  def test_large_number_of_even_and_odd_steps
    assert_equal 152, CollatzConjecture.steps(1_000_000)
  end

  def test_zero_is_an_error
    assert_raises(ArgumentError) { CollatzConjecture.steps(0) }
  end

  def test_negative_value_is_an_error
    assert_raises(ArgumentError) { CollatzConjecture.steps(-15) }
  end

  # Problems in exercism evolve over time, as we find better ways to ask
  # questions.
  # The version number refers to the version of the problem you solved,
  # not your solution.
  #
  # Define a constant named VERSION inside of the top level BookKeeping
  # module, which may be placed near the end of your file.
  #
  # In your file, it will look like this:
  #
  # module BookKeeping
  #   VERSION = 1 # Where the version number matches the one in the test.
  # end
  #
  # If you are curious, read more about constants on RubyDoc:
  # http://ruby-doc.org/docs/ruby-doc-bundle/UsersGuide/rg/constants.html

  def test_bookkeeping
    skip
    assert_equal 1, BookKeeping::VERSION
  end
end
