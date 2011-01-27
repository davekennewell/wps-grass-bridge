import ZOOGrassModuleStarter as zoo
def r_flow(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.flow", inputs, outputs)
    return 1
