class School
  attr_accessor :all_students
  def initialize
    @all_students = []
  end

  def add(name, grade)
    @all_students << Student.new(name, grade)
  end

  def students(grade)
    @all_students.select { |e| e.grade == grade }.map { |e| e.name }.sort rescue []
  end

  def grades
    @grades ||= @all_students.map { |e| e.grade }.uniq.sort
  end

  def students_by_grade
    grades.map { |e| {grade: e, students: students(e)} }
  end

  class Student
    attr_reader :name, :grade
    def initialize(name, grade)
      @name = name
      @grade = grade
    end

  end

end

module BookKeeping
  VERSION = 3
end