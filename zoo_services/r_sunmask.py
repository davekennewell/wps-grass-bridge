import ZOOGrassModuleStarter as zoo
def r_sunmask(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.sunmask", inputs, outputs)
    return 1
