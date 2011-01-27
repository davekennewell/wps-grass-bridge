import ZOOGrassModuleStarter as zoo
def r_cost(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.cost", inputs, outputs)
    return 1
