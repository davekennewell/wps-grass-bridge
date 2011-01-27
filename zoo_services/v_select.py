import ZOOGrassModuleStarter as zoo
def v_select(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.select", inputs, outputs)
    return 1
