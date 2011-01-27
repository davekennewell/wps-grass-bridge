import ZOOGrassModuleStarter as zoo
def v_net_spanningtree(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.net.spanningtree", inputs, outputs)
    return 1
