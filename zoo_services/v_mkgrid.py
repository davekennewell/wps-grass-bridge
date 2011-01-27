import ZOOGrassModuleStarter as zoo
def v_mkgrid(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.mkgrid", inputs, outputs)
    return 1
