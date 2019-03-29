# Photomosaic
<img src="https://raw.githubusercontent.com/SouravSharan/photomontage/master/ex1.jpeg"  height="300" width="425"/> <img src="https://raw.githubusercontent.com/SouravSharan/photomontage/master/ex2.jpeg"  height="300" width="425"/> 

Simple end-to-end python script to make cool mosaic posters from scenes extracted from movies

# Tech Stack: 
* Python
* OpenCV
* NumPy

# How to run
python main.py --videoPath "~/PATH/TO/VIDEO.mp4" --posterPath "~/PATH/TO/POSTER.jpg"

Use high resolution posters for best results.

# How does it work
Since this is a proof of concept I used the most naieve approach I could think of.
  ## Algorithm
    * Extract every nth frame from the video, resize it to (tx,ty) pixels and store it in a directory
    * Find the colour histogram of each image and store them in a pickle file
    * Iterate over the poster, find histogram of every block of (tx,ty) pixels and compare it with the histograms stored in the pickle file
    * Replace that part with the scence having most simmilar histogram

Feel free to experiment with diffrent histogram comparison methods
