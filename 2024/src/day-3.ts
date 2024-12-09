import { readInput } from "./utils/utils";

function part1(input: string) {
  const pattern = /mul\(\d{1,3},\d{1,3}\)/g;

  const matches = input
    .match(pattern);
  // console.log("matches ", matches);
  
  const muls = matches ? matches.map(exp => mul(exp)) : [];
  // console.log("muls ", muls);
  
  const res = muls.reduce((acc, curr) => acc + curr, 0);
  console.log("res ", res);
}

function part2(input: string) {
  const pattern = /(?<=(?:do\(\)|^)(?:[^d]|d(?!on't\(\)))*)mul\((\d{1,3}),(\d{1,3})\)/g;
  const matches = input.matchAll(pattern);
  let res = 0;
  matches.forEach(match => {
    res += Number(match[1]) * Number(match[2])
  });
  console.log("res ", res);
}

function mul(input: string): number {
  const re = /mul\((\d{1,3}),(\d{1,3})\)/g;
  const matches = input.matchAll(re);
  let res = 0;
  matches.forEach(match => res = parseInt(match[1]) * parseInt(match[2]));
  return res;
}


const day = 3;
const test = false;
const input = readInput(day, test);

// part1(input);
part2(input);