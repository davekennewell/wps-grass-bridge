import ZOOGrassModuleStarter as zoo
def v_distance(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.distance", inputs, outputs)
    return 1
