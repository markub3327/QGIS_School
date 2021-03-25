# define fields for feature attributes. A QgsFields object is needed
fields = QgsFields()
fields.append(QgsField("id", QVariant.Int))
fields.append(QgsField("Name", QVariant.String))

crs = QgsProject.instance().crs()
transform_context = QgsProject.instance().transformContext()
save_options = QgsVectorFileWriter.SaveVectorOptions()
save_options.driverName = "ESRI Shapefile"
save_options.fileEncoding = "UTF-8"

writer = QgsVectorFileWriter.create(
  "C:/Users/user/Desktop/skola/output_my.shp",
  fields,
  QgsWkbTypes.Polygon,
  crs,
  transform_context,
  save_options
)

if writer.hasError() != QgsVectorFileWriter.NoError:
    print("Error when creating shapefile: ",  writer.errorMessage())

# "layer" is a QgsVectorLayer instance
layer = iface.activeLayer()
features = layer.getFeatures()

for feature in features:
    # fetch geometry
    # show some information about the feature geometry
    geom = feature.geometry()
    geomSingleType = QgsWkbTypes.isSingleType(geom.wkbType())
    
    # fetch attributes
    attrs = feature.attributes()

    if attrs[0] != NULL:
        # add a feature
        fet = QgsFeature()

        fet.setGeometry(geom)
        fet.setAttributes([attrs[0], attrs[1]])
        writer.addFeature(fet)

        # retrieve every feature with its geometry and attributes
        print("Feature ID: ", feature.id())
        # attrs is a list. It contains all the attribute values of this feature
        print(attrs)
        print('Written successful\n')

del writer