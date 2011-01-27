import ZOOGrassModuleStarter as zoo
def v_voronoi(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.voronoi", inputs, outputs)
    return 1
