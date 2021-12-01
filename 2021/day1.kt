import java.io.File

fun main() {
  
  val filename: String = "1_input.txt"
  val lines = File(filename).readLines()
  val nums = lines.map { it.trim().toInt() }

  fun part1(): Int {
    var previous: Int? = null
    var counter = 0

    loop@ for (num in nums) {
      if (previous == null) {
        previous = num
        continue@loop
      }

      if (num > previous) counter += 1

      previous = num
    }
    return counter
  }

  fun part2(): Int {
    var previous: Int? = null
    var counter = 0

    loop@ for (i in 0 until nums.size - 2) {
      val windowSum: Int = nums[i] + nums[i+1] + nums[i+2]

      if (previous == null) {
        previous = windowSum
        continue@loop
      }

      if (windowSum > previous!!) counter += 1

      previous = windowSum
    }
    return counter
  }

  println("Part I " + part1().toString())
  println("Part II " + part2().toString())
}