import ZOOGrassModuleStarter as zoo
def r_resamp_rst(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.resamp.rst", inputs, outputs)
    return 1
