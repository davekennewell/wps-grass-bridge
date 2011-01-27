import ZOOGrassModuleStarter as zoo
def v_reclass(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.reclass", inputs, outputs)
    return 1
