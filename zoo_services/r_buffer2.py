import ZOOGrassModuleStarter as zoo
def r_buffer2(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.buffer2", inputs, outputs)
    return 1
