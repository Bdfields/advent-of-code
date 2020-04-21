"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
var fs_1 = __importDefault(require("fs"));
var fileBuffer = fs_1.default.readFileSync("test-data.txt");
var weights = fileBuffer
    .toString()
    .split("\n")
    .map(function (str) { return +str; });
console.log(weights);
var total = 0;
weights.forEach(function (weight) { return (total += fuelRequired(weight)); });
console.log(total);
total = 0;
weights.forEach(function (weight) { return (total += fuelRequiredInception(weight)); });
console.log(total);
function fuelRequired(mass) {
    return Math.floor(mass / 3) - 2;
}
function fuelRequiredInception(mass) {
    var total = 0;
    mass = fuelRequired(mass);
    while (mass > 0) {
        total += mass;
        mass = fuelRequired(mass);
    }
    return total;
}
