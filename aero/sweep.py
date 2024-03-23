import subprocess
import pickle
import json
import csv

cmd = '/Users/jrighetti/Downloads/OpenVSP-3.35.3-MacOS/vspaero'

model = 'RR_vsp_DegenGeom'


def aero_case(aoa, elevons, mach):
    return f"""Sref = 8.850000
Cref = 2.575000
Bref = 3.600000
X_cg = 0.732425
Y_cg = 0.000001
Z_cg = -0.000000
Mach = {mach}
AoA = {aoa}
Beta = 0.000000
Vinf = 100.000000
Rho = 0.002377
ReCref = 10000000.000000
ClMax = -1.000000
MaxTurningAngle = -1.000000
Symmetry = NO
FarDist = -1.000000
NumWakeNodes = 32
WakeIters = 5
NumberOfControlGroups = 1
elevons
Wing_Surf0_elevon,Wing_Surf1_elevon
-1, 1
{elevons}
Preconditioner = Matrix
Karman-Tsien Correction = N
Stability Type = 0
NumberOfQuadTrees = 1
1 2 0.000000
"""

aoa=[ -40.0, -20.0, -10.0, -5.0, 0.0, 5.0, 10.0, 20.0, 40.0]
elevons=[ -40.0, -20.0, -10.0, -5.0, 0.0, 5.0, 10.0, 20.0, 40.0]
mach=[ 0.01, 0.1, 0.2, 0.5, 0.9]


# aoa = [-40.0, 0.0, 40.0]
# elevons = [-40.0, 0.0, 40.0]
# mach = [0.01, 0.9]

result = []
for _mach in mach:
    for _elevons in elevons:
        for _aoa in aoa:
            print('#' * 40)
            print(f'case: aoa={_aoa} elevons={_elevons} mach={_mach}')
            with open(f'{model}.vspaero', 'w') as fh:
                fh.write(aero_case(_aoa, _elevons, _mach))
            r = subprocess.run([cmd, model], capture_output=True)
            print(r.returncode)
            with open(f'{model}.polar', 'r') as fh:
                dat = fh.read()
            lines = dat.split('\n')
            m = dict(zip(lines[0].split(), lines[1].split()))
            m['_mach'] = _mach
            m['_elevons'] = _elevons
            m['_aoa'] = _aoa
            result.append(m)
            print(m)

# with open('vspaero.sweep.json', 'wb') as fh:
#     json.dump(result, fh)

with open('vspaero.sweep.pkl', 'wb') as fh:
    pickle.dump(result, fh)

with open('vspaero.sweep.csv', 'w', newline='') as csvfile:
    fieldnames = result[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for r in result:
        writer.writerow(r)
