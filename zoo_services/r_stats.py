import ZOOGrassModuleStarter as zoo
def r_stats(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.stats", inputs, outputs)
    return 1
