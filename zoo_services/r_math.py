import ZOOGrassModuleStarter as zoo
def r_math(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.math", inputs, outputs)
    return 1
