import arcpy

#set a workspace
aWS = r""
arcpy.env.workspace = aWS
print arcpy.env.workspace

#create a list
aFCLIST = arcpy.ListFeatureClasses()

#create text file
OutFile = open(r"", "w")
OutFile.write("There are {0} features \n".format(len(aFCLIST)))
#go through each data in database
for x in aFCLIST:
    #print x 
    #Get count of features of each dataset
    print arcpy.GetCount_management(x)
    #Describe feature of each dataset
    describe = arcpy.Describe(x)
    print describe.shapeType
    #Spatial reference
    print describe.SpatialReference.type

    if describe.SpatialReference.type == "Geographic":
        aType = "not projected!"
        
    else:
        aType = "projected!"
    OutFile.write("{0} feature class is {1} type and has {2} features. It is {3} \n ".format(x,describe.shapeType.lower(),arcpy.GetCount_management(x),aType))
OutFile.close()
print "\nEnd"
