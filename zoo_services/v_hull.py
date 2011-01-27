import ZOOGrassModuleStarter as zoo
def v_hull(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.hull", inputs, outputs)
    return 1
