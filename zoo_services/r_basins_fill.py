import ZOOGrassModuleStarter as zoo
def r_basins_fill(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.basins.fill", inputs, outputs)
    return 1
