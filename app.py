nilai1 = int(input("Part 1\t"))
nilai2 = int(input("Part 2\t"))
nilai3 = int(input("Part 3\t"))

def nilai(x, y, z):
  # Part 1 -> 15 Question * 2 => 30
  # Part 2 -> 5 Question * 2  => 10
  # Part 3 -> 2 Question * 5  => 10
  #                           => 50 * 2
  #                    Result => 100
  x *= 2
  y *= 2
  z *= 5

  # Result = ( Part 1  + Part 2 + Part 3 ) * 2
  return ( x + y + z ) * 2

print(nilai(nilai1, nilai2, nilai3))
