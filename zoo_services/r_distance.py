import ZOOGrassModuleStarter as zoo
def r_distance(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.distance", inputs, outputs)
    return 1
