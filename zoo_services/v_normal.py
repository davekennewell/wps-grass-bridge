import ZOOGrassModuleStarter as zoo
def v_normal(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.normal", inputs, outputs)
    return 1
