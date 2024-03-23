import subprocess
import pickle
import json
import csv
import sys#

aoa=[ -40.0, -20.0, -10.0, -5.0, 0.0, 5.0, 10.0, 20.0, 40.0]
elevons=[ -40.0, -20.0, -10.0, -5.0, 0.0, 5.0, 10.0, 20.0, 40.0]
mach=[ 0.01, 0.1, 0.2, 0.5, 0.9]

hdr=f"""RR_Aero_Aoa={aoa};
RR_Aero_Elevons={elevons};
RR_Aero_Mach={mach};
"""

with open('vspaero.sweep.pkl', 'rb') as fh:
    dat=pickle.load(fh)

def dat_get(a,e,m,p):
    for d in dat:
        if d['_aoa']==a and d['_elevons']==e and d['_mach']==m:
            return d[p]

print(hdr)

for p in ['CL','CDtot_t', 'CMy']:
    # print('];\n\n% ', p, '%'*40)
    for _mach in mach:
        print('];\n\n% ', p, ' mach',_mach, '%'*40)
        #sys.stdout.write('];\n')
        for _elevons in elevons:
            #print('row',_elevons)
            sys.stdout.write(';\n')
            for _aoa in aoa:
                r=dat_get(_aoa,_elevons,_mach, p)
                sys.stdout.write(f'{r} ')
                #print('col',_aoa)
                #print('val',r)
print('];')
