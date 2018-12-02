#読み込み
import bme280

#初期設定
bme280.setup()
bme280.get_calib_param()

#温度(℃),気圧(hPa),湿度(%)の順でタプルとして出てくるので、アンパックして変数に代入
temp,pres,hum =bme280.readData()

#各値を表示
print(temp)
print(pres)
print(hum)
