import ZOOGrassModuleStarter as zoo
def r_bitpattern(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.bitpattern", inputs, outputs)
    return 1
