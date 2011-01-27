import ZOOGrassModuleStarter as zoo
def r_ros(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.ros", inputs, outputs)
    return 1
