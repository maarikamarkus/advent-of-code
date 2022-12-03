package dayX

import scala.io.Source

@main def part1(source: String): Unit = {
  val data = Source.fromFile(s"data/$source/day3").mkString
  println(sol1(data))
}

@main def part2(source: String): Unit = {
  val data = Source.fromFile(s"data/$source/day3").mkString
  println(sol2(data))
}

def sol1(data: String): Int = {
  0
}

def sol2(data: String): Int = {
  0
}
