import ZOOGrassModuleStarter as zoo
def r_terraflow(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.terraflow", inputs, outputs)
    return 1
