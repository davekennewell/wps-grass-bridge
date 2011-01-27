import ZOOGrassModuleStarter as zoo
def r_carve(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.carve", inputs, outputs)
    return 1
