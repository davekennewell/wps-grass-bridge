import ZOOGrassModuleStarter as zoo
def r_univar(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.univar", inputs, outputs)
    return 1
