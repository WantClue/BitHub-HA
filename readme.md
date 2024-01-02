# SUPPORT MY WORK
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/R5R0IYN9V)

-------------------------------------------------------------------------------------------------------------------------------------------------

# How to use this component



To run this custom component for your HA integration you need to have HA Core or VM.
Activate the advanced mode in your user settings

Next step would be to install the Studio Code Server and add the folder `custom_components`

In the sensor.py change the `YOURBITAXEIP` to the ip of your Bitaxe

in the `configurtaion.yaml` file add the sensor:
```linux
sensor:
  - platform: bithub
    name: "BitaxeHub"
```
It will look like this
![bitaxehub](/picture/dashboard.png)