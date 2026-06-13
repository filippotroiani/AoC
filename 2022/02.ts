/*
--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

Your puzzle answer was 14264.

--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

Your puzzle answer was 12382.
 */

import { exit } from 'process';
import { join } from 'path';
import { promises } from 'fs';
const INPUT_PATH = join(__dirname, 'input/02.txt');

type RPSRule = {
	yourMove: RPSMoves;
	opponentMove: RPSMoves;
	result: RPSResults;
};

enum RPSMoves {
	rock,
	paper,
	scissors,
}

enum RPSResults {
	defeat,
	draw,
	win,
}

const MOVE_DICTIONARY = new Map([
	['B', RPSMoves.paper],
	['A', RPSMoves.rock],
	['C', RPSMoves.scissors],
	['X', RPSMoves.rock],
	['Y', RPSMoves.paper],
	['Z', RPSMoves.scissors],
]);

const RESULT_DICTIONARY = new Map([
	['Y', RPSResults.draw],
	['X', RPSResults.defeat],
	['Z', RPSResults.win],
]);

const RULES = [
	{
		yourMove: RPSMoves.rock,
		opponentMove: RPSMoves.scissors,
		result: RPSResults.win,
	},
	{
		yourMove: RPSMoves.scissors,
		opponentMove: RPSMoves.paper,
		result: RPSResults.win,
	},
	{
		yourMove: RPSMoves.paper,
		opponentMove: RPSMoves.rock,
		result: RPSResults.win,
	},
	{
		yourMove: RPSMoves.rock,
		opponentMove: RPSMoves.rock,
		result: RPSResults.draw,
	},
	{
		yourMove: RPSMoves.scissors,
		opponentMove: RPSMoves.scissors,
		result: RPSResults.draw,
	},
	{
		yourMove: RPSMoves.paper,
		opponentMove: RPSMoves.paper,
		result: RPSResults.draw,
	},
	{
		yourMove: RPSMoves.scissors,
		opponentMove: RPSMoves.rock,
		result: RPSResults.defeat,
	},
	{
		yourMove: RPSMoves.paper,
		opponentMove: RPSMoves.scissors,
		result: RPSResults.defeat,
	},
	{
		yourMove: RPSMoves.rock,
		opponentMove: RPSMoves.paper,
		result: RPSResults.defeat,
	},
] satisfies Array<RPSRule>;

const POINTS_FOR_YOUR_MOVE: Record<RPSMoves, number> = {
	[RPSMoves.rock]: 1,
	[RPSMoves.paper]: 2,
	[RPSMoves.scissors]: 3,
};

const POINTS_FOR_ROUND_RESULT: Record<RPSResults, number> = {
	[RPSResults.draw]: 3,
	[RPSResults.defeat]: 0,
	[RPSResults.win]: 6,
};

function getRoundResult(
	opponentMove: RPSMoves,
	yourMove: RPSMoves,
): RPSResults {
	let foundRule = RULES.find(
		(rule) => rule.opponentMove === opponentMove && rule.yourMove === yourMove,
	);
	if (foundRule == undefined)
		throw new Error(
			`Result not found for yourMove: ${yourMove}, opponentMove: ${opponentMove} `,
		);
	return foundRule.result;
}

function calculateRoundScorePart1(
	opponentMove: string,
	yourMove: string,
): number {
	const opponentDecodedMove = decodeMove(opponentMove);
	const yourDecodedMove = decodeMove(yourMove);

	if (opponentDecodedMove == undefined || yourDecodedMove == undefined)
		throw new Error('invalid round result');
	const roundResult = getRoundResult(opponentDecodedMove, yourDecodedMove);
	return calculateRoundPoints(yourDecodedMove, roundResult);
}

function calculateRoundScorePart2(
	opponentMove: string,
	expectedResult: string,
): number {
	const opponentDecodedMove = decodeMove(opponentMove);
	const decodedExpectedResult = RESULT_DICTIONARY.get(expectedResult);
	if (decodedExpectedResult == undefined)
		throw new Error(`Invalid expected result '${expectedResult}' in part2.`);
	const foundRule = RULES.find(
		(value) =>
			value.opponentMove === opponentDecodedMove &&
			value.result === decodedExpectedResult,
	);

	if (foundRule == undefined)
		throw new Error(
			`Rule not found for opponentMove: ${opponentMove} and expectedResult: ${expectedResult} in part2.`,
		);

	return calculateRoundPoints(foundRule.yourMove, foundRule.result);
}

function decodeMove(move: string): RPSMoves {
	const decodedMove = MOVE_DICTIONARY.get(move);
	if (decodedMove == undefined)
		throw new Error(`Invalid expected move '${decodedMove}'.`);
	return decodedMove;
}

function calculateRoundPoints(yourMove: RPSMoves, result: RPSResults): number {
	let score: number = 0;
	score += POINTS_FOR_YOUR_MOVE[yourMove];
	score += POINTS_FOR_ROUND_RESULT[result];
	return score;
}

async function main() {
	let totalScorePart1 = 0;
	let totalScorePart2 = 0;
	let inputData = await promises
		.readFile(INPUT_PATH, 'utf8')
		.catch((reason: any) => {
			console.log(reason);
			exit(-1);
		});
	const re = /(\w) (\w)/g;
	let line: RegExpExecArray | null;
	while ((line = re.exec(inputData)) !== null) {
		totalScorePart1 += calculateRoundScorePart1(line[1] ?? '', line[2] ?? '');
		totalScorePart2 += calculateRoundScorePart2(line[1] ?? '', line[2] ?? '');
	}
	console.log('Part 1: your total score of the tournment is ', totalScorePart1);
	console.log('Part 2: your total score of the tournment is ', totalScorePart2);
}

main();
