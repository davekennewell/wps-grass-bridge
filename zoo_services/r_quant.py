import ZOOGrassModuleStarter as zoo
def r_quant(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.quant", inputs, outputs)
    return 1
