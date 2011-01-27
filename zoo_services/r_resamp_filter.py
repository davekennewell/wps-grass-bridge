import ZOOGrassModuleStarter as zoo
def r_resamp_filter(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.resamp.filter", inputs, outputs)
    return 1
