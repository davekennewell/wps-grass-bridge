import ZOOGrassModuleStarter as zoo
def r_fill_dir(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.fill.dir", inputs, outputs)
    return 1
