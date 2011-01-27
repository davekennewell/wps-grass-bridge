import ZOOGrassModuleStarter as zoo
def v_drape(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.drape", inputs, outputs)
    return 1
