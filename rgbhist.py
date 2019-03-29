import imutils
import cv2
from imutils.paths import list_images
import argparse
import pickle
import numpy as np
import os

class RGBHistogram:
	def __init__(self, bins):
		self.bins = bins
 
	def describe(self, image):
		hist = cv2.calcHist([image], [0, 1, 2],
			None, self.bins, [0, 256, 0, 256, 0, 256])
 
		if imutils.is_cv2():
			hist = cv2.normalize(hist)
 
		else:
			hist = cv2.normalize(hist,hist)
 
		return hist.flatten()

