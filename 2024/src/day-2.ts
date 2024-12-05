import { readInput } from "./utils/utils";

function part1() {
  const input = readInput(day, test);
  const reports = getReports(input);
  console.log(reports.map(report => isReportSafe(report)).reduce((acc, curr) => acc + (curr ? 1 : 0), 0))
}

function part2() {
  const input = readInput(day, test);
  const reports = getReports(input);
  console.log(
    reports.reduce((acc, curr) => 
      // Report is already safe, or exists a safe subreport
      acc + (isReportSafe(curr) || curr.some(
        (_, i) => isReportSafe([...curr.slice(0, i), ...curr.slice(i + 1)]))
        ? 1 : 0
      ), 0
  ));
}

function getReports(input: string): number[][] {
  const rows: string[] = input.trim().split("\n");
  return rows.map(row => row.split(" ").map(el => parseInt(el)));
}

function isReportSafe(report: number[]): boolean {
  const compareNums = (a: number, b: number) => a - b;
  const compareNumsAlt = (a: number, b: number) => b - a;
  if (!report.toSorted(compareNums).every((el, idx) => el === report[idx]) && 
      !report.toSorted(compareNumsAlt).every((el, idx) => el === report[idx])) {
    return false;
  }

  let i = 1;
  while (i < report.length) {
    const prev = report[i - 1];
    const curr = report[i];
    const diff = Math.abs(prev - curr);

    if (diff <= 0 || diff > 3) {
      return false;
    }
    i++;
  }
  return true;
}


const day = 2;
const test = true;
part1()
part2()