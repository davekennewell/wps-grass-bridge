import ZOOGrassModuleStarter as zoo
def r_rescale(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.rescale", inputs, outputs)
    return 1
