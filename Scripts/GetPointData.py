# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
sh5o5pvd = PVDReader(FileName='/import/freenas-m-05-seissol/dli/ExaHyPE/Obv/test2_12/Y180C169_b8.pvd')
sh5o5pvd.CellArrays = ['Q']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()


# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1158, 799]

# show data in view
sh5o5pvdDisplay = Show(sh5o5pvd, renderView1)

# trace defaults for the display properties.
sh5o5pvdDisplay.Representation = 'Surface'
sh5o5pvdDisplay.AmbientColor = [0.0, 0.0, 0.0]
sh5o5pvdDisplay.ColorArrayName = [None, '']
sh5o5pvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
sh5o5pvdDisplay.SelectOrientationVectors = 'None'
sh5o5pvdDisplay.ScaleFactor = 2000.0
sh5o5pvdDisplay.SelectScaleArray = 'None'
sh5o5pvdDisplay.GlyphType = 'Arrow'
sh5o5pvdDisplay.GlyphTableIndexArray = 'None'
sh5o5pvdDisplay.GaussianRadius = 100.0
sh5o5pvdDisplay.SetScaleArray = [None, '']
sh5o5pvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
sh5o5pvdDisplay.OpacityArray = [None, '']
sh5o5pvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
sh5o5pvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
sh5o5pvdDisplay.SelectionCellLabelFontFile = ''
sh5o5pvdDisplay.SelectionPointLabelFontFile = ''
sh5o5pvdDisplay.PolarAxes = 'PolarAxesRepresentation'
sh5o5pvdDisplay.ScalarOpacityUnitDistance = 351.09611088860265

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
sh5o5pvdDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
sh5o5pvdDisplay.DataAxesGrid.XTitleFontFile = ''
sh5o5pvdDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
sh5o5pvdDisplay.DataAxesGrid.YTitleFontFile = ''
sh5o5pvdDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
sh5o5pvdDisplay.DataAxesGrid.ZTitleFontFile = ''
sh5o5pvdDisplay.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
sh5o5pvdDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
sh5o5pvdDisplay.DataAxesGrid.XLabelFontFile = ''
sh5o5pvdDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
sh5o5pvdDisplay.DataAxesGrid.YLabelFontFile = ''
sh5o5pvdDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
sh5o5pvdDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
sh5o5pvdDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
sh5o5pvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
sh5o5pvdDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
sh5o5pvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
sh5o5pvdDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
sh5o5pvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
sh5o5pvdDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
sh5o5pvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.0, 100.0, 10000.0]
renderView1.CameraFocalPoint = [0.0, 100.0, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=sh5o5pvd)

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)

# trace defaults for the display properties.
cellDatatoPointData1Display.Representation = 'Surface'
cellDatatoPointData1Display.AmbientColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.ColorArrayName = [None, '']
cellDatatoPointData1Display.OSPRayScaleArray = 'Q'
cellDatatoPointData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.SelectOrientationVectors = 'None'
cellDatatoPointData1Display.ScaleFactor = 2000.0
cellDatatoPointData1Display.SelectScaleArray = 'None'
cellDatatoPointData1Display.GlyphType = 'Arrow'
cellDatatoPointData1Display.GlyphTableIndexArray = 'None'
cellDatatoPointData1Display.GaussianRadius = 100.0
cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'Q']
cellDatatoPointData1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.OpacityArray = ['POINTS', 'Q']
cellDatatoPointData1Display.OpacityTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData1Display.SelectionCellLabelFontFile = ''
cellDatatoPointData1Display.SelectionPointLabelFontFile = ''
cellDatatoPointData1Display.PolarAxes = 'PolarAxesRepresentation'
cellDatatoPointData1Display.ScalarOpacityUnitDistance = 351.09611088860265

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
cellDatatoPointData1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.XTitleFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.YTitleFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.ZTitleFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.XLabelFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.YLabelFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleFontFile = ''
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelFontFile = ''
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextFontFile = ''
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(sh5o5pvd, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData('/import/freenas-m-05-seissol/dli/ExaHyPE/ShearBand/ng_shear5_vM_c172/pointdata.csv', proxy=cellDatatoPointData1, WriteTimeSteps=1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 100.0, 10000.0]
renderView1.CameraFocalPoint = [0.0, 100.0, 0.0]
renderView1.CameraParallelScale = 12560.254774486066

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
