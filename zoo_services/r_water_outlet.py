import ZOOGrassModuleStarter as zoo
def r_water_outlet(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.water.outlet", inputs, outputs)
    return 1
