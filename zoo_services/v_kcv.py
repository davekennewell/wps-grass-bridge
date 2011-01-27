import ZOOGrassModuleStarter as zoo
def v_kcv(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.kcv", inputs, outputs)
    return 1
