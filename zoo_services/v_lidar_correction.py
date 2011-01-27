import ZOOGrassModuleStarter as zoo
def v_lidar_correction(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.lidar.correction", inputs, outputs)
    return 1
