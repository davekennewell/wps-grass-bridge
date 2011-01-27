import ZOOGrassModuleStarter as zoo
def v_transform(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.transform", inputs, outputs)
    return 1
