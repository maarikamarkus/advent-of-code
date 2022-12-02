package day2

import scala.io.Source

val testRound: Round = Round('A', 'Y')
val testRounds = List(testRound, testRound.copy(opponent = 'B', strategy = 'X'), testRound.copy(opponent = 'C', strategy = 'Z'))


@main def part1(source: String): Unit = {
  val data = Source.fromFile(s"data/$source/day2").mkString
  println(sol1(data))
}

@main def part2(source: String): Unit = {
  val data = Source.fromFile(s"data/$source/day2").mkString
  println(sol2(data))
}

def sol1(data: String): Int = {
  val rounds = data.split("\n").map(_.split(" ") match { case Array(i, j) => Round(i(0), j(0))}).toList
  totalScore(rounds)
}

def sol2(data: String): Int = {
  val rounds = data.split("\n").map(_.split(" ") match { case Array(i, j) => Round(i(0), j(0))}).toList
  totalScore2(rounds)
}

case class Round(opponent: Char, strategy: Char)

private def totalScore(rounds: List[Round]): Int =
  rounds.map(score).sum

private def score(round: Round): Int =
  shape(round.strategy) + outcome(round)

private def shape(sh: Char): Int = sh match
  case 'X' => 1
  case 'Y' => 2
  case 'Z' => 3

private def outcome(round: Round): Int = (round.opponent, round.strategy) match
  // rock vs rock => a vs x => 3
  // rock vs paper => a vs y => 0
  // rock vs scissors => a vs z => 6
  case ('A', 'X') => 3
  case ('A', 'Y') => 6
  case ('A', 'Z') => 0
  case ('B', 'X') => 0
  case ('B', 'Y') => 3
  case ('B', 'Z') => 6
  case ('C', 'X') => 6
  case ('C', 'Y') => 0
  case ('C', 'Z') => 3

private def totalScore2(rounds: List[Round]): Int =
  rounds.map(score2).sum

private def score2(round: Round): Int =
  shape(chooseShape(round)) + outcome2(round.strategy)

private def chooseShape(round: Round): Char = (round.opponent, round.strategy) match
  // a vs x = rock and lose => scissors = Z
  // a vs y = rock and draw => rock = x
  // a vs z = rock and win => paper = y
  case ('A', 'X') => 'Z'
  case ('A', 'Y') => 'X'
  case ('A', 'Z') => 'Y'
  
  // b vs x = paper and lose => rock = Z
  // b vs y = paper and draw => paper = Y
  // b vs z = scissors and win => scissors = Z
  case ('B', 'X') => 'X'
  case ('B', 'Y') => 'Y'
  case ('B', 'Z') => 'Z'

  // c vs x = scissors and lose => paper = Y
  // c vs y = scissors and draw => scissors = Z
  // c vs z = scissors and win => rock = X
  case ('C', 'X') => 'Y'
  case ('C', 'Y') => 'Z'
  case ('C', 'Z') => 'X'

private def outcome2(strategy: Char): Int = strategy match
  case 'X' => 0
  case 'Y' => 3
  case 'Z' => 6
  
// part 1
// A = X = rock
// B = Y = paper
// C = Z = scissors

// part 2
// A = rock
// B = paper
// C = scissors
// X = lose
// Y = draw
// Z = win
