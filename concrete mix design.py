


#collecting data

grade = int(input("Enter the design grade: M"))
cement = input("Enter the type of cement used:")
a = int(input("Enter maximum nominal size of aggregate:"))
print("____________________________________________________________________________________________________________________________________________")
print("according to IS 456.2000 table 3 select the appropriate environmental condition.")
print("(1) Mild :")
print("(2) Moderate :")
print("(3) Severe :")
print("(4) Very Severe :")
print("(5) Extreme :")
print("____________________________________________________________________________________________________________________________________________")
envcon = int(input("Enter appropriate environmental condition (1/2/3/4/5) :"))
print("____________________________________________________________________________________________________________________________________________")
workability = int(input("Enter slump required:"))
print("____________________________________________________________________________________________________________________________________________")
print("method of placing:")
print("(1) pumpable")
print("(2) non pumpable")
print("____________________________________________________________________________________________________________________________________________")
methodOfPlacing = int(input("enter method of placing(1/2):"))
print("____________________________________________________________________________________________________________________________________________")
#admixtureType = input("Enter the type of chemical admixture:")
zone = int(input("enter the zone of fineaggregate(1/2/3/4):"))
spcement = float(input("enter the specific gravity of cement:"))
spag = float(input("enter the specific gravity of flyash/ggbs:"))
spcoarseaggregate = float(input("enter the specific gravity of coarse aggregate:"))
spfineaggregate = float(input("enter the specific gravity of fine aggregate:"))
spadmixture = float(input("enter the specific gravity of chemical admixture:"))
wacoarseaggregate =  float(input("enter the water absorption % of coarse aggregate:"))
wacoarseaggregate = wacoarseaggregate/100
wafineaggregate = float(input("enter the water absorption % of fine aggregate:"))
wafineaggregate = wafineaggregate/100
mcoarseaggregate = float(input("enter moisture content of coarse aggregate:"))
mcoarseaggregate = mcoarseaggregate/100
mfineaggregate = float(input("enter moisture content of fine aggregate:"))
mfineaggregate = mfineaggregate/100
print("____________________________________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________________________________")

#calculating target strength for mix proportioning:

#according to table 1 of IS 10262:2019
if (grade<20):
    x=5
elif (grade>15 and grade<30):
    x=5.5
elif (grade>25 and grade<65):
    x=6.5
else:
    x=8

#according to table 2 of IS 10262:2019
if (grade<20):
    s=3.5
elif (grade>15 and grade<30):
    s=4
elif (grade>25 and grade<65):
    s=5
else:
    s=6
    
fck1 = grade + (1.65*s)
fck2 = grade + x

if (fck1>fck2):
    fck=fck1
else:
    fck=fck2

print("target mean compressive strength at 28days, in N/mm2:",fck)
print("____________________________________________________________________________________________________________________________________________")

#calculation of approximate air content
#according to table 3 of IS 10262:2019
if (a==10):
    airpercent = 1.5
elif (a==20):
    airpercent = 1.0
elif (a==40):
    airpercent = 0.8
elif (a==80):
    airpercent = 0.3
elif (a==150):
    airpercent = 0.2

print("the amount of entrapped air to be expected in normal (non aired entrained) concrete is :",airpercent,"%")
print("____________________________________________________________________________________________________________________________________________")

#selection of water cement ratio
print("according to fig 1, ")
wc = float(input("w/c ratio required for the target strength is:"))

#according to table 5 of IS 456.2000

if (envcon==1):
    mincement = 300
    maxwc = 0.55
elif (envcon==2) :
    mincement = 300
    maxwc = 0.5
elif (envcon==3) :
    mincement = 320
    maxwc = 0.45
elif (envcon==4) :
    mincement = 340
    maxwc = 0.45
elif (envcon==5) :
    mincement = 360
    maxwc = 0.4

if (maxwc>wc):
    print("the w/c ratio is lower than the maximum value of",maxwc," according to the table 5 of IS 456.2000 . Therefore the w/c ratio is:",wc)
else:
    wc=maxwc
    print("the w/c ratio is higher than the maximum value of",maxwc," according to the table 5 of IS 456.2000 . Therefore the w/c ratio is:",wc)
print("____________________________________________________________________________________________________________________________________________")
#selection of water content
#according to table 4 of IS 10262:2019
    
if (a==10):
    watercontent = 208
elif (a==20):
    watercontent = 186
elif (a==40):
    watercontent = 165

#correction for the required slump

if  (workability<50):
    m = 50-workability
    watercontent = watercontent - (0.0012*m*watercontent)
elif (workability>50):
    m = workability-50
    watercontent = watercontent + (0.0012*m*watercontent)
else:
    watercontent = watercontent

#correction due to admixture
r=float(input("enter percentage of reduction in water content due to addition of admixture:"))
r=100-r
r=r/100
watercontent = watercontent*r

print("the water content is:",watercontent)
print("____________________________________________________________________________________________________________________________________________")
#calculation of cement content
cementcontent = watercontent/wc

if (cementcontent>mincement):
    print("the cement content ratio is higher than the minimum value of",mincement," according to the table 5 of IS 456.2000 . Therefore the cement content is:",cementcontent)
else:
    cementcontent=mincement
    print("the cement content ratio is lower than the minimum value of",mincement," according to the table 5 of IS 456.2000 . Therefore the cement content is:",cementcontent)

inc= float(input("enter if you want any increase in % cementitious content:"))
cementitiouscontent= cementcontent + (cementcontent*(inc/100))
per=float(input("enter the % of ggbs/flyash"))
agcontent = cementitiouscontent*(per/100)
cement = cementitiouscontent - agcontent
print("____________________________________________________________________________________________________________________________________________")
#proportion of volume of coarse aggregate and fine aggregate content
if (zone==1):
    if (a==10):
        c=0.48
    elif (a==20):
        c=0.6
    elif (a==40):
        c=0.69
elif (zone==2):
    if (a==10):
        c=0.5
    elif (a==20):
        c=0.62
    elif (a==40):
        c=0.71
elif (zone==3):
    if (a==10):
        c=0.52
    elif (a==20):
        c=0.64
    elif (a==40):
        c=0.72
elif (zone==4):
    if (a==10):
        c=0.54
    elif (a==20):
        c=0.66
    elif (a==40):
        c=0.73

#correction of coarse aggregate
if (wc>0.5):
    m=wc-0.5
    c = c - (m/5)
elif (wc<0.5):
    m=0.5-wc
    c= c + (m/5)
if (methodOfPlacing==1):
    c=c*0.9
f=1-c

#mix calculations
print("____________________________________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________________________________")
print("Mix Calculations")
print("Total volume = 1m3")
vair = airpercent/100
print("Volume of entrapped air in wet concrete =",vair,"m3")
vcement= (cement/spcement)/1000
print("Volume of cement =",vcement,"m3")
vwater= (watercontent/1)/1000
print("Volume of water =",vwater,"m3")
cheadmixture=cementitiouscontent/100
vadmixture = ((cheadmixture)/spadmixture)/1000
print("Volume of chemical admixture =",vadmixture,"m3")
vagcontent= (agcontent/spag)/1000
print("Volume of ggbs/flyash =",vagcontent,"m3")
vaggregate=1-vair-vcement-vwater-vadmixture-vagcontent
print("total volume of aggregate =",vaggregate,"m3")
vcaggregate= vaggregate*c
print("volume of coarse aggregate =",vcaggregate,"m3")
caggregate = vcaggregate*spcoarseaggregate*1000
print("mass of coarse aggregate =",caggregate,"kg")
vfaggregate= vaggregate*f
print("volume of fine aggregate =",vfaggregate,"m3")
faggregate = vfaggregate*spfineaggregate*1000
print("mass of fine aggregate =",faggregate,"kg")
print("____________________________________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________________________________")
#mix proportioning for trial number 1:
print("mix proportioning for trial number 1:")
print("cement = ",cement,"kg/m3")
print("flyash/ggbs = ",agcontent,"kg/m3")
print("water = ",watercontent,"kg/m3")
print("fine aggregate = ",faggregate,"kg/m3")
print("coarse aggregate = ",caggregate,"kg/m3")
print("chemical admixture = ",cheadmixture,"kg/m3")
print("free water cement ratio = ",wc)
print("____________________________________________________________________________________________________________________________________________")

#adjustment on water, fine aggregate and coarse aggregate(if the coarse and fine aggregate is in dry condition)

faggregatedry = faggregate/(1+wafineaggregate)
caggregatedry = caggregate/(1+wacoarseaggregate)

#extra water to be added for absorption by coarse and fine aggregate
exwcaggregate = caggregate - caggregatedry
exwfaggregate = faggregate - faggregatedry

watercontentdry = watercontent + exwcaggregate + exwfaggregate

print("mix proportion adjustment for dry aggregates:")
print("cement = ",cement,"kg/m3")
print("flyash/ggbs = ",agcontent,"kg/m3")
print("water = ",watercontentdry,"kg/m3")
print("fine aggregate(dry) = ",faggregatedry,"kg/m3")
print("coarse aggregate(dry) = ",caggregatedry,"kg/m3")
print("chemical admixture = ",cheadmixture,"kg/m3")
print("free water cement ratio = ",wc)
print("____________________________________________________________________________________________________________________________________________")

#adjustment on water, fine aggregate and coarse aggregate(if the coarse and fine aggregate is in wet condition)
if (mcoarseaggregate!=0 or mfineaggregate!=0):
    fmcaggregate = mcoarseaggregate - wacoarseaggregate
    fmfaggregate = mfineaggregate - wafineaggregate

    faggregatewet = faggregate*(1+fmfaggregate)
    caggregatewet = caggregate*(1+fmcaggregate)

#extra water to be added for absorption by coarse and fine aggregate
    exwcaggregate = caggregatewet - caggregate
    exwfaggregate = faggregatewet - faggregate

    watercontentwet = watercontent - exwcaggregate - exwfaggregate
    print("mix proportion adjustment for wet aggregates:")
    print("cement = ",cement,"kg/m3")
    print("flyash/ggbs = ",agcontent,"kg/m3")
    print("water = ",watercontentwet,"kg/m3")
    print("fine aggregate(wet) = ",faggregatewet,"kg/m3")
    print("coarse aggregate(wet) = ",caggregatewet,"kg/m3")
    print("chemical admixture = ",cheadmixture,"kg/m3")
    print("free water cement ratio = ",wc)
print("____________________________________________________________________________________________________________________________________________")
