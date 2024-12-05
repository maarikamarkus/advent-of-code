"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const utils_1 = require("./utils/utils");
function part1() {
    const input = (0, utils_1.readInput)(day, test).trim();
    const { first, second } = getCols(input);
    const distances = [];
    for (let i = 0; i < first.length; i++) {
        const distance = Math.abs(second[i] - first[i]);
        distances.push(distance);
    }
    console.log(distances.reduce((acc, curr) => acc + curr, 0));
}
function part2() {
    const input = (0, utils_1.readInput)(day, test).trim();
    const { first, second } = getCols(input);
    const rightCounts = new Map();
    second.forEach(num => { var _a; return rightCounts.set(num, ((_a = rightCounts.get(num)) !== null && _a !== void 0 ? _a : 0) + 1); });
    const simScore = first.reduce((acc, curr) => { var _a; return acc + (curr * ((_a = rightCounts.get(curr)) !== null && _a !== void 0 ? _a : 0)); }, 0);
    console.log(simScore);
}
function getCols(input) {
    const rows = input.split("\n");
    const first = [];
    const second = [];
    rows.forEach(row => {
        const parts = row.split(/\s+/);
        first.push(parseInt(parts[0]));
        second.push(parseInt(parts[1]));
    });
    const compareNums = (a, b) => a - b;
    return { first: first.sort(compareNums), second: second.sort(compareNums) };
}
const day = 1;
const test = true;
part1();
part2();
