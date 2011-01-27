import ZOOGrassModuleStarter as zoo
def v_net_components(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.net.components", inputs, outputs)
    return 1
