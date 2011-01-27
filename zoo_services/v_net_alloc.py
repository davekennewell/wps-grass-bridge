import ZOOGrassModuleStarter as zoo
def v_net_alloc(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.net.alloc", inputs, outputs)
    return 1
