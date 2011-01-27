import ZOOGrassModuleStarter as zoo
def r_resamp_bspline(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.resamp.bspline", inputs, outputs)
    return 1
