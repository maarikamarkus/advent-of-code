package day1

import scala.io.Source
import scala.collection.mutable.ListBuffer

@main def part1(source: String): Unit =
  val input = Source.fromFile(s"data/$source/day1").mkString
  val answer = sol1(input)
  println(s"The solution is $answer")

@main def part2(source: String): Unit =
  val input = Source.fromFile(s"data/$source/day1").mkString
  val answer = sol2(input)
  println(s"The solution is $answer")

def sol1(input: String): Int = calories(input).max

def sol2(input: String): Int = calories(input).sorted.reverse.take(3).sum

private def calories(data: String): ListBuffer[Int] = {
  val calories = new ListBuffer[Int]
  var cur = 0

  for (line <- data.linesIterator) {
    if (line.nonEmpty) {
      cur += line.toInt
    } else {
      calories += cur
      cur = 0
    }
  }
  calories += cur
  calories
}