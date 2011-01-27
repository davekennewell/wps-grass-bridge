import ZOOGrassModuleStarter as zoo
def r_quantile(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.quantile", inputs, outputs)
    return 1
