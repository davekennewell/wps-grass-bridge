import ZOOGrassModuleStarter as zoo
def v_lidar_edgedetection(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.lidar.edgedetection", inputs, outputs)
    return 1
