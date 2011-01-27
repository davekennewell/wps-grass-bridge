import ZOOGrassModuleStarter as zoo
def r_grow(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.grow", inputs, outputs)
    return 1
