import ZOOGrassModuleStarter as zoo
def r_mult(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.mult", inputs, outputs)
    return 1
