import ZOOGrassModuleStarter as zoo
def v_rast_stats(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.rast.stats", inputs, outputs)
    return 1
