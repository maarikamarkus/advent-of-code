package day6

import utils.helpers.readData
import scala.io.Source

@main def part1(source: String): Unit = {
  val data = readData(source, 6)
  println(sol1(data))
  }

@main def part2(source: String): Unit = {
  val data = readData(source, 6)
  println(sol2(data))
}

def sol1(data: String): Int = 
  findEndOfPacketMarker(data, 4)

def sol2(data: String): Int = {
  findEndOfPacketMarker(data, 14)
}

def findEndOfPacketMarker(input: String, packetSize: Int): Int = 
  input.sliding(packetSize).indexWhere(window => packetMarker(window, packetSize)) + packetSize

def packetMarker(input: String, packetSize: Int): Boolean = input.toSet.size == packetSize
