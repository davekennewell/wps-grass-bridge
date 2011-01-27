import ZOOGrassModuleStarter as zoo
def v_net_distance(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.net.distance", inputs, outputs)
    return 1
