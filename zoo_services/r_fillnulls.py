import ZOOGrassModuleStarter as zoo
def r_fillnulls(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.fillnulls", inputs, outputs)
    return 1
