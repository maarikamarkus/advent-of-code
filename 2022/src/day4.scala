package day4

import utils.helpers.readData
import scala.io.Source

@main def part1(source: String): Unit = {
  val data = readData(source, 4)
  println(sol1(data))
}

@main def part2(source: String): Unit = {
  val data = readData(source, 4)
  println(sol2(data))
}

def sol1(data: String): Int = {
  val pairs = splitIntoTupleRanges(data)
  pairs.map(oneRangeFullyContainsOther).sum
}

def sol2(data: String): Int = {
  val pairs = splitIntoTupleRanges(data)
  pairs.map(rangesOverLap).sum
}

private def oneRangeFullyContainsOther(ranges: ((Int, Int), (Int, Int))): Int =
  val expandedFirst = expand(ranges(0))
  val expandedSecond = expand(ranges(1))
  val union = expandedFirst.union(expandedSecond)
  if (union.size == expandedFirst.size || union.size == expandedSecond.size) then 1 else 0

private def expand(pair: (Int, Int)): Set[Int] =
  (pair(0) until (pair(1) + 1)).toSet

private def rangesOverLap(ranges: ((Int, Int), (Int, Int))): Int =
  val expandedFirst = expand(ranges(0))
  val expandedSecond = expand(ranges(1))
  val union = expandedFirst.union(expandedSecond)
  if (union.size < expandedFirst.size + expandedSecond.size) then 1 else 0

private def splitIntoTupleRanges(data: String): List[((Int, Int), (Int, Int))] =
  data.split("\n").map(_.split(",") match { 
    // [
    // ((2,4), (6,8)),
    // ((2,3), (4,5)),
    // ...
    // ]
    case Array(i, j) => 
      (
        (i.split("-")(0).toInt, i.split("-")(1).toInt), 
        (j.split("-")(0).toInt, j.split("-")(1).toInt)
      )
  }).toList