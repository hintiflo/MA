import numpy as np 
import matplotlib.pyplot as plt

# plt.rcParams['text.usetex'] = True

dc = -5.5

amp = 0.815
n = range(0, 20, 1)
y = []

for i in range(len(n)):
    temp =  amp*n[i] + dc
    y.append(temp)
    
for i in range(len(n)):
    temp = amp*n[i] + dc
    y.append(temp)

for i in range(3):
    temp = amp*n[i] + dc
    y.append(temp)
    
# plt.stem(y, basefmt=" ")
plt.figure(figsize=(10,6))

(markerline, stemlines, baseline) = plt.stem(y)
plt.setp(stemlines, visible=False)
plt.setp(baseline, visible=False)
plt.setp(markerline, markersize = 2)

# plt.line( (0,0),(20,0), linewidth = 10)
plt.annotate("", xy=(0, 0), xytext=( 43, 0),  arrowprops=dict(arrowstyle="-"))

plt.annotate("", xy=(len(n)-1, 5.1), xytext=( 2*len(n)-1, 5.1),  arrowprops=dict(arrowstyle="<->"))
plt.text(1.5*len(n) -2, 4.1, "$t_{signal}$", rotation=0, size=15)

plt.annotate("", xy=(13-.2, 5.1), xytext=( 13+1 +.2, 5.1),  arrowprops=dict(arrowstyle="<->"))
plt.text(13-.5, 4.1, '$t_{sample}$', rotation=0, size=15)

plt.annotate("", xy=(19-.2, 10.1), xytext=( 19+1 +.2, 10.1),  arrowprops=dict(arrowstyle="->"))
plt.text(20.4, 10-.3, '$V_{high}$', rotation=0, size=15)

plt.annotate("", xy=(19-.2, -6), xytext=( 19+1 +.2, -6),  arrowprops=dict(arrowstyle="->"))
plt.text(20.4, -6.4, '$V_{low}$', rotation=0, size=15)

plt.annotate("", xy=(19, -6), xytext=(19, 10.2),  arrowprops=dict(arrowstyle="<->"))
plt.text(19.2, 0.5, "$V_{amplitude}$", rotation=90, size=15)

plt.annotate("", xy=(30, -0.1), xytext=( 30, 2.7),  arrowprops=dict(arrowstyle="<->"))
plt.text(30.2, 0.2, "$V_{offset}$", rotation=90, size=15)


plt.axis([0, len(y), -11, 11])
plt.xlabel('Time')
plt.ylabel('Voltage')
# plt.title('ramp signal')
plt.grid(True)
#
plt.savefig("_rampProperties.pdf",  dpi=800)
# plt.show()
