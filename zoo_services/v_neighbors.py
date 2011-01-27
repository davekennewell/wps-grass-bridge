import ZOOGrassModuleStarter as zoo
def v_neighbors(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.neighbors", inputs, outputs)
    return 1
