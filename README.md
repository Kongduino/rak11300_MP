# rak11300_MP

Micropython environment for the RAK11300 (rp2040).

There's a [recent compile for RAK11300](https://github.com/mrpackethead/rak11300_micropython) by [user mrpackethead](https://github.com/mrpackethead/). Install this. After which, download / clone this repo and upload the files with Thonny (or ampy). The sensors are by default RAK's. Their I2C address can differ than the standard. *Caveat usor...* Here's an up-to-date list, fomr the `i2c_scan.py` file:

```python
knownDevices = {
  '0x18' : 'rak1904 proto / lis3dh', # proto is 0x18
  '0x19' : 'rak1904 / lis3dh',
  '0x2c' : 'rak12008 / stc31',
  '0x76' : 'rak1906 / bme680',
  '0x59' : 'rak12047 / sgp40',
  '0x5c' : 'rak1902 / lps22hb',
  '0x44' : 'rak1903 / opt3001',
  '0x5d' : 'rak12011 / lps33hw',
  '0x53' : 'rak12019 / ltr-390uv-01',
}
```

Note that support for rak12019 hasn't been implemented yet – it's a little more complex.

## Libraries

* `aes_lib`	convenience wrapper around `cryptolib`.
* `sx126x`	sx1261/2/8 LoRa library, from Github [user ehong](https://github.com/ehong-tl/micropySX126X). Modified and extend by me to work on rak11300.
* `bme280`	bme280, by Paul Cunnane and Peter Dahlebrg. I am modifying it a little to match syntax of bme680 library. WIP.
* `bme680[i]`	Adafruit's bme680 library
* `i2c_scan`	An I2C scanner that recognizes RAK sensors.
* `lis3dh`	Port of an old RAK library for RAK4600
* `lps22hb`	Very simple LPS22HB library
* `lps33hb`	Very simple LPS33HB library
* `opt3001`	OPT3001 light sensor library, converted from a C library
* `pinout`	RAK11300 pin names to numbers
* `sgp40`	SGP40 air quality sensor library, converted from a C library
* `voc_algorithm`	SGP40 algorithm implementation
* `stc3x`	STC31 CO2 sensor library



