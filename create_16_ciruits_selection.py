import json
with open(r'E:\Data\yfan\sec_cir_update_24.json', 'rb') as fp:
    data_dict = json.load(fp)
'''
#get rid of feederid=='0'
for k in data_dict:
    if '0' in data_dict[k]:
        print k
        in_d=data_dict[k].index('0')
        data_dict[k].pop(in_d)

24244
where="SIXTEENTHSECTIONNAME like '{}%'".format(n)
cursor=arcpy.da.SearchCursor(r"CE Landbase\Sixteenth Section",["SHAPE@","SIXTEENTHSECTIONNAME"],where)


where="FEEDERID= '{}'".format(n)
cursor=arcpy.da.SearchCursor(r'Org Bounds\Circuit Boundaries',["FEEDERID","SHAPE@"],where)
'''
import copy
209230
sixteen_feed={}
for k in data_dict:
    if len(data_dict[k])<=1:
        fd1=copy.deepcopy(data_dict[k])
        where1="SIXTEENTHSECTIONNAME like '{}%'".format(k) 
        cursor1=arcpy.da.SearchCursor(r"CE Landbase\Sixteenth Section",["SIXTEENTHSECTIONNAME"],where1)
        for r1 in cursor1:
            sixteen_feed[r1]=copy.deepcopy(fd1)



circuit={}
cursor_circuit=arcpy.da.SearchCursor('Boundary_Feeder_GO',["SHAPE@","FEEDERID"])
for row in cursor_circuit:
    fd=row[1]
    shp=row[0]
    circuit[fd]=shp

#find circuits with more r=than one polygons, manually update the polygon shape of every circuit
cursor=arcpy.da.SearchCursor('Boundary_Feeder_GO',["FEEDERID"])
fl=[i[0] for i in cursor]
set([i for i in fl if fl.count(i)>1])

[u'115601', u'072102', u'069301', u'205001', u'099501', u'112401', u'084003', u'048101', u'096301', u'119401', u'077301', u'145501', u'058401']

FEEDERID='058401'
cursor=arcpy.da.SearchCursor("Boundary_Feeder_GO",["SHAPE@"])
for i in cursor:
    i
circuit['058401']=i[0]

FEEDERID='115601'
cursor=arcpy.da.SearchCursor("Boundary_Feeder_GO",["SHAPE@"])
for i in cursor:
    i
circuit['115601'].area

FEEDERID='099501'
cursor=arcpy.da.SearchCursor("Boundary_Feeder_GO",["SHAPE@"])
for i in cursor:
    i
circuit['099501']=i[0]

FEEDERID='112401'
cursor=arcpy.da.SearchCursor("Boundary_Feeder_GO",["SHAPE@"])
for i in cursor:
    i
circuit['112401']=i[0]

FEEDERID='205001'
cursor=arcpy.da.SearchCursor("Boundary_Feeder_GO",["SHAPE@"])
for i in cursor:
    i
circuit['205001']=i[0]

FEEDERID='048101'
cursor=arcpy.da.SearchCursor("Boundary_Feeder_GO",["SHAPE@"])
for i in cursor:
    i
circuit['048101'].area

FEEDERID='072102'
cursor=arcpy.da.SearchCursor("Boundary_Feeder_GO",["SHAPE@"])
for i in cursor:
    i
circuit['072102'].area

FEEDERID='069301'
cursor=arcpy.da.SearchCursor("Boundary_Feeder_GO",["SHAPE@"])
for i in cursor:
    i
circuit['069301'].area

FEEDERID='096301'
cursor=arcpy.da.SearchCursor("Boundary_Feeder_GO",["SHAPE@"])
for i in cursor:
    i
circuit['096301'].area


FEEDERID='119401'
cursor=arcpy.da.SearchCursor("Boundary_Feeder_GO",["SHAPE@"])
for i in cursor:
    i
circuit['119401']=i[0]

FEEDERID='077301'
cursor=arcpy.da.SearchCursor("Boundary_Feeder_GO",["SHAPE@"])
for i in cursor:
    i
circuit['077301'].area

FEEDERID='145501'
cursor=arcpy.da.SearchCursor("Boundary_Feeder_GO",["SHAPE@"])
for i in cursor:
    i
circuit['145501'].area

FEEDERID='084003'
cursor=arcpy.da.SearchCursor("Boundary_Feeder_GO",["SHAPE@"])
union_shp=[]
for i in cursor:
    union_shp.append(i[0])

a=union_shp[0]
b=union_shp[1]
c=a.union(b)

circuit['084003']=c

142157
#sixteen_feed={}
empty_zone=[]
n=0
import copy
for k in data_dict:
    if n%1000==0:
        print n
    n=n+1
    if len(data_dict[k])>1:
        feederid=copy.deepcopy(data_dict[k])
        feederid_set=set(feederid)                                            
        feederid_ls=list(feederid_set)
        fd2=copy.deepcopy(feederid_ls)
        fd2_poly=[]
        for f in fd2:
            fd2_poly.append(circuit[f])    
        nm=len(fd2)
        #print nm
        where2="SIXTEENTHSECTIONNAME like '{}%'".format(k) 
        cursor2=arcpy.da.SearchCursor(r"CE Landbase\Sixteenth Section",["SIXTEENTHSECTIONNAME","SHAPE@"],where2)        
        for r2 in cursor2:
            name_16=r2[0]                                               
            poly_16=r2[1]
            #print name_16,poly_16
            sixteen_feed[name_16]=[]        
            for nr in range(nm):               
                if poly_16.overlaps(fd2_poly[nr]) or fd2_poly[nr].contains(poly_16) or poly_16.contains(fd2_poly[nr]):
                    sixteen_feed[name_16].append(fd2[nr])
                    #print 't'
            if len(sixteen_feed[name_16])==0:
                empty_zone.append(name_16)
                            
#manually update the tiny circuit
