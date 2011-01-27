import ZOOGrassModuleStarter as zoo
def v_net_steiner(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.net.steiner", inputs, outputs)
    return 1
