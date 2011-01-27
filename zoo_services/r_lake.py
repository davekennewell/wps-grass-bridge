import ZOOGrassModuleStarter as zoo
def r_lake(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.lake", inputs, outputs)
    return 1
