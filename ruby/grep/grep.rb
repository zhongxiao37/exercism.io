class Grep
  def self.grep(pattern, flags, files)
    grep_lines = []
    files.each { |f| grep_lines += process_single_file(f, pattern, flags) }
    format_results(grep_lines, flags, files.size > 1)
  end

  def self.process_single_file(file, pattern, flags)
    grep_lines = []
    regexp_flags = flags.include?('-i') ? Regexp::IGNORECASE : nil
    reg = Regexp.new(pattern, regexp_flags)

    File.open(file).each.with_index do |l, i|
      matched = false
      if flags.include?('-x')
        matched =  true if l.rstrip.downcase == pattern.downcase
      elsif reg.match(l)
        matched =  true
      end

      if flags.include?('-v')
        grep_lines << MatchLine.new(i + 1, l.rstrip, file) unless matched
      elsif matched
        grep_lines << MatchLine.new(i + 1, l.rstrip, file)
      end
    end

    grep_lines
  end

  def self.format_results(grep_lines, flags, include_file_name)
    format_results = if flags.include?('-l')
                       grep_lines.map(&:file_name).uniq
                     elsif flags.include?('-n')
                       if include_file_name
                         grep_lines.map { |e| '%s:%s:%s' % [e.file_name, e.line_number, e.line_text] }
                       else
                         grep_lines.map { |e| '%s:%s' % [e.line_number, e.line_text] }
                       end
                     else
                       grep_lines.map { |e| include_file_name ? '%s:%s' % [e.file_name, e.line_text] : e.line_text }
                     end

    format_results.join("\n")
  end

  class MatchLine
    attr_reader :line_number, :line_text, :file_name

    def initialize(line_number, line_text, file_name)
      @line_number = line_number
      @line_text = line_text
      @file_name = file_name
    end
  end
end
