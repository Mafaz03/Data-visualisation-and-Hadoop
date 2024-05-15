import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    cause = line[1]
    state = line[2]
    deaths = line[3]
    print(f'{state}\t{cause}\t{deaths}')    
