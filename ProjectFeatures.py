import arcpy

#set ennvironment
ws = r"C:\Users\Nico\Desktop\SCHOOL\SPRING2019\408E\Assignment_02\Assignment_02.gdb"
arcpy.env.workspace = ws

#assign feature classes
fc = arcpy.ListFeatureClasses()
#sort feature count
fc.sort()

#create a text file
OutFile = open(r"C:\Users\Nico\Desktop\SCHOOL\SPRING2019\408E\Assignment_02\Lab2.txt","w")
#Describe each feature class
for x in fc:
    fc.sort()
    desc = arcpy.Describe(x)
    if desc.SpatialReference.type == "Geographic":
        type = "It is not projected. It has been projected to {0}".format(x.upper() + "_P")
        if arcpy.Exists(x + "_P"):
            arcpy.Delete_management(x + "_P")
            arcpy.Project_management(x, x + "_P", arcpy.SpatialReference(26945))
    else:
        type = "It is projected."
    OutFile.write("{0} feature class is {1} and has {2} features. {3} \n\n".format(x.upper(), desc.shapeType.lower(), arcpy.GetCount_management(x), type))
OutFile.close()
print "\nEnd of script"
    
