import ZOOGrassModuleStarter as zoo
def r_gwflow(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.gwflow", inputs, outputs)
    return 1
