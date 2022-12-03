package day3

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
  val ruckSacks = data.split("\n").toList
  sumPrioritiesSack(ruckSacks)
}

def sol2(data: String): Int = {
  val rucksackGroups = data.split("\n").toList.grouped(3).toList
  sumPrioritiesGroup(rucksackGroups)
}

private def sumPrioritiesSack(rucksacks: List[String]): Int =
  rucksacks.map(prioritySack).sum

private def sumPrioritiesGroup(rucksackGroups: List[List[String]]): Int = 
rucksackGroups.map(priorityGroup).sum

private def prioritySack(rucksack: String): Int =
  val middle = rucksack.length / 2
  val ch = commonItems(rucksack.slice(0, middle), rucksack.slice(middle, rucksack.length))(0)
  if ch.isUpper then ch.toInt - 38 else ch.toInt - 96

private def priorityGroup(rucksackGroup: List[String]): Int = 
  val ch = commonItems(rucksackGroup(0), commonItems(rucksackGroup(1), rucksackGroup(2)))(0)
  if ch.isUpper then ch.toInt - 38 else ch.toInt - 96

private def commonItems(group1: String, group2: String): String =
  group1.intersect(group2)
