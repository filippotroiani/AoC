# Advent of Code 2015
# --- Day 14: Reindeer Olympics ---

# This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

# Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

# For example, suppose you have the following Reindeer:

#     Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
#     Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

# After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

# In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

# Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?

# Your puzzle answer was 2655.

# --- Part Two ---

# Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

# Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

# Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

# After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

# Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?

# Your puzzle answer was 1059.

import re
INPUT_PATH = '2015/input/14.txt'

def calculateDistance(seconds, speed, flyTime, restTime):   # return the distance traveled by the reindeer after 'seconds' seconds
	time = 0
	distance = 0
	while time < seconds:
		if time + flyTime < seconds:
			distance += speed*flyTime
		else:
			distance += speed*(seconds - time)
		time += flyTime + restTime
	return distance

def race(seconds, reindeers):   # return the winner points after 'seconds' seconds of race
    leaderDistance = 0
    leaders = []
    for reindeer, info in reindeers.items():    # add race infos to each reindeer
        info['raceInfo'] = {'points' : 0, 'distance' : 0, 'running' : True, 'time' : 0}
    for _ in range(seconds):    # for every second until seconds (2503)
        for reindeer, info in reindeers.items():    # for every reindeer
            if info['raceInfo']['running']:   # if reindeer is running
                info['raceInfo']['distance'] += info['speed']
                info['raceInfo']['time'] += 1
                if info['raceInfo']['time'] == info['flyTime']: # if reindeer has been running enough put it to rest
                    info['raceInfo']['time'] = 0
                    info['raceInfo']['running'] = False
                if info['raceInfo']['distance'] > leaderDistance:   # if reindeer is leading the race put it in leaders
                    leaderDistance = info['raceInfo']['distance']
                    leaders = [reindeer]
                elif info['raceInfo']['distance'] == leaderDistance:
                    leaders.append(reindeer)
            else:   # if reindeer is resting
                info['raceInfo']['time'] += 1
                if info['raceInfo']['time'] == info['restTime']:    # if reindeer is done resting let it run
                    info['raceInfo']['time'] = 0
                    info['raceInfo']['running'] = True
        for leader in leaders:  # update leaders' points
            reindeers[leader]['raceInfo']['points'] += 1
        maxPoints = 0
        for info in reindeers.values(): # look for the winner points
            if info['raceInfo']['points'] > maxPoints:
                maxPoints = info['raceInfo']['points']
    return maxPoints

SECONDS = 2503
reindeers = {}
with open(INPUT_PATH) as file:
	for line in file:
		reindeerInfo = re.findall("(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
		reindeers[reindeerInfo[0][0]] = {'speed' : int(reindeerInfo[0][1]), 'flyTime' : int(reindeerInfo[0][2]), 'restTime' : int(reindeerInfo[0][3])}
# PART 1
maxDistance = 0
for reindeer in reindeers.values():
	distance = calculateDistance(SECONDS , **reindeer)
	if distance > maxDistance:
		maxDistance = distance
print(f'PART 1: The winning reindeer traveled {maxDistance} km.')

# PART 2
maxPoints = race(SECONDS, reindeers)
print(f'PART 2: The winning reindeer has {maxPoints} points.')
