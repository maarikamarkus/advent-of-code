# Advent of Code 2022 in Scala

## Setup

I use Visual Studio Code with Metals to write Scala code, and scala-cli to compile and run it.

### How to run a solution

To run a solution on the given input in the `data/input` folder:
```
$ scala-cli src -M <dayX>.<partX> -- input
```

For example:
```
$ scala-cli src -M day1.part1 -- input
```

To run the solution on test data in the `data/test` run:
```
$ scala-cli src -M <dayX>.<partX> -- test
```