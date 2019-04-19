import arcpy, numpy
arcpy.env.workspace = r""

fc = "LandParcels"
query = 'Zone = \'Zone D\''

x = arcpy.da.FeatureClassToNumPyArray(fc, "TaxValue06", query)
n = [numpy.square(i) for i in x['TaxValue06']]
    sum = numpy.sum(n)
    sqrt = numpy.sqrt(sum)
    items = [(i / sqrt) for i in x['TaxValue06']]
    
    for i in items:
        print i



