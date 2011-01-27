import ZOOGrassModuleStarter as zoo
def r_div(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.div", inputs, outputs)
    return 1
