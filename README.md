# Photomosaic
<img src="https://raw.githubusercontent.com/SouravSharan/photomontage/master/ex1.jpeg"  height="300" width="425"/> <img src="https://raw.githubusercontent.com/SouravSharan/photomontage/master/ex2.jpeg"  height="300" width="425"/> 

Simple end-to-end python script to make cool mosaic posters made from scenes extracted from movies

# Tech Stack: 
* Python
* OpenCV
* NumPy

# How to run
python main.py --videoPath "PATH/TO/VIDEO.mp4" --posterPath "PATH/TO/POSTER.jpg"

Use high-resolution posters for best results.

# How does it work
Since this is a proof of concept which I hacked in an hour for fun, I used the most naive approach I could think of.
  ## Algorithm
    * Extract every nth frame from the video, resize it to (tx,ty) and store it in a directory
    * Find colour histograms of extracted images and store them in a pickle file
    * Iterate over the poster while comparing the histogram of every consecutive block of size (tx,ty) with the histograms stored in the pickle file. 
    * Replace that block with the most similar scene. 

Feel free to experiment with different histogram comparison methods or image similarity measures. 

## License
See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
