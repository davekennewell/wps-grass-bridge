import ZOOGrassModuleStarter as zoo
def r_random(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.random", inputs, outputs)
    return 1
