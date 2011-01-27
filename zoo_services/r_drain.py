import ZOOGrassModuleStarter as zoo
def r_drain(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.drain", inputs, outputs)
    return 1
