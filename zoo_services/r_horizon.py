import ZOOGrassModuleStarter as zoo
def r_horizon(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.horizon", inputs, outputs)
    return 1
