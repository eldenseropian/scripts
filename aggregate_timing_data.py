"""
To generate data for this script:
for i in `seq 100`; do { time [process_to_time] ; } 2>> /tmp/timing.txt; [clean up] ; done
"""

f = open("/tmp/timing.txt", "r")
lines = f.readlines()
real = [float(line.split("\t")[1][2:-2]) for line in lines if "real" in line]
user = [float(line.split("\t")[1][2:-2]) for line in lines if "user" in line]
sys = [float(line.split("\t")[1][2:-2]) for line in lines if "sys" in line]

print "min real", min(real)
print "max real", max(real)
print "mean real", sum(real)/len(real)
print
print "min user", min(user)
print "max user", max(user)
print "mean user", sum(user)/len(user)
print
print "min sys", min(sys)
print "max sys", max(sys)
print "mean sys", sum(sys)/len(sys)
