import arcpy
#arcpy.env.overwriteOutput = True
FolderPath = r"C:\Users\ndr83893\Desktop\NicoRome\Assignment_04"
currGDB = r"Assignment_04.gdb"
newGDB = r"PCS_Data.gdb"
arcpy.env.workspace = FolderPath + "\\" + currGDB
fc = arcpy.ListFeatureClasses()

'''
arcpy.Delete_management(arcpy.CreateFileGDB_management(FolderPath, newGDB))

for x in fc:
    dc = arcpy.Describe(x)
    project = dc.spatialReference.type
    output = FolderPath + "\\" + newGDB + "\\" + x + "_P"
    if project == "Geographic":
        arcpy.Delete_management(output)
        if arcpy.Exists(output):
            arcpy.Delete_management(output)
        arcpy.Project_management(x, output, 26945)
'''
shapefile = r"C:\Users\ndr83893\Desktop\NicoRome\Assignment_04\PCS_Data.gdb\SFV_BG_P"
arcpy.AddField_management(shapefile, "DI", "DOUBLE")

query = "POP_16 > 0"

with arcpy.da.UpdateCursor(shapefile, "DI", query) as cur:
    for y in cur:
        y[14] = 1- ((y[3]/y[4])**2 + ((y[3]/y[5])**2) + ((y[3]/y[6])**2) + ((y[3]/y[7])**2) + ((y[3]/y[8])**2) + ((y[3]/y[9])**2) + ((y[3]/y[10])**2) + ((y[3]/y[11])**2))
        cur.updateRow(y)
        

print "End"            
