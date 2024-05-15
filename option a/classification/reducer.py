import sys
cause_total = {}
#Partitoner
for line in sys.stdin:
    line = line.strip()
    state,cause, total = line.split('\t')
    state_cause = cause +': ' + state
    if state_cause in cause_total:
        cause_total[state_cause].append(int(total))
    else:
        cause_total[state_cause] = []
        cause_total[state_cause].append(int(total))
    #Reducer
for state_cause in cause_total.keys():
    ave_total = round(sum(cause_total[state_cause])*1.0 / len(cause_total[state_cause]))
    print('%s\t%s' % (state_cause, ave_total))