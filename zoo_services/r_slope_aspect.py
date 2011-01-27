import ZOOGrassModuleStarter as zoo
def r_slope_aspect(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.slope.aspect", inputs, outputs)
    return 1
