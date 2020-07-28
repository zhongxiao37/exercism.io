module Hamming

    def self.compute(src, tgt)
        raise ArgumentError.new("param lengths don't match each other") if src.length != tgt.length
        compare_params(src, tgt)
    end

    private

    def self.compare_params(src, tgt)
        index = 0
        diff_count = 0
        while index < src.length
            diff_count += 1 if src[index] != tgt[index]
            index += 1
        end
        diff_count
    end

end

module BookKeeping
    VERSION = 3 # Where the version number matches the one in the test.
end
