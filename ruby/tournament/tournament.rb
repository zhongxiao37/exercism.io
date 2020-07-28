class Tournament

  attr_reader :matches
  def self.tally(input)
    @teams = []
    @matches = []

    score_list = ["Team                           | MP |  W |  D |  L |  P\n"]

    input.split("\n").map { |e| e.split(';') }.each do |m|
      team_1 = create_or_find_team(m[0])
      team_2 = create_or_find_team(m[1])
      @matches << Match.new(team_1, team_2, m[2])
    end

    @teams.sort { |a, b| [b.points, a.name] <=> [a.points, b.name] }.each do |t|
      score_list << "%-31s|%3d |%3d |%3d |%3d |%3d\n" % [t.name, t.matches, t.wins, t.draws, t.loses, t.points]
    end

    score_list.join
  end


  def self.create_or_find_team(team_name)
    team = @teams.find { |e| e.name == team_name }
    return team unless team.nil?
    team = Team.new(team_name)
    @teams << team
    team
  end


  class Team
    attr_accessor :wins, :draws, :loses
    attr_reader :name
    def initialize(name)
      @name = name
      @wins, @draws, @loses= 0, 0, 0
    end

    def points
      @wins * 3 + @draws * 1
    end

    def matches
      @wins + @loses + @draws
    end
  end

  class Match
    attr_reader :team_1, :team_2, :result
    def initialize(team_1, team_2, result)
      @team_1 = team_1
      @team_2 = team_2
      @result = result
      case result
      when 'win'
        @team_1.wins += 1
        @team_2.loses += 1
      when 'draw'
        @team_1.draws += 1
        @team_2.draws += 1
      when 'loss'
        @team_1.loses += 1
        @team_2.wins += 1
      else
        # invalid result do nothing
      end
    end
  end

end

module BookKeeping
  VERSION = 3
end
