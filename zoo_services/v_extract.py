import ZOOGrassModuleStarter as zoo
def v_extract(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.extract", inputs, outputs)
    return 1
