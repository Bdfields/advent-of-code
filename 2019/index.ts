import fs from "fs";

let fileBuffer = fs.readFileSync("test-data.txt");

let weights = fileBuffer
  .toString()
  .split("\n")
  .map((str) => +str);
console.log(weights);

let total = 0;
weights.forEach((weight) => (total += fuelRequired(weight)));

console.log(total);

total = 0;
weights.forEach((weight) => (total += fuelRequiredInception(weight)));
console.log(total);

function fuelRequired(mass: number): number {
  return Math.floor(mass / 3) - 2;
}

function fuelRequiredInception(mass: number): number {
  let total = 0;
  mass = fuelRequired(mass);
  while (mass > 0) {
    total += mass;
    mass = fuelRequired(mass);
  }

  return total;
}
