import ZOOGrassModuleStarter as zoo
def v_net_flow(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.net.flow", inputs, outputs)
    return 1
