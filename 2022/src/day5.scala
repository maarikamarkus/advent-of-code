package day5

import utils.helpers.readData
import scala.io.Source
import scala.collection.mutable.Map
import scala.collection.mutable.Stack

@main def part1(source: String): Unit = {
  val data = readData(source, 5)
  println(sol1(data))
}

@main def part2(source: String): Unit = {
  val data = readData(source, 5)
  println(sol2(data))
}

def sol1(data: String): String = {
  topOfStacks(data)
}

def sol2(data: String): String = {
  topOfStacks2(data)
}

private def topOfStacks(data: String): String = {
  val stackMap: Map[Int, Stack[Char]] = parseData(data)
  val stacks = stackMap.values
  var res = ""
  stacks.foreach(stack => res += (stack.pop))
  res
}

private def topOfStacks2(data: String): String = {
  val stackMap: Map[Int, Stack[Char]] = parseData2(data)
  val stacks = stackMap.values
  var res = ""
  stacks.foreach(stack => res += (stack.pop))
  res
}

private def parseData(data: String): Map[Int, Stack[Char]] = {
  val (startingMap: String, procedureKey: String) = Tuple.fromArray(data.split("\n\n"))

  val startingStacks = stacksOfCrates(startingMap)
  val procedure = rearrengementProcedure(procedureKey)
  runProcedure(startingStacks, procedure)
}

private def parseData2(data: String): Map[Int, Stack[Char]] = {
  val (startingMap: String, procedureKey: String) = Tuple.fromArray(data.split("\n\n"))

  val startingStacks = stacksOfCrates(startingMap)
  val procedure = rearrengementProcedure(procedureKey)
  runProcedure2(startingStacks, procedure)
}


private def stacksOfCrates(startingMap: String): Map[Int, Stack[Char]] = {
  var stackMap: Map[Int, Stack[Char]] = Map.empty
  var lines = startingMap.split("\n")
  lines = lines.slice(0, lines.length - 1)
  val noOfStacks = (lines(0).length() / 4.0).ceil.toInt
  
  for (i <- 1 to noOfStacks) {
    stackMap += (i -> Stack.empty)
  }
  
  val splittedLines = lines.map(line => line.grouped(4).toList.map(_.trim).toList).toList
  for (i <- splittedLines.length -1 to 0 by -1) {
    val line = splittedLines(i)
    for (j <- 1 to noOfStacks) {
      if (!line(j-1).isEmpty) stackMap += (j -> stackMap(j).push(line(j-1)(1)))
    }
  }
  stackMap
}

private def rearrengementProcedure(procedureKey: String): List[(Int, Int, Int)] = {
  procedureKey.split("\n").map(_.split(" ") match {
    case Array(_, m, _, f, _ , t) => (m.toInt, f.toInt, t.toInt)
  }).toList
}

private def runProcedure(stacks: Map[Int, Stack[Char]], procedure: List[(Int, Int, Int)]): Map[Int, Stack[Char]]
= {
  for ((n, f, t) <- procedure) {
    for (i <- 1 to n) {
      stacks(t).push(stacks(f).pop)
    }
  }
  stacks
}

private def runProcedure2(stacks: Map[Int, Stack[Char]], procedure: List[(Int, Int, Int)]): Map[Int, Stack[Char]]
= {
  for ((n, f, t) <- procedure) {
    var cratesToBeMoved: Array[Char] = Array.empty
    for (i <- 1 to n) {
      cratesToBeMoved +:= stacks(f).pop
    }
    cratesToBeMoved.foreach(crate => stacks(t).push(crate))
  }
  stacks
}