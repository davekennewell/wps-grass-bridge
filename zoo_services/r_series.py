import ZOOGrassModuleStarter as zoo
def r_series(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.series", inputs, outputs)
    return 1
