import arcpy
import datetime

ws = r""
arcpy.env.workspace = ws
fc = "LandParcels"

n = datetime.datetime.now()
outfile = open(r"", "w")

with arcpy.da.UpdateCursor(fc, "*") as Cursor:
    for x in Cursor:
        if x[2] > 100 and x[3] > 100:
            x[6] = ((x[2] - x[3]) / x[3]) * 100
            if x[6] < -3:
                x[7] = "A"
            if x[6] < 0 and x[6] >= -3:
                x[7] = "B"
            if x[6] == 0:
                x[7] = "C"
            if x[6] > 0 and x[6] <= 3:
                x[7] = "D"
            if x[6] > 3:
                x[7] = "E"
            Cursor.updateRow(x)
       
      


outfile.write(str(n))
outfile.close()
print "\nEnd of script."
            
    
