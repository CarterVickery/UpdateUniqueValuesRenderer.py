# vcsRevalUniqueValueSymbologyUpdate.py
# Created on: 2015-05-21
# Author: Carter Vickery
# Description: Python script to update the Unique Value Symbology for the VCS Reval Layer used by RMaps and Restart the Map Service to pick up the new values
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

mxd = arcpy.mapping.MapDocument("D:\\Workspace\\Python\\VCSReval.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
RevalVCSlyr = arcpy.mapping.ListLayers (mxd, "VCS Reval",df)[0]

RevalVCSlyr.symbology.addAllValues()
arcpy.RefreshActiveView()
arcpy.RefreshTOC()
mxd.save()
