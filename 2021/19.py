# Advent of Code 2021
import os
import time
import logging
import re

class Scanner:
    def __init__(self, num, beacons, posx = None, posy = None, posz = None) -> None:
        self.num = num
        self.pos = [posx, posy, posz]
        self.beacons = beacons
    def __init__(self, num, posx = None, posy = None, posz = None) -> None:
        self.num = num
        self.pos = [posx, posy, posz]
        self.beacons = []
    def __repr__(self) -> str:
        s = f'-- scanner {self.num} --\n'
        for beacon in self.beacons:
            s += f'{",".join(map(str, beacon))}\n'
        return s
    def setBeacons(self, beacons):
        self.beacons = beacons
    def addBeacons(self, beacon):
        self.beacons.append(beacon)
    def setPosition(self, posx = None, posy = None, posz = None):
        self.pos = [posx, posy, posz]

    
logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
SCRIPT_DIR = os.path.dirname(__file__)
INPUT_PATH = f'input/{os.path.basename(__file__).split(".")[0]}.txt'    # 'input/19.txt'

def main():
    input_file = os.path.join(SCRIPT_DIR, INPUT_PATH)
    with open(input_file, 'r') as file:
        report = file.readlines()
    scannersV = []
    scanners = []
    for line in report:
        if line.startswith('--'):
            scannersV.append([])
            scanners.append( Scanner(len(scanners)) )
        else:
            if line == '\n': continue
            beacons = list(map(int, line.rstrip().split(',')))
            scannersV[-1].append(beacons)
            scanners[-1].addBeacons(beacons)
    scanners[0].setPosition(0, 0, 0)    
    beacon1 = scanners[0].beacons[0]
    beacon2 = scanners[1].beacons[0]
    
    
    
    # for scanner in scanners:
    #     print(scanner)
    
        
    # for i,beacons in enumerate(scanners):
    #     logger.debug('--scanner %d', i)
    #     for beacon in beacons:
    #         logger.debug('%d,%d', *beacon)
    
if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info('Execution time: %0.4f seconds', t2 - t1)