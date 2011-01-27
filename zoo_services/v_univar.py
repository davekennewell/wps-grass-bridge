import ZOOGrassModuleStarter as zoo
def v_univar(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.univar", inputs, outputs)
    return 1
