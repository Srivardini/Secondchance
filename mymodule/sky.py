# Determine Andromeda location in ra/dec degrees
from math import cos,sin,pi
from random import uniform


# from wikipedia
def clip_to_radius():
    pass

def generate_sky_pos():

    ra = '00:42:44.3'
    dec = '41:16:09'

    # convert to decimal degrees


    d, m, s = dec.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = ra.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/cos(dec*pi/180)

    nsrc = 1_000_000

    # make 1000 stars within 1 degree of Andromeda

    ras = []
    decs = []
    for i in range(nsrc):
        ras.append(ra + uniform(-1,1))
        decs.append(dec + uniform(-1,1))


# now write these to a csv file for use by my other program
f = open('catalog.csv','w')
print("id,ra,dec", file=f)
for i in range(nsrc):
    print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}".format(i, ras[i], decs[i]), file=f)
