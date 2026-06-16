# Why these files exist

The .sh file is the executable file that will be run by the service
The .service file is the file that will be symbolically linked to the correct folder through the command:

```bash
sudo ln -s /home/legion/ros2_ws/src/Legion-Go-S-Joystick-Publisher/system_services/legion_joystick_node.service /etc/systemd/system/legion_joystick_node.service
```

And then activated with:
```bash
sudo systemctl daemon-reload
sudo systemctl enable legion_joystick_node.service
sudo systemctl start legion_joystick_node.service
```


If you change the file you will need to run
```bash
sudo systemctl daemon-reload
sudo systemctl restart legion_joystick_node.service
```


# Debugging / journalctl

Journalctl allows us to filter by a specific service unit `-u`flag + name 

The tailing `-f` flag stands for follow, so we have a live view of the logs
```bash
journalctl -u legion_joystick_node.service -f 
```