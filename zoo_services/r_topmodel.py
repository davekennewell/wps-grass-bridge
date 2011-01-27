import ZOOGrassModuleStarter as zoo
def r_topmodel(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.topmodel", inputs, outputs)
    return 1
