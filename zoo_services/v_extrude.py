import ZOOGrassModuleStarter as zoo
def v_extrude(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.extrude", inputs, outputs)
    return 1
