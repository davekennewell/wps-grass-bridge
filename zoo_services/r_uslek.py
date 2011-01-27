import ZOOGrassModuleStarter as zoo
def r_uslek(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.uslek", inputs, outputs)
    return 1
