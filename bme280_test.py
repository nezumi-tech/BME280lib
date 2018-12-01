import bme280

bme280.setup()
bme280.get_calib_param()

temp,pres,hum =bme280.readData()
print(temp)
print(pres)
print(hum)