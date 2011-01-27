import ZOOGrassModuleStarter as zoo
def r_transect(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.transect", inputs, outputs)
    return 1
