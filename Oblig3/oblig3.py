import oblig3runner
import sys
import time

def main(filename):
    with open(filename, 'r') as f:
        A = [int(x) for x in f.readlines()]
    #oblig3runner.run_algs_part1(A, filename)
    t = time.time_ns()
    oblig3runner.run_algs_part2(A, filename)
    timeus = (time.time_ns() - t)/1000
    print(f"Den totale tiden målt i mikrosekunder: {timeus} µs")

if __name__ == '__main__':
    main(sys.argv[1])
