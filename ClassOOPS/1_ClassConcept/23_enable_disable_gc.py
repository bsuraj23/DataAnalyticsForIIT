# How to enable and disable Garbage Collector in our Program
import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
