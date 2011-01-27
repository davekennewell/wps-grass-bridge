import ZOOGrassModuleStarter as zoo
def v_sample(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.sample", inputs, outputs)
    return 1
