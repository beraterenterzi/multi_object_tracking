# tracker

## Jetson TX2 Installation

You can reach Jetson TX2 Intallation in [here](https://www.clearpathrobotics.com/assets/guides/melodic/husky/jetson_tx2.html)

### After Jetson TX2 Installation, Install Requirements

`$ sudo apt-get update && upgrade`

`$ sudo apt-get install python3-pip`

`$ pip3 install opencv-python==4.5.4.60`

** Check installation OpenCV
```
$ python3
>>import cv2
>>cv2.__version__
'4.5.4'
```

`$ pip3 install opencv-contrib-python==4.5.4.60`

`$ pip3 install datetime`

## Single Object Tracking

` $ cd /home/moveonboxer/tracker/single_object_tracker`

` $ python3 single_object_tracker.py`

## Multi Object Tracking

` $ cd /home/moveonboxer/tracker/multi_object_tracker`

` $ python3 multi_object_tracking.py`

**Press 'T' for capture the object 
**Press 'Space' for start tracking
 











