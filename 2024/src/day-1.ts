import { readInput } from "./utils/utils";

function part1() {
  const input = readInput(day, test).trim();
  const {first, second} = getCols(input);
  const distances = [];

  for (let i = 0; i < first.length; i++) {
    const distance = Math.abs(second[i] - first[i]);
    distances.push(distance);
  }
  console.log(distances.reduce((acc, curr) => acc + curr, 0));
}

function part2() {
  const input = readInput(day, test).trim();
  const {first, second} = getCols(input);
  const rightCounts = new Map();
  second.forEach(num => rightCounts.set(num, (rightCounts.get(num) ?? 0) + 1));

  const simScore = first.reduce((acc, curr) => acc + (curr * (rightCounts.get(curr) ?? 0)), 0);
  console.log(simScore);
}

function getCols(input: string): { first: number[], second: number[]} {
  const rows = input.split("\n");
  const first: number[] = [];
  const second: number[] = [];
  rows.forEach(row => {
    const parts = row.split(/\s+/);
    first.push(parseInt(parts[0]));
    second.push(parseInt(parts[1]));
  })
  const compareNums = (a: number, b: number) => a - b;

  return {first: first.sort(compareNums), second: second.sort(compareNums)};
}

const day = 1;
const test = true;

part1();
part2();