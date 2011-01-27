import ZOOGrassModuleStarter as zoo
def r_watershed(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.watershed", inputs, outputs)
    return 1
