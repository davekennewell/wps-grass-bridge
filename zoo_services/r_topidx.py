import ZOOGrassModuleStarter as zoo
def r_topidx(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.topidx", inputs, outputs)
    return 1
