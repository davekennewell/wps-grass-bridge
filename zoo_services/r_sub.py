import ZOOGrassModuleStarter as zoo
def r_sub(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.sub", inputs, outputs)
    return 1
