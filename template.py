# Advent of Code 2021
import os
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
SCRIPT_DIR = os.path.dirname(__file__)
INPUT_PATH = f'input/{os.path.basename(__file__).split(".")[0]}.txt'    # 'input/<day_number>.txt'

def main():
    input_file = os.path.join(SCRIPT_DIR, INPUT_PATH)
    with open(input_file, 'r') as file:
        report = file.readlines()
    print(*report)
    
if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info('Execution time: %0.4f seconds', t2 - t1)