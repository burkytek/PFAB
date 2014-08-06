gpas = {"Lassoff":3.12, "Johnson":2.22, "Reich":3.59, "Honeychurch":2.98, "Maini":3.11, "Levin":2.88, "Marcus":2.77, "Banks":3.71}

sum = 0
for key, value in gpas.iteritems():
    print "Last Name:", key, "	", "GPA:", value
    sum = sum + value

print "Average GPA is", sum/len(gpas)

rank = 1
for key in sorted(gpas.iteritems(), key=lambda gpa: gpa[1], reverse=True):
    print "Rank #", rank, "    ", key[0]
    rank = rank + 1