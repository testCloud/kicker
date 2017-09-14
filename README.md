For the touchscreen to work we need to uncomment some configurations in `/boot/config.txt`
```
hdmi_group=2
hdmi_mode=16
hdmi_drive=2
```

More details: https://www.raspberrypi.org/documentation/configuration/config-txt/

I'm assuming you are currently inside the kicker repos root folder.
Also the kicker repo should be at `/home/pi/kicker`.

Install pip dependencies
`pip3 install -r backend/pip_packages`

Edit the crontab: `crontab -e`
* add `SHELL=/bin/bash` at the top
* add `@reboot bash /home/pi/kicker/backend/start.sh` at the bottom
