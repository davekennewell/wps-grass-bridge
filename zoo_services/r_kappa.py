import ZOOGrassModuleStarter as zoo
def r_kappa(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.kappa", inputs, outputs)
    return 1
