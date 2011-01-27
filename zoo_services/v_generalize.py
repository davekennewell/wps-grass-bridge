import ZOOGrassModuleStarter as zoo
def v_generalize(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.generalize", inputs, outputs)
    return 1
