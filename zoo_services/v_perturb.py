import ZOOGrassModuleStarter as zoo
def v_perturb(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.perturb", inputs, outputs)
    return 1
