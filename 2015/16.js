/* --- Day 16: Aunt Sue ---

Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

    children, by human DNA age analysis.
    cats. It doesn't differentiate individual breeds.
    Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
    goldfish. No other kinds of fish.
    trees, all in one group.
    cars, presumably by exhaust or gasoline or something.
    perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1

You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?

Your puzzle answer was 373.

--- Part Two ---

As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?

Your puzzle answer was 260.
*/

const fs = require('fs');
const path = require('path');
const { exit } = require('process');

const INPUT_PATH = path.join(__dirname, 'input/16.txt');
const tickerTapeList = {
	children: 3,
	cats: 7,
	samoyeds: 2,
	pomeranians: 3,
	akitas: 0,
	vizslas: 0,
	goldfish: 5,
	trees: 3,
	cars: 2,
	perfumes: 1,
};

function parseInput(inputFilePath) {
	return fs.promises
		.readFile(inputFilePath, 'utf-8')
		.then((data) => {
			let sueList = [],
				regExp = /(\w+):? (\d+),?/g,
				i = 0,
				match = null;

			while ((match = regExp.exec(data)) !== null) {
				if (match[1] == 'Sue') {
					// it's a new line
					i = match[2] - 1;
					sueList[i] = {};
				} else sueList[i][match[1]] = parseInt(match[2]); // store the value
			}
			return sueList;
		})
		.catch((err) => {
			console.error(err);
			exit(-1);
		});
}

function binarySearch(arr, val) {
	let start = 0,
		end = arr.length - 1;

	while (start <= end) {
		const mid = Math.floor((start + end) / 2);
		if (arr[mid] === val) return mid;
		if (arr[mid] < val) start = mid;
		else end = mid - 1;
	}
	return -1;
}

function couldBeThisSuePart2(prop, sue, tickerTapeList) {
	return (
		(['cats', 'trees'].includes(prop) && sue[prop] > tickerTapeList[prop]) ||
		(['pomeranians', 'goldfish'].includes(prop) &&
			sue[prop] < tickerTapeList[prop]) ||
		(!['cats', 'trees', 'pomeranians', 'goldfish'].includes(prop) &&
			sue[prop] == tickerTapeList[prop]) ||
		sue[prop] == undefined
	); //part 2
}

function couldBeThisSuePart1(prop, sue, tickerTapeList) {
	return sue[prop] == tickerTapeList[prop] || sue[prop] == undefined; //part 1 check
}

async function checkSueList(sueList, checkFunction) {
	let sueCheck = new Array(sueList.length).fill(true);
	const tickerTapeListProperties = Object.keys(tickerTapeList);
	for (const prop of tickerTapeListProperties) {
		for (const [i, sue] of sueList.entries()) {
			if (
				!sueCheck[i] || // if false we already established this is not the right sue -> skip check
				checkFunction(prop, sue, tickerTapeList, 1)
			)
				continue;
			//sueCheck.splice(binSrc(sueCheck, i), 1);
			sueCheck[i] = false;
		}
	}
	return sueCheck.indexOf(true) + 1; // we assume there is at least one
}

async function main() {
	let sueList = await parseInput(INPUT_PATH);
	let part1Promise = checkSueList(sueList, couldBeThisSuePart1);
	let part2Promise = checkSueList(sueList, couldBeThisSuePart2);
	const [part1Result, part2Result] = await Promise.all([
		part1Promise,
		part2Promise,
	]);
	console.log('Part 1 result: ', part1Result);
	console.log('Part 2 result: ', part2Result);
}

main();
