import ZOOGrassModuleStarter as zoo
def r_neighbors(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.neighbors", inputs, outputs)
    return 1
