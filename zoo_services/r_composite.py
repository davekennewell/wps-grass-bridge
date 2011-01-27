import ZOOGrassModuleStarter as zoo
def r_composite(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.composite", inputs, outputs)
    return 1
