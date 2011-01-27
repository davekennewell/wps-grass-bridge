import ZOOGrassModuleStarter as zoo
def r_resample(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.resample", inputs, outputs)
    return 1
