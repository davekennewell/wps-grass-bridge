import ZOOGrassModuleStarter as zoo
def r_cross(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.cross", inputs, outputs)
    return 1
