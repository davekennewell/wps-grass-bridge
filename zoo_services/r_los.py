import ZOOGrassModuleStarter as zoo
def r_los(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.los", inputs, outputs)
    return 1
