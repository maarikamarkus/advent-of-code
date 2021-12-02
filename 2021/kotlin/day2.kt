import java.io.File

fun main() {
  fun getAllLinesFromFile(filename: String): List<String> =
    File(filename).readLines().map { it.trim() }

  fun part1(input: List<String>): Int {
    var x: Int = 0;
    var y: Int = 0;

    input.forEach { el ->
      val command = el.split(" ")
      val dir = command[0]
      val amount = command[1].toInt()

      if (dir == "forward") x += amount
      else if (dir == "up") y-= amount
      else y += amount
    }

    return x * y
  }

  fun part2(input: List<String>): Int {
    var x: Int = 0
    var y: Int = 0
    var aim: Int = 0

    input.forEach { el ->
      val command = el.split(" ")
      val dir = command[0]
      val amount = command[1].toInt()

      if (dir == "down") aim += amount
      else if (dir == "up") aim -= amount
      else {
        x += amount
        y += aim*amount
      }
    }

    return x * y
  }

  val input = getAllLinesFromFile("../data/day2-input.txt")
  println("Part I: " + part1(input).toString())
  println("Part II: " + part2(input).toString())

  
}
