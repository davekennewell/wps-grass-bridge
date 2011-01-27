import ZOOGrassModuleStarter as zoo
def r_resamp_stats(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.resamp.stats", inputs, outputs)
    return 1
