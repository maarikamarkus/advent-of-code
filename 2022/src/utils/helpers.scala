package utils.helpers

import scala.io.Source

def readData(source: String, day: Int): String =
  Source.fromFile(s"data/$source/day$day").mkString
