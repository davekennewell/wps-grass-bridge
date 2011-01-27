import ZOOGrassModuleStarter as zoo
def r_covar(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.covar", inputs, outputs)
    return 1
