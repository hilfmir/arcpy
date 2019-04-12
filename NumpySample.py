import arcpy
import numpy

arcpy.env.workspace = r""

#Sum of tax collected for 2004 = 7% and 2006 = 8%. Land Parcels must be > 100 for both 
fc = "LandParcels"
f = open(r"", "w")
x = arcpy.da.FeatureClassToNumPyArray(fc, ('TaxVal06', 'TaxVal04'))

print numpy.sum(x[x["TaxVal04"] > 100]["TaxVal04"]*.07)
print numpy.sum(x[x["TaxVal06"] > 100]["TaxVal06"]*.08)


f.write("Tax collected for 2006 is $" + str((x['TaxVal06' ]*.08).sum()))
f.write("\nTax collected for 2004 is $" + str((x['TaxVal04' ]*.07).sum()))


f.close()
