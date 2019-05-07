import P2D_fd
import numpy as np
# D1=1.5e-9,Dspref=7.5e-14,Dsnref=7.2e-14,
# >        Kappa=1.170027489,
# >        ctp=4.5829e4,ctn=3.0555e4,
# >        ep=0.4,es=0.45,en=0.38,efp=0.025,efn=0.03260,brugp=1.5,brugs=1.5,brugn=1.5,
# >        lp=43e-6,ls=16e-6,ln1=46.5e-6,Rpp=8e-6,Rpn=10e-6,
# >        kpref=1.334e-10,knref=1.0307e-10,
# >        c0=1200,F=96487,R=8.3143,t1=0.363,socp=0.424,socn=0.9867
# a = [1e-14, 1e-14, 51555.0, 30555.0, 8e-05, 8.8e-05, 2e-06, 2e-06, 303.15, 1000.0, 885000.0, 723600.0, 2.334e-11, 8.307e-12, 30.0, 30.0, 0.5, 1.0, 0.0, 10000.0, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 49503.111, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 305.55, 3.67873289259766, 0.18276374809384, 3.0596914450382, 30.0]
# [.15e-8, .72e-13, .75e-13, 96487, 1.170027489, 8.3143, .10e-4, .8e-5, 1.5, 1.5, 1.5, 1200, 30555., 45829., .3260e-1, .25e-1, .38, .4, .45, 17.1*ratetest, .10307e-9, .1334e-9, .465e-4, .43e-4, .16e-4, .9867, .424, .363]
#
# a = [0, .15e-8, .72e-13, .75e-13, .10e-4, .8e-5, 298.15, 1.5,1.5,1.5,  1200, 30555, 45829., .3260e-1,
# # efp, en,  ep,    es, iapp,     kn,         kp,     ln,      lp,     ls,    sigman, sigmap, t1, N1, N2, N3, Nr1, Nr2, CC
# .025, .38, .4, .45,      -1, .10307e-9, .1334e-9, .465e-4, .43e-4, .16e-4, 100, 10, .363, 7, 3, 7, 3, 3, 1]
a = [1.5e-09, 7.2e-14, 7.5e-14, 1e-05, 8e-06, 298.15, 1.5, 1.5, 1.5, 1200.0, 30555.0, 45829.0, 0.0326, 0.025, 0.38, 0.4, 0.45, 1.0307e-10, 1.334e-10, 4.65e-05, 4.3e-05, 1.6e-05, 100.0, 10.0, 0.363, 170, 30, 170, 40, 40, -1.0, 1.0, 1.0, 400.0]
a = np.array(a)
for i in range(len(a)):
	print(a[i], i)
N1 = a[25]
N2 = a[26]
N3 = a[27]
Nr1 = a[28]
Nr2 = a[29]
b = np.zeros((10000,int(5*N1+2*N2+5*N3+N1*Nr1+N3*Nr2+15)))
print(b.shape)
# print(b[:,0])
# for i in range(50)
# p2d_fd.model(a, b)
# # # print(b.shape)
import time
st = time.time()
# for i in range(50):
P2D_fd.model(a, b)
# print(b[:100,[0,-1]])
# print((time.time()-st)/50)
count = np.nonzero(b[1:,0])[0][-1]+1
print(count)
# # print(b[:,0])
# print(count)
# print(list(b[0]))
# for i in range(count+1):
# 	print(b[i,[0,-2, -1]])
# print(list(b[count]))

# from solve import spm_fd
# print(spm_fd(a[:21], initial=1.0))
