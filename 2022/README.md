# Advent of Code 2022 in Scala

## Setup

I use Visual Studio Code with Metals to write Scala code, and scala-cli to compile and run it.

### How to run a solution

In a terminal you can run:
```
$ scala-cli src -M <dayX>.<partX> -- input
```

For example:
```
$ scala-cli src -M day1.part1 -- input
```

By default the solution programs run on input files in the `data/input` folder.

To run the solution on test data in the `data/test` run:
```
$ scala-cli src -M <dayX>.<partX> -- input
```