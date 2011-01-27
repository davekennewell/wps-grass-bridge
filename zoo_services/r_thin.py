import ZOOGrassModuleStarter as zoo
def r_thin(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.thin", inputs, outputs)
    return 1
