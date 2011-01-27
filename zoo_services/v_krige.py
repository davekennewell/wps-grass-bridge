import ZOOGrassModuleStarter as zoo
def v_krige(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.krige", inputs, outputs)
    return 1
