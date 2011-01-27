import ZOOGrassModuleStarter as zoo
def r_volume(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.volume", inputs, outputs)
    return 1
