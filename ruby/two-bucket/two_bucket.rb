class TwoBucket
  attr_reader :moves, :goal_bucket, :other_bucket

  def initialize(bucket_one, bucket_two, goal_size, starting_bucket)
    @buckets = []
    @buckets << Bucket.new(bucket_one, :one)
    @buckets << Bucket.new(bucket_two, :two)
    @goal_size = goal_size
    @operations = []
    starting_bucket == 'one' ? @buckets : @buckets.reverse!
    move_buckets
  end

  def move_buckets
    cnt = 0
    while true
      fill_bucket(@buckets[0]) if @operations == 0
      transfer_between_buckets(@buckets[0], @buckets[1])

      goal_bucket = @buckets.find { |e| e.holding_size == @goal_size }
      cnt += 1
      break if goal_bucket
      break if @operations.size > 100
      break if cnt > 100
    end

    @goal_bucket = goal_bucket.label.to_s
    @other_bucket = @buckets.find { |e| e.holding_size != @goal_size }.holding_size
    @moves = @operations.size
  end


  def fill_bucket(bucket)
    bucket.holding_size = bucket.size
    @operations << "fill bucket #{bucket.label}"
  end

  def empty_bucket(bucket)
    bucket.holding_size = 0
    @operations << "empty bucket #{bucket.label}"
  end

  def transfer_between_buckets(starting_bucket, another_bucket)
    full_bkt = @buckets.find { |e| e.full? }
    empty_bkt = @buckets.find { |e| e.empty? }
    if full_bkt && empty_bkt
      min_size = [full_bkt.size, empty_bkt.size].min
      full_bkt.holding_size -= min_size
      empty_bkt.holding_size += min_size
      @operations << "transfer #{min_size} from bucket #{full_bkt.label} to bucket #{empty_bkt.label}"
      return nil
    end

    if starting_bucket.full? && !another_bucket.full?
      min_size = [starting_bucket.size, another_bucket.remaining_size].min
      starting_bucket.holding_size -= min_size
      another_bucket.holding_size += min_size
      @operations << "transfer #{min_size} from bucket #{starting_bucket.label} to bucket #{another_bucket.label}"
      return nil
    end

    if starting_bucket.holding_size > 0 && another_bucket.empty?
      min_size = [starting_bucket.holding_size, another_bucket.remaining_size].min
      starting_bucket.holding_size -= min_size
      another_bucket.holding_size += min_size
      @operations << "transfer #{min_size} from bucket #{starting_bucket.label} to bucket #{another_bucket.label}"
      return nil
    end

    if another_bucket.full?
      empty_bucket(another_bucket)
      return nil
    end

    if starting_bucket.empty?
      fill_bucket(starting_bucket)
      return nil
    end

  end

  class Bucket
    attr_reader :size, :label
    attr_accessor :holding_size
    def initialize(size, label)
      @size = size
      @label = label
      @holding_size = 0
    end

    def empty?
      @holding_size == 0
    end

    def full?
      @holding_size == @size
    end

    def remaining_size
      @size - @holding_size
    end
  end
end


module BookKeeping
  VERSION = 3
end

