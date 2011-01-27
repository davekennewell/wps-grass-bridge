import ZOOGrassModuleStarter as zoo
def r_usler(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.usler", inputs, outputs)
    return 1
