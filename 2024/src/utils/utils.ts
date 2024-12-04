import * as fs from 'fs';
import * as path from 'path';

export function readInput(day: number, test: boolean): string {
  const file = test ? 'day-' + day + '-test.txt' : 'day-' + day + '.txt';
  const absPath = path.resolve(__dirname, `../input/${file}`);
  const input = fs.readFileSync(absPath, 'utf8');

  return input;
}
