import ZOOGrassModuleStarter as zoo
def v_split(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.split", inputs, outputs)
    return 1
