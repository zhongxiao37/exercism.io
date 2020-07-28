enum = [1,3,5].each

p enum

loop do
  puts enum.next 
end

puts 'this will be printed out'


array = [1, 2, 3]
enum = array.to_enum

p enum


array = [1, 2, 3]
enum = array.to_enum(&:each)

p enum