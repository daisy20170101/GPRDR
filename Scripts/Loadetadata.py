# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
y180C169_b8pvd = PVDReader(FileName='/import/freenas-m-05-seissol/dli/ExaHyPE/Obv/test2_12/Y180C169_b8.pvd')
y180C169_b8pvd.CellArrays = ['time', 'Q']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on y180C169_b8pvd

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1158, 799]

# show data in view
y180C169_b8pvdDisplay = Show(y180C169_b8pvd, renderView1)

# trace defaults for the display properties.
y180C169_b8pvdDisplay.Representation = 'Surface'
y180C169_b8pvdDisplay.AmbientColor = [0.0, 0.0, 0.0]
y180C169_b8pvdDisplay.ColorArrayName = [None, '']
y180C169_b8pvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
y180C169_b8pvdDisplay.SelectOrientationVectors = 'None'
y180C169_b8pvdDisplay.ScaleFactor = 4000.0
y180C169_b8pvdDisplay.SelectScaleArray = 'None'
y180C169_b8pvdDisplay.GlyphType = 'Arrow'
y180C169_b8pvdDisplay.GlyphTableIndexArray = 'None'
y180C169_b8pvdDisplay.GaussianRadius = 200.0
y180C169_b8pvdDisplay.SetScaleArray = [None, '']
y180C169_b8pvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
y180C169_b8pvdDisplay.OpacityArray = [None, '']
y180C169_b8pvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
y180C169_b8pvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
y180C169_b8pvdDisplay.SelectionCellLabelFontFile = ''
y180C169_b8pvdDisplay.SelectionPointLabelFontFile = ''
y180C169_b8pvdDisplay.PolarAxes = 'PolarAxesRepresentation'
y180C169_b8pvdDisplay.ScalarOpacityUnitDistance = 664.2595995611829

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
y180C169_b8pvdDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
y180C169_b8pvdDisplay.DataAxesGrid.XTitleFontFile = ''
y180C169_b8pvdDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
y180C169_b8pvdDisplay.DataAxesGrid.YTitleFontFile = ''
y180C169_b8pvdDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
y180C169_b8pvdDisplay.DataAxesGrid.ZTitleFontFile = ''
y180C169_b8pvdDisplay.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
y180C169_b8pvdDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
y180C169_b8pvdDisplay.DataAxesGrid.XLabelFontFile = ''
y180C169_b8pvdDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
y180C169_b8pvdDisplay.DataAxesGrid.YLabelFontFile = ''
y180C169_b8pvdDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
y180C169_b8pvdDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
y180C169_b8pvdDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
y180C169_b8pvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
y180C169_b8pvdDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
y180C169_b8pvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
y180C169_b8pvdDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
y180C169_b8pvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
y180C169_b8pvdDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
y180C169_b8pvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.0, 200.0, 10000.0]
renderView1.CameraFocalPoint = [0.0, 200.0, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(Input=y180C169_b8pvd)

# Properties modified on calculator1
calculator1.ResultArrayName = 'eta_t'
calculator1.Function = 'sqrt(0.5*0.5^2/32e9^2*0.5^2/Q_33*sqrt(3.0)*(Q_27*Q_27+Q_28*Q_28+Q_29*Q_29+2*Q_30*Q_30))'

# show data in view
calculator1Display = Show(calculator1, renderView1)

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.AmbientColor = [0.0, 0.0, 0.0]
calculator1Display.ColorArrayName = [None, '']
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 4000.0
calculator1Display.SelectScaleArray = 'None'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'None'
calculator1Display.GaussianRadius = 200.0
calculator1Display.SetScaleArray = [None, '']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = [None, '']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.SelectionCellLabelFontFile = ''
calculator1Display.SelectionPointLabelFontFile = ''
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityUnitDistance = 664.2595995611829

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.XTitleFontFile = ''
calculator1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.YTitleFontFile = ''
calculator1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.ZTitleFontFile = ''
calculator1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.XLabelFontFile = ''
calculator1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.YLabelFontFile = ''
calculator1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(y180C169_b8pvd, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on calculator1
calculator1.AttributeType = 'Cell Data'

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(calculator1Display, ('CELLS', 'eta_t'))

# rescale color and/or opacity maps used to include current data range
calculator1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'eta_t'
eta_tLUT = GetColorTransferFunction('eta_t')

# get opacity transfer function/opacity map for 'eta_t'
eta_tPWF = GetOpacityTransferFunction('eta_t')

animationScene1.GoToLast()

# rescale color and/or opacity maps used to exactly fit the current data range
calculator1Display.RescaleTransferFunctionToDataRange(False, True)

# save data
SaveData('/import/freenas-m-05-seissol/dli/ExaHyPE/Obv/test2_12/etadata.csv', proxy=calculator1, WriteTimeSteps=1)

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=calculator1)

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)

# trace defaults for the display properties.
cellDatatoPointData1Display.Representation = 'Surface'
cellDatatoPointData1Display.AmbientColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.ColorArrayName = ['POINTS', 'eta_t']
cellDatatoPointData1Display.LookupTable = eta_tLUT
cellDatatoPointData1Display.OSPRayScaleArray = 'eta_t'
cellDatatoPointData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.SelectOrientationVectors = 'None'
cellDatatoPointData1Display.ScaleFactor = 4000.0
cellDatatoPointData1Display.SelectScaleArray = 'eta_t'
cellDatatoPointData1Display.GlyphType = 'Arrow'
cellDatatoPointData1Display.GlyphTableIndexArray = 'eta_t'
cellDatatoPointData1Display.GaussianRadius = 200.0
cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'eta_t']
cellDatatoPointData1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.OpacityArray = ['POINTS', 'eta_t']
cellDatatoPointData1Display.OpacityTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData1Display.SelectionCellLabelFontFile = ''
cellDatatoPointData1Display.SelectionPointLabelFontFile = ''
cellDatatoPointData1Display.PolarAxes = 'PolarAxesRepresentation'
cellDatatoPointData1Display.ScalarOpacityFunction = eta_tPWF
cellDatatoPointData1Display.ScalarOpacityUnitDistance = 609.6866802625348

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
Hide(calculator1, renderView1)

# show color bar/color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(cellDatatoPointData1Display, ('POINTS', 'Q', '20'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(eta_tLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
cellDatatoPointData1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Q'
qLUT = GetColorTransferFunction('Q')

# get opacity transfer function/opacity map for 'Q'
qPWF = GetOpacityTransferFunction('Q')

# save data
SaveData('/import/freenas-m-05-seissol/dli/ExaHyPE/Obv/test2_12/etadata.csv', proxy=cellDatatoPointData1, WriteTimeSteps=1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 200.0, 10000.0]
renderView1.CameraFocalPoint = [0.0, 200.0, 0.0]
renderView1.CameraParallelScale = 25120.50954897213

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
