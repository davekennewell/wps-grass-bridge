import ZOOGrassModuleStarter as zoo
def v_lidar_growing(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.lidar.growing", inputs, outputs)
    return 1
