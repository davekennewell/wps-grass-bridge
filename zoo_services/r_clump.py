import ZOOGrassModuleStarter as zoo
def r_clump(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.clump", inputs, outputs)
    return 1
