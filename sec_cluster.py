import sys
sys.getrecursionlimit()
sys.setrecursionlimit(100000)

fid='011004'
cursor=arcpy.da.SearchCursor('E:\\Data\\yfan\\Connection to dgsep011.sde\\ELECDIST.ElectricDist\\ELECDIST.SecOHElectricLineSegment',["OID@","SHAPE@","WIRETYPE"],"feederid='{}'".format(fid))
line_shp=[[i[0],[(int(i[1].firstPoint.X),int(i[1].firstPoint.Y)),(int(i[1].lastPoint.X),int(i[1].lastPoint.Y))],i[2]] for i in cursor]

line_all=[]
for i in line_shp:
    i.append(0)
    line_all.append(i)
#0 is oh
cursor=arcpy.da.SearchCursor('E:\\Data\\yfan\\Connection to dgsep011.sde\\ELECDIST.ElectricDist\\ELECDIST.SecUGElectricLineSegment',["OID@","SHAPE@","WIRETYPE"],"feederid='{}'".format(fid))
line_shp=[[i[0],[(int(i[1].firstPoint.X),int(i[1].firstPoint.Y)),(int(i[1].lastPoint.X),int(i[1].lastPoint.Y))],i[2]] for i in cursor]

#1 is underground 
for i in line_shp:
    i.append(1)
    line_all.append(i)


cluster=[]        
#cluster1=[line_shp[0]]
cluster1=[line_all[0]]
cluster2=[]
cluster3=[]

#include all oh and un sec line to the list
def find_line(lists):#lists=cluster1
    global cluster
    global cluster2
    global cluster1
    global cluster3
    global line_shp
    for l in lists:
        if l in line_all:
            line_all.remove(l)
    for i in line_all:
        for j in lists:
            if [a for a in i[1] if a in j[1]]:  
                if i not in lists:
                    cluster2.append(i)
    if len(cluster2)>0:
        cluster3=[]
        for h in cluster2:
            cluster1.append(h)
            cluster3.append(h)
        cluster2=[]
        #print cluster1
        find_line(cluster3)
    elif len(line_all)>0:
        cluster.append(cluster1)
        cluster3=[]
        cluster1=[line_all[0]]
        find_line(cluster1)
    else:
        cluster.append(cluster1)
        return len(cluster)

find_line(cluster1)

#find the tlm for each cluster
cursor=arcpy.da.SearchCursor('E:\\Data\\yfan\\Connection to dgsep011.sde\\ELECDIST.ElectricDist\\ELECDIST.Transformer',["SHAPE@","TLM"],"feederid='{}'".format(fid))
tlm_shp=[[str(i[1]),(int(i[0].firstPoint.X),int(i[0].firstPoint.Y))] for i in cursor]
#cluster_tlm=[]
def line_oh_tlm(oh_clust,tlm):#oh_clust is the element of cluster, tlm is the element of tlm_shp
    n=0
    for i in oh_clust:
        if [l for l in i[1] if l==tlm[1]]:
            n=n+1
    if n>0:
        for i in oh_clust:
            if len(i)==4:
                i.append(tlm[0])
            

for j in tlm_shp:
    for i in cluster:
        line_oh_tlm(i,j)

#add lines without TLM 'None'        
for i in cluster:
    for j in i:
        if len(j)<5:
            j.append('None')        
        
#find the sp for each cluster
cursor=arcpy.da.SearchCursor('E:\\Data\\yfan\\Connection to dgsep011.sde\\ELECDIST.ElectricDist\\ELECDIST.ServicePoint',["SHAPE@","DEVICELOCATION"],"feederid='{}'".format(fid))
sp_shp=[[i[1],(int(i[0].firstPoint.X),int(i[0].firstPoint.Y))] for i in cursor]

def line_oh_sp(tlm_clust,sp):#tlm_clust is the element of cluster_tlm(clust,tlm), sp is the element of sp_shp
    for i in tlm_clust:
        if [p for p in i[1] if p==sp[1]]:
            i.append(sp[0])

            
    
 #i[0] is line cluster, i[1] is tlm
for s in sp_shp:
    for clt in cluster:
        line_oh_sp(clt,s)

#add 'None' to sec lines without service point
for i in cluster:
    for j in i:
        if len(j) < 6:
            j.append('None')

#create table of oid,measured length,wire type,oh_un,tlm,device
def feet(l):#l contains 2 pts
    d=((l[0][0]-l[1][0])**2+(l[0][1]-l[1][1])**2)**0.5
    f=d*3.2808399
    return f


file_name='E:\\Data\\yfan\\tlm_sec\\{}.csv'.format(fid)
import csv 
with open(file_name, 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in cluster:#test_cluster=cluster
        for j in i:
            if j[3]==0:
                t="'{}'".format(j[4])
                row=[j[0],feet(j[1]),j[2],t,j[5]]
                filewriter.writerow(row)


                





