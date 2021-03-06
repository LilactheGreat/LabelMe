EnhancedLabelMe

This is the revised LabelMe based on 4.1.1 version

<installtion>
1.
(Linux)
   
> pip install enhancedlabelme

(Windows : Run cmd as administrator)

> python -m pip install enhancedlabelme

2. you can start the program typing below command line

> labelme+

3. (to update)

> pip install enhancedlabelme --upgrade

<history>
   
v0.1 (200805)
- Added time keys to json data (loadTime, saveTime)
- Removed double click function when creating polygon

v0.2 (200806)
- Always dump jsons in utf-8 encoding
- "Save Automatically" is checked as default
- Added indication of work progress in the window title (# of images/# of jsons)
- Added the Preference in menu bar (File - Preference) and open config file.
   : You can change hotkey(단축키) in this config file. It will be applied after relaunch
   
v0.3 (200807)
- Labelme will launch in fullscreen mode as default

v0.4 (200810)
- Added the dark theme (menubar - View - Toggle dark theme)
  : To set dark theme as default, add below line in config file and relaunch
  > dark_mode: true

v0.6
- Fixed bug when reading json fails due to encoding

v0.7
- The enhanced labelme is separated from the labelme which means it will be installed as independent package.
  : you don't have to delete existing labelme from now on
  : Start enhanced labelme by typing below line in terminal
  > labelme+
- Fixed tool bar icon alignment

v0.8 (200811)
- Open config file with notepad.exe as default in Windows
- Cleaned some useless codes

v0.9 (200812)
- Fixed unexpected error when closing file
- Fixed writing wrong version to json(0.8.1 --> 4.1.1)
- Added drag & drop function (drag & drop to open image except folder)
- Added brightness & contrast adjustment function (View - Brightness Contrast)
- Added RGB indicator right to labellist (same color with polygon)
- Cleaned some codes

v0.9.5
- Fixed warning in terminal saying JSON file may be incompatible with 'current labelme'
- imageData & imagePath will be rewritten everytime json is loaded

v0.9.6
- Fixed Runtime Error when deleting multiple polygon labels
- Added crosshair when creating polygon
  : Fixed low framelate when showing crosshair

v1.0
- You can now toggle crosshair
  : You can add below line to config file to make it default
  > cross_hair: true
  : Also you can create hotkey for this by adding below line to config file under shortcuts
  > cross_hair: Ctrl+1
- Fixed error when opening euckr encoded json

v1.1
- Fixed Open File & Open Directory not showing up when cross hair is on

v1.2
- Added QtWidget above file search which shows the current file path + filename
  : Now you can copy the file path from it
- Fixed crash when double clicking item in Polygon Labels
- Added checking available update function in help menu bar

v1.3
- Now you can configure the style of cross hair (view - Cross-line Style)

v1.4
- Fixed unintentionally deleteing Polygon Labels during drag & drop

v1.5
- Added immersive mode which hides entire polygons except current creating polygon (view - Immersive Mode)
  ** IMPORTANT!!! ***
  : To enable, please add follow line to shortcuts section in config file
  > show_polygon: Ctrl+2

v1.6
- You can not toggle immersive mode while creating polygon anymore to prevent unexpected error
- Now the labelme application will be scaled based on the dpi of your screen

* To Do
- drag & drop folder
- Enable deleting elements from label list
- Use Qimage instead of Qpainter/QPixmap


@misc{labelme2016,
  author =       {Kentaro Wada},
  title =        {{labelme: Image Polygonal Annotation with Python}},
  howpublished = {\url{https://github.com/wkentaro/labelme}},
  year =         {2016}
}
