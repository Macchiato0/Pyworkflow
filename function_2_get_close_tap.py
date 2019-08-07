'''
select the tap points with LCP based on feederid
feederid in ('129802','051101','051102','060203','060204','140701','140702','026501','026502','077201','077202') and LCP is not Null
'''

import itertools

feederid=['129802','051101','051102','060203','060204','140701','140702','026501','026502','077201','077202']

#delete the lable of tap points to close to each other
def get_close_tap(feederid): 
    where="feederid='{}'".format(i)
    cursor=arcpy.da.SearchCursor("Tap Dots, T-points, & Wire Changes selection",["OID@","SHAPE@","LCP"],where)
    rows=[q for q in cursor]
    rows2=[]
    #find the taps with a label
    tap=[]
    for j in rows:     
        where="FEATUREID={}".format(j[0])
        cursor1=arcpy.da.SearchCursor(r'Misc Network Features\Feature Linked Anno\MiscNetworkFeature_Label_300',["SHAPE@"],where)
        cursor2=arcpy.da.SearchCursor(r'Misc Network Features\Feature Linked Anno\MiscNetworkFeature_Label_3200',["SHAPE@"],where)
        cursor3=arcpy.da.SearchCursor(r'Misc Network Features\Feature Linked Anno\MiscNetworkFeature_Label_600',["SHAPE@"],where)
        #apply try keywords to escape empty cursor error
        try:
            lable_shp300=[r1[0] for r1 in cursor1]
        except:
            pass
        try:
            lable_shp3200=[r2[0] for r2 in cursor2]
        except:
            pass
        try:
            lable_shp600=[r3[0] for r3 in cursor3]
        except:
            pass
        lable=lable_shp300+lable_shp3200+lable_shp600    
        if len(lable)>0:
            rows2.append(j)        
    for x,y in itertools.combinations(rows2, 2):
        if x[1].distanceTo(y[1])<400:
            tap.append(x[0])
            tap.append(y[0])
    tapr=list(set(tap))
    return tapr    
   
'''