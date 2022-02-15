import matplotlib.pyplot as plt
import numpy as np
# import matplotlib.ticker
import csv
nodes = np.array( [ [0, -5], [2, -3.75], [6, -1], [9, 5] ] )


points = np.array([
# 2.5Vpp	
	# Frequenz 		unten in mm 	oben in mm
[	50.   			,686		,		396    ],
[  60.14390997  	,	686		,		396	   ],
[  72.34579812   	,686		,		396    ],
[  87.02318338  	,	686     ,        396   ],
[  104.67829012	    ,686        ,     396      ],
[  125.91523313     , 686       ,      396     ],
[  151.4606889      , 686       ,      396     ],
[  182.18876073     , 686       ,      396     ],
[  219.15088845     , 686       ,      396     ],
[  263.61182608     , 686       ,      396     ],
[  317.09291868  	,686		,		397    ],
[  381.42415905  	,685		,		400		],
[  458.80680562  	,685		,		400    ],
[  551.88870419  	,686		,		398    ],
[  663.85489074		,686		,		398    ],
[  798.53657559  	,686		,		395    ],
[  960.54223816 	,685		,		395    ],
[1000, 556, 271],
[1100, 506, 240],
[1200, 480, 255],
[  1389.823897   	,634		,		445    ],
[  1671.78886663	,600		,		472    ],
[  2010.95838157 	,576		,		490    ],
[  2418.93799697 	,560		,		500	   ],
[  2909.68778212 	,550		,		506    ],
[  3500.        	,541		,		514    ]
])


points1Vpp = np.array([
	#1Vpp
	#	Frequenz 		unten in mm 	oben in mm
	[ 50.   			,475	,			573],
	[ 60.14390997  		,476	,			574],
	[ 72.34579812   	,478	,			575],
	[ 87.02318338  		,478	,			575],	
	[ 104.67829012		,479	,			575],	
	[ 125.91523313  	,479	,			575],	
	[ 151.4606889   	,479	,			575],	
	[ 182.18876073  	,479	,			575],	
	[ 219.15088845  	,479	,			576],
	[ 263.61182608  	,479	,			576],
	[ 317.09291868  	,480	,			577],
	[ 381.42415905  	,480	,			577],
	[ 458.80680562  	,481	,			578],
	[ 551.88870419  	,482	,			580],
	[ 663.85489074		,482 	,		581],
	[ 798.53657559  	,480 	,		583],
	[ 960.54223816 		,480 	,		585],
	[ 1155.41531783 	,480 	,		585],
	[ 1389.823897   	,484 	,		582],
	[ 1671.78886663		,493 	,		573],
	[ 2010.95838157 	,504 	,		562],
	[ 2418.93799697 	,513 	,		552],
	[ 2909.68778212 	,519 	,		546],
	[ 3500.        		,523 	,		541]
])


csvfn = "../messungen/Phase_2.5Vpp.csv"

phaseDat = np.genfromtxt(csvfn
                     , skip_header = 1
                #     , names=True
                     , delimiter = ',' 
                #, defaultfmt="var_%02i", autostrip = True, dtype = None, dtype = "|S5"
                # , dtype = float
				).transpose()

phaseFreqs = phaseDat[0]
phaseDelays = phaseDat[1]

phasePhi = []

for pt in phaseDat.transpose():
    phasePhi.append(-360*pt[0]*pt[1]*10**-6) # pho = 360° * f * delta_t

freq1Vpp = points1Vpp[:,0]
unten1Vpp = points1Vpp[:,2]
oben1Vpp = points1Vpp[:,1]
ampl1Vpp = -(oben1Vpp - unten1Vpp)


freq = points[:,0]
unten = points[:,2]
oben = points[:,1]
ampl2_5Vpp = oben - unten

# print(ampl2_5Vpp)
# print(freq)

minus13dB = 10**(-13/20)
# print(minus13dB, 1/np.sqrt(2), 10**(-3/20))
# print(20*np.log10(minus13dB), 20*np.log10(1/np.sqrt(2)), 20*np.log10(np.exp(-3/10)))
print("max Ausschlag 2.5Vpp: ", np.max(ampl2_5Vpp), "mm, -3dB davon: ", np.round(np.max(ampl2_5Vpp)/np.sqrt(2.0)), "mm",
      " -13dB davon: ", np.round(minus13dB*np.max(ampl2_5Vpp)), "mm" )
print("max Ausschlag 1Vpp: ", np.max(ampl1Vpp), "mm, -3dB davon: ", np.round(np.max(ampl1Vpp)/np.sqrt(2.0)), "mm")


fig, ax = plt.subplots(2,1)
ax[0].plot(freq, ampl2_5Vpp)
ax[0].set_xlabel("Frequenz in Hz, log")
ax[0].set_xscale('log')
ax[0].set_xticks([  100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000])
ax[0].set_ylabel("Auslenkung in mm, log")
ax[0].set_yscale('log')
ax[0].set_yticks([10, 20,30, 40, 50, 60, 70, 80, 90, 100, 200, 300])
ax[0].grid()
# ax[0].plot(freq1Vpp, ampl1Vpp)
ax[0].plot(1300,  206 , '+')    # -3dB @ 2.5Vpp
# ax[0].plot(1750,  74 , '+')     # -3dB @ 1.0Vpp

# ax[0].plot(2300,  66 , '+')    # -13dB
ax[0].plot(2000,  86 , '+')    #
ax[0].plot(3000,  41 , '+')    #

print(20*np.log10(41/86))

ax[1].plot(phaseFreqs, phasePhi)
ax[1].set_xscale('log')
# ax[1].set_yscale('log')
# ax[1].set_ylim(-200, 200)

# ax[1].set_yticks([-180, -90, 0 ,90, 180])
ax[1].set_yticks([0 ,-90, -180])
ax[1].set_ylabel("Phase in °")
ax[1].set_xlabel("Frequenz in Hz, log")
ax[1].grid()


# plt.show()
plt.savefig("Mess1log.png")
plt.savefig("Mess1log.pdf")
plt.savefig("Mess1log.eps")

np.savetxt("..\Mess1.csv", points, delimiter=' & ', fmt='%2.2e', newline=' \\\\\n')
