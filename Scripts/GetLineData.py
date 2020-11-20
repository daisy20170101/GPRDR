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
y180C169_b8pvd.CellArrays = ['Q']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

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

# create a new 'Ruler'
ruler1 = Ruler()

# destroy ruler1
Delete(ruler1)
del ruler1

# set active source
SetActiveSource(y180C169_b8pvd)

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=y180C169_b8pvd,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [-20000.0, -15000.0, 0.0]
plotOverLine1.Source.Point2 = [20000.0, 15400.0, 0.0]

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point1 = [-20000.0, 250.0, 0.0]
plotOverLine1.Source.Point2 = [20000.0, 250.0, 0.0]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1)

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.AmbientColor = [0.0, 0.0, 0.0]
plotOverLine1Display.ColorArrayName = [None, '']
plotOverLine1Display.OSPRayScaleArray = 'Q'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'None'
plotOverLine1Display.ScaleFactor = 2000.0
plotOverLine1Display.SelectScaleArray = 'None'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'None'
plotOverLine1Display.GaussianRadius = 100.0
plotOverLine1Display.SetScaleArray = ['POINTS', 'Q']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'Q']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.SelectionCellLabelFontFile = ''
plotOverLine1Display.SelectionPointLabelFontFile = ''
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
plotOverLine1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
plotOverLine1Display.DataAxesGrid.XTitleFontFile = ''
plotOverLine1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
plotOverLine1Display.DataAxesGrid.YTitleFontFile = ''
plotOverLine1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
plotOverLine1Display.DataAxesGrid.ZTitleFontFile = ''
plotOverLine1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
plotOverLine1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
plotOverLine1Display.DataAxesGrid.XLabelFontFile = ''
plotOverLine1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
plotOverLine1Display.DataAxesGrid.YLabelFontFile = ''
plotOverLine1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
plotOverLine1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
plotOverLine1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
plotOverLine1Display.PolarAxes.PolarAxisTitleFontFile = ''
plotOverLine1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
plotOverLine1Display.PolarAxes.PolarAxisLabelFontFile = ''
plotOverLine1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
plotOverLine1Display.PolarAxes.LastRadialAxisTextFontFile = ''
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [574, 799]
lineChartView1.ChartTitleFontFile = ''
lineChartView1.LeftAxisTitleFontFile = ''
lineChartView1.LeftAxisRangeMaximum = 6.66
lineChartView1.LeftAxisLabelFontFile = ''
lineChartView1.BottomAxisTitleFontFile = ''
lineChartView1.BottomAxisRangeMaximum = 6.66
lineChartView1.BottomAxisLabelFontFile = ''
lineChartView1.RightAxisRangeMaximum = 6.66
lineChartView1.RightAxisLabelFontFile = ''
lineChartView1.TopAxisTitleFontFile = ''
lineChartView1.TopAxisRangeMaximum = 6.66
lineChartView1.TopAxisLabelFontFile = ''

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(2, lineChartView1)

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1)

# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [0]
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['Q_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Q_0', 'Q_0', 'Q_1', 'Q_1', 'Q_2', 'Q_2', 'Q_3', 'Q_3', 'Q_4', 'Q_4', 'Q_5', 'Q_5', 'Q_6', 'Q_6', 'Q_7', 'Q_7', 'Q_8', 'Q_8', 'Q_9', 'Q_9', 'Q_10', 'Q_10', 'Q_11', 'Q_11', 'Q_12', 'Q_12', 'Q_13', 'Q_13', 'Q_14', 'Q_14', 'Q_15', 'Q_15', 'Q_16', 'Q_16', 'Q_17', 'Q_17', 'Q_18', 'Q_18', 'Q_19', 'Q_19', 'Q_20', 'Q_20', 'Q_21', 'Q_21', 'Q_22', 'Q_22', 'Q_23', 'Q_23', 'Q_24', 'Q_24', 'Q_25', 'Q_25', 'Q_26', 'Q_26', 'Q_27', 'Q_27', 'Q_28', 'Q_28', 'Q_29', 'Q_29', 'Q_30', 'Q_30', 'Q_31', 'Q_31', 'Q_32', 'Q_32', 'Q_33', 'Q_33', 'Q_34', 'Q_34', 'Q_35', 'Q_35', 'Q_36', 'Q_36', 'Q_37', 'Q_37', 'Q_38', 'Q_38', 'Q_39', 'Q_39', 'Q_40', 'Q_40', 'Q_41', 'Q_41', 'Q_42', 'Q_42', 'Q_Magnitude', 'Q_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Q_0', '0.89', '0.1', '0.11', 'Q_1', '0.22', '0.49', '0.72', 'Q_2', '0.3', '0.69', '0.29', 'Q_3', '0.6', '0.31', '0.64', 'Q_4', '1', '0.5', '0', 'Q_5', '0.65', '0.34', '0.16', 'Q_6', '0', '0', '0', 'Q_7', '0.89', '0.1', '0.11', 'Q_8', '0.22', '0.49', '0.72', 'Q_9', '0.3', '0.69', '0.29', 'Q_10', '0.6', '0.31', '0.64', 'Q_11', '1', '0.5', '0', 'Q_12', '0.65', '0.34', '0.16', 'Q_13', '0', '0', '0', 'Q_14', '0.89', '0.1', '0.11', 'Q_15', '0.22', '0.49', '0.72', 'Q_16', '0.3', '0.69', '0.29', 'Q_17', '0.6', '0.31', '0.64', 'Q_18', '1', '0.5', '0', 'Q_19', '0.65', '0.34', '0.16', 'Q_20', '0', '0', '0', 'Q_21', '0.89', '0.1', '0.11', 'Q_22', '0.22', '0.49', '0.72', 'Q_23', '0.3', '0.69', '0.29', 'Q_24', '0.6', '0.31', '0.64', 'Q_25', '1', '0.5', '0', 'Q_26', '0.65', '0.34', '0.16', 'Q_27', '0', '0', '0', 'Q_28', '0.89', '0.1', '0.11', 'Q_29', '0.22', '0.49', '0.72', 'Q_30', '0.3', '0.69', '0.29', 'Q_31', '0.6', '0.31', '0.64', 'Q_32', '1', '0.5', '0', 'Q_33', '0.65', '0.34', '0.16', 'Q_34', '0', '0', '0', 'Q_35', '0.89', '0.1', '0.11', 'Q_36', '0.22', '0.49', '0.72', 'Q_37', '0.3', '0.69', '0.29', 'Q_38', '0.6', '0.31', '0.64', 'Q_39', '1', '0.5', '0', 'Q_40', '0.65', '0.34', '0.16', 'Q_41', '0', '0', '0', 'Q_42', '0.89', '0.1', '0.11', 'Q_Magnitude', '0.22', '0.49', '0.72', 'vtkValidPointMask', '0.3', '0.69', '0.29', 'Points_X', '0.6', '0.31', '0.64', 'Points_Y', '1', '0.5', '0', 'Points_Z', '0.65', '0.34', '0.16', 'Points_Magnitude', '0', '0', '0']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'Q_0', '0', 'Q_1', '0', 'Q_2', '0', 'Q_3', '0', 'Q_4', '0', 'Q_5', '0', 'Q_6', '0', 'Q_7', '0', 'Q_8', '0', 'Q_9', '0', 'Q_10', '0', 'Q_11', '0', 'Q_12', '0', 'Q_13', '0', 'Q_14', '0', 'Q_15', '0', 'Q_16', '0', 'Q_17', '0', 'Q_18', '0', 'Q_19', '0', 'Q_20', '0', 'Q_21', '0', 'Q_22', '0', 'Q_23', '0', 'Q_24', '0', 'Q_25', '0', 'Q_26', '0', 'Q_27', '0', 'Q_28', '0', 'Q_29', '0', 'Q_30', '0', 'Q_31', '0', 'Q_32', '0', 'Q_33', '0', 'Q_34', '0', 'Q_35', '0', 'Q_36', '0', 'Q_37', '0', 'Q_38', '0', 'Q_39', '0', 'Q_40', '0', 'Q_41', '0', 'Q_42', '0', 'Q_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'Q_0', '1', 'Q_1', '1', 'Q_2', '1', 'Q_3', '1', 'Q_4', '1', 'Q_5', '1', 'Q_6', '1', 'Q_7', '1', 'Q_8', '1', 'Q_9', '1', 'Q_10', '1', 'Q_11', '1', 'Q_12', '1', 'Q_13', '1', 'Q_14', '1', 'Q_15', '1', 'Q_16', '1', 'Q_17', '1', 'Q_18', '1', 'Q_19', '1', 'Q_20', '1', 'Q_21', '1', 'Q_22', '1', 'Q_23', '1', 'Q_24', '1', 'Q_25', '1', 'Q_26', '1', 'Q_27', '1', 'Q_28', '1', 'Q_29', '1', 'Q_30', '1', 'Q_31', '1', 'Q_32', '1', 'Q_33', '1', 'Q_34', '1', 'Q_35', '1', 'Q_36', '1', 'Q_37', '1', 'Q_38', '1', 'Q_39', '1', 'Q_40', '1', 'Q_41', '1', 'Q_42', '1', 'Q_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'Q_0', '2', 'Q_1', '2', 'Q_2', '2', 'Q_3', '2', 'Q_4', '2', 'Q_5', '2', 'Q_6', '2', 'Q_7', '2', 'Q_8', '2', 'Q_9', '2', 'Q_10', '2', 'Q_11', '2', 'Q_12', '2', 'Q_13', '2', 'Q_14', '2', 'Q_15', '2', 'Q_16', '2', 'Q_17', '2', 'Q_18', '2', 'Q_19', '2', 'Q_20', '2', 'Q_21', '2', 'Q_22', '2', 'Q_23', '2', 'Q_24', '2', 'Q_25', '2', 'Q_26', '2', 'Q_27', '2', 'Q_28', '2', 'Q_29', '2', 'Q_30', '2', 'Q_31', '2', 'Q_32', '2', 'Q_33', '2', 'Q_34', '2', 'Q_35', '2', 'Q_36', '2', 'Q_37', '2', 'Q_38', '2', 'Q_39', '2', 'Q_40', '2', 'Q_41', '2', 'Q_42', '2', 'Q_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Q_0', '0', 'Q_1', '0', 'Q_2', '0', 'Q_3', '0', 'Q_4', '0', 'Q_5', '0', 'Q_6', '0', 'Q_7', '0', 'Q_8', '0', 'Q_9', '0', 'Q_10', '0', 'Q_11', '0', 'Q_12', '0', 'Q_13', '0', 'Q_14', '0', 'Q_15', '0', 'Q_16', '0', 'Q_17', '0', 'Q_18', '0', 'Q_19', '0', 'Q_20', '0', 'Q_21', '0', 'Q_22', '0', 'Q_23', '0', 'Q_24', '0', 'Q_25', '0', 'Q_26', '0', 'Q_27', '0', 'Q_28', '0', 'Q_29', '0', 'Q_30', '0', 'Q_31', '0', 'Q_32', '0', 'Q_33', '0', 'Q_34', '0', 'Q_35', '0', 'Q_36', '0', 'Q_37', '0', 'Q_38', '0', 'Q_39', '0', 'Q_40', '0', 'Q_41', '0', 'Q_42', '0', 'Q_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Q_30', 'Q_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Q_0', '0.889998', '0.100008', '0.110002', 'Q_1', '0.220005', '0.489998', '0.719997', 'Q_2', '0.300008', '0.689998', '0.289998', 'Q_3', '0.6', '0.310002', '0.639994', 'Q_4', '1', '0.500008', '0', 'Q_5', '0.650004', '0.340002', '0.160006', 'Q_6', '0', '0', '0', 'Q_7', '0.889998', '0.100008', '0.110002', 'Q_8', '0.220005', '0.489998', '0.719997', 'Q_9', '0.300008', '0.689998', '0.289998', 'Q_10', '0.6', '0.310002', '0.639994', 'Q_11', '1', '0.500008', '0', 'Q_12', '0.650004', '0.340002', '0.160006', 'Q_13', '0', '0', '0', 'Q_14', '0.889998', '0.100008', '0.110002', 'Q_15', '0.220005', '0.489998', '0.719997', 'Q_16', '0.300008', '0.689998', '0.289998', 'Q_17', '0.6', '0.310002', '0.639994', 'Q_18', '1', '0.500008', '0', 'Q_19', '0.650004', '0.340002', '0.160006', 'Q_20', '0', '0', '0', 'Q_21', '0.889998', '0.100008', '0.110002', 'Q_22', '0.220005', '0.489998', '0.719997', 'Q_23', '0.300008', '0.689998', '0.289998', 'Q_24', '0.6', '0.310002', '0.639994', 'Q_25', '1', '0.500008', '0', 'Q_26', '0.650004', '0.340002', '0.160006', 'Q_27', '0', '0', '0', 'Q_28', '0.889998', '0.100008', '0.110002', 'Q_29', '0.220005', '0.489998', '0.719997', 'Q_30', '0.300008', '0.689998', '0.289998', 'Q_31', '0.6', '0.310002', '0.639994', 'Q_32', '1', '0.500008', '0', 'Q_33', '0.650004', '0.340002', '0.160006', 'Q_34', '0', '0', '0', 'Q_35', '0.889998', '0.100008', '0.110002', 'Q_36', '0.220005', '0.489998', '0.719997', 'Q_37', '0.300008', '0.689998', '0.289998', 'Q_38', '0.6', '0.310002', '0.639994', 'Q_39', '1', '0.500008', '0', 'Q_40', '0.650004', '0.340002', '0.160006', 'Q_41', '0', '0', '0', 'Q_42', '0.889998', '0.100008', '0.110002', 'Q_Magnitude', '0.220005', '0.489998', '0.719997', 'vtkValidPointMask', '0.300008', '0.689998', '0.289998', 'Points_X', '0.6', '0.310002', '0.639994', 'Points_Y', '1', '0.500008', '0', 'Points_Z', '0.650004', '0.340002', '0.160006', 'Points_Magnitude', '0', '0', '0']
plotOverLine1Display_1.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Q_0', '0', 'Q_1', '0', 'Q_10', '0', 'Q_11', '0', 'Q_12', '0', 'Q_13', '0', 'Q_14', '0', 'Q_15', '0', 'Q_16', '0', 'Q_17', '0', 'Q_18', '0', 'Q_19', '0', 'Q_2', '0', 'Q_20', '0', 'Q_21', '0', 'Q_22', '0', 'Q_23', '0', 'Q_24', '0', 'Q_25', '0', 'Q_26', '0', 'Q_27', '0', 'Q_28', '0', 'Q_29', '0', 'Q_3', '0', 'Q_30', '0', 'Q_31', '0', 'Q_32', '0', 'Q_33', '0', 'Q_34', '0', 'Q_35', '0', 'Q_36', '0', 'Q_37', '0', 'Q_38', '0', 'Q_39', '0', 'Q_4', '0', 'Q_40', '0', 'Q_41', '0', 'Q_42', '0', 'Q_5', '0', 'Q_6', '0', 'Q_7', '0', 'Q_8', '0', 'Q_9', '0', 'Q_Magnitude', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Q_0', '1', 'Q_1', '1', 'Q_10', '1', 'Q_11', '1', 'Q_12', '1', 'Q_13', '1', 'Q_14', '1', 'Q_15', '1', 'Q_16', '1', 'Q_17', '1', 'Q_18', '1', 'Q_19', '1', 'Q_2', '1', 'Q_20', '1', 'Q_21', '1', 'Q_22', '1', 'Q_23', '1', 'Q_24', '1', 'Q_25', '1', 'Q_26', '1', 'Q_27', '1', 'Q_28', '1', 'Q_29', '1', 'Q_3', '1', 'Q_30', '1', 'Q_31', '1', 'Q_32', '1', 'Q_33', '1', 'Q_34', '1', 'Q_35', '1', 'Q_36', '1', 'Q_37', '1', 'Q_38', '1', 'Q_39', '1', 'Q_4', '1', 'Q_40', '1', 'Q_41', '1', 'Q_42', '1', 'Q_5', '1', 'Q_6', '1', 'Q_7', '1', 'Q_8', '1', 'Q_9', '1', 'Q_Magnitude', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Q_0', '2', 'Q_1', '2', 'Q_10', '2', 'Q_11', '2', 'Q_12', '2', 'Q_13', '2', 'Q_14', '2', 'Q_15', '2', 'Q_16', '2', 'Q_17', '2', 'Q_18', '2', 'Q_19', '2', 'Q_2', '2', 'Q_20', '2', 'Q_21', '2', 'Q_22', '2', 'Q_23', '2', 'Q_24', '2', 'Q_25', '2', 'Q_26', '2', 'Q_27', '2', 'Q_28', '2', 'Q_29', '2', 'Q_3', '2', 'Q_30', '2', 'Q_31', '2', 'Q_32', '2', 'Q_33', '2', 'Q_34', '2', 'Q_35', '2', 'Q_36', '2', 'Q_37', '2', 'Q_38', '2', 'Q_39', '2', 'Q_4', '2', 'Q_40', '2', 'Q_41', '2', 'Q_42', '2', 'Q_5', '2', 'Q_6', '2', 'Q_7', '2', 'Q_8', '2', 'Q_9', '2', 'Q_Magnitude', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Q_0', '0', 'Q_1', '0', 'Q_10', '0', 'Q_11', '0', 'Q_12', '0', 'Q_13', '0', 'Q_14', '0', 'Q_15', '0', 'Q_16', '0', 'Q_17', '0', 'Q_18', '0', 'Q_19', '0', 'Q_2', '0', 'Q_20', '0', 'Q_21', '0', 'Q_22', '0', 'Q_23', '0', 'Q_24', '0', 'Q_25', '0', 'Q_26', '0', 'Q_27', '0', 'Q_28', '0', 'Q_29', '0', 'Q_3', '0', 'Q_30', '0', 'Q_31', '0', 'Q_32', '0', 'Q_33', '0', 'Q_34', '0', 'Q_35', '0', 'Q_36', '0', 'Q_37', '0', 'Q_38', '0', 'Q_39', '0', 'Q_4', '0', 'Q_40', '0', 'Q_41', '0', 'Q_42', '0', 'Q_5', '0', 'Q_6', '0', 'Q_7', '0', 'Q_8', '0', 'Q_9', '0', 'Q_Magnitude', '0', 'arc_length', '0', 'vtkValidPointMask', '0']

# save data
SaveData('/import/freenas-m-05-seissol/dli/ExaHyPE/Obv/test2_12/linedata_y250.csv', proxy=plotOverLine1, WriteTimeSteps=1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 200.0, 10000.0]
renderView1.CameraFocalPoint = [0.0, 200.0, 0.0]
renderView1.CameraParallelScale = 25120.50954897213

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
