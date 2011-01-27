import ZOOGrassModuleStarter as zoo
def v_net_connectivity(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.net.connectivity", inputs, outputs)
    return 1
