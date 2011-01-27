import ZOOGrassModuleStarter as zoo
def r_add(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.add", inputs, outputs)
    return 1
