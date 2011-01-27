import ZOOGrassModuleStarter as zoo
def r_resamp_interp(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.resamp.interp", inputs, outputs)
    return 1
