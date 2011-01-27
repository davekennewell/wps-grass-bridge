import ZOOGrassModuleStarter as zoo
def r_spreadpath(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.spreadpath", inputs, outputs)
    return 1
