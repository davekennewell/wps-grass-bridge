import ZOOGrassModuleStarter as zoo
def r_statistics(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.statistics", inputs, outputs)
    return 1
