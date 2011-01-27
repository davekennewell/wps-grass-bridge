import ZOOGrassModuleStarter as zoo
def r_circle(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.circle", inputs, outputs)
    return 1
