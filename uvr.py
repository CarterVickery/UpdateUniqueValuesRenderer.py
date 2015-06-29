# vcsRevalUniqueValueSymbologyUpdate.py
# Created on: 2015-05-13
# Author: Carter Vickery
# Description: Python script to update the Unique Value Symbology for the VCS Reval Layer used by an Internal Application
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

mxd = arcpy.mapping.MapDocument("D:\\Workspace\\Python\\VCSReval.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
RevalVCSlyr = arcpy.mapping.ListLayers (mxd, "VCS Reval",df)

for lyr in arcpy.mapping.ListLayers(mxd,"",df):
    if lyr.name == "VCS Reval":
       lyr.symbology.addAllValues()
arcpy.RefreshActiveView()
arcpy.RefreshTOC()
mxd.save()

del mxd
del RevalVCSlyr

	
# Write messages to a Text File
txtFile = open("D:\\Workspace\\Python\\vcsRevalUniqueValueSymbologyUpdate.txt","w")
txtFile.write (arcpy.GetMessages())
txtFile.close()		

