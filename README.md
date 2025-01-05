# imgsorter
A python program for sorting jpgs, jpegs, and pngs into landscape, portrait, or square folders based on the file dimension ratios
If you have a folder of thousands of photos that you need to sort by their dimensions and move to separate folders, this will do so. If you have some that you want to sort into a wallpaper folder of images that are 16 by 9, this will create a folder within landscape and sort those first.

# abstractor
This script takes two numerical arguments, the first being a contrast value, the second being a brightness value. Add your own /path/to/image/directory to the script.
This will calculate the images' contrast and brightness profiles and return a list of files in plaintext.
For instance, you could add it into a one-liner that looks for images with a contrast higher than 30 and a brightness less than 600 and sort accordingly:

con_bright.sh:
```
#!/bin/sh

mkdir $1_$2
cd $1_#2
/path/to/abstractor $1 $2 | sed -e 's/\/home/cp \/home/g' -e 's/png/png ./g' | sh
```
Ex: ./con_bright.sh 30 600

You could amend the code to take a third argument being the path of the image directory you want on the fly, but I might look into that later.
