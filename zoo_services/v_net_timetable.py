import ZOOGrassModuleStarter as zoo
def v_net_timetable(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.net.timetable", inputs, outputs)
    return 1
