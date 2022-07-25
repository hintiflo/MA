import numpy as np 
import matplotlib.pyplot as plt

# plt.rcParams['text.usetex'] = True

dc = -10
amp = 0.51

n = range(0, 40, 1)
y = []

for i in range(len(n)):
    temp =  amp*n[i] + dc
    y.append(temp)
    
for i in range(len(n)):
    temp = amp*n[i] + dc
    y.append(temp)

for i in range(5):
    temp =0
    y.append(temp)



    
# plt.stem(y, basefmt=" ")
fig, (ax1, ax2) = plt.subplots(1,2)
plt.figure(figsize=(10,3))


(markerline, stemlines, baseline) = plt.stem(y)
plt.setp(stemlines, visible=False)
plt.setp(baseline, visible=False)
plt.setp(markerline, markersize = 2)
plt.text(30, 0, '0% ratio', rotation=0, size=15)
plt.axis([0, len(y), -11, 11])
plt.xlabel('Time')
plt.ylabel('Voltage')
# plt.title('ramp signal')
plt.grid(True)
#
plt.savefig("_rampAssymetry0perc.pdf",  dpi=800)
# plt.show()

y.clear()

for i in range(len(n)):
    temp = len(n) - amp*n[i] + dc -len(n)/2
    y.append(temp)
    
for i in range(len(n)):
    temp = len(n) - amp*n[i] + dc -len(n)/2
    y.append(temp)

for i in range(5):
    temp = 0
    y.append(temp)


    
# plt.stem(y, basefmt=" ")
fig, (ax1, ax2) = plt.subplots(1,2)
plt.figure(figsize=(10,3))


(markerline, stemlines, baseline) = plt.stem(y)
plt.setp(stemlines, visible=False)
plt.setp(baseline, visible=False)
plt.setp(markerline, markersize = 2)

plt.text(30, 0, '100% ratio', rotation=0, size=15)

plt.axis([0, len(y), -11, 11])
plt.xlabel('Time')
plt.ylabel('Voltage')
# plt.title('ramp signal')
plt.grid(True)
#
plt.savefig("_rampAssymetry100perc.pdf",  dpi=800)
# plt.show()


y.clear()

for i in range( int(len(n)/2) ):
    temp = amp*n[i]*2 + dc
    y.append(temp)
    
for i in range( int(len(n)/2) ):
    temp = (len(n) - amp*n[i]*2) + dc -len(n)/2
    y.append(temp)

for i in range( int(len(n)/2) ):
    temp = amp*n[i]*2 + dc
    y.append(temp)
    
for i in range( int(len(n)/2) ):
    temp = (len(n) - amp*n[i]*2) + dc -len(n)/2
    y.append(temp)

for i in range(5):
    temp = 0
    y.append(temp)

    
# plt.stem(y, basefmt=" ")
fig, (ax1, ax2) = plt.subplots(1,2)
plt.figure(figsize=(10,3))


(markerline, stemlines, baseline) = plt.stem(y)
plt.setp(stemlines, visible=False)
plt.setp(baseline, visible=False)
plt.setp(markerline, markersize = 2)

plt.text(30, 0, '50% ratio', rotation=0, size=15)

plt.axis([0, len(y), -11, 11])
plt.xlabel('Time')
plt.ylabel('Voltage')
# plt.title('ramp signal')
plt.grid(True)
#
plt.savefig("_rampAssymetry50perc.pdf",  dpi=800)
# plt.show()



