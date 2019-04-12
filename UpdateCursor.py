import arcpy
import datetime

ws = r"C:\Users\Nico\Desktop\SCHOOL\SPRING2019\408E\Assignment_03\Assignment_03.gdb"
arcpy.env.workspace = ws
fc = "LandParcels"

n = datetime.datetime.now()
outfile = open(r"C:\Users\Nico\Desktop\SCHOOL\SPRING2019\408E\Assignment_03\Lab3.txt", "w")

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
       
      
del x
del Cursor

outfile.write(str(n))
outfile.close()
print "\nEnd of script."
            
    
