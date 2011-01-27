import ZOOGrassModuleStarter as zoo
def r_walk(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.walk", inputs, outputs)
    return 1
