import imutils
import cv2
from imutils.paths import list_images
import argparse
import pickle
import numpy as np
import os
import rgbhist

class Searcher:
	def __init__(self, index):
		self.index = index
 
	def search(self, queryFeatures):
		results = {}

		for (k, features) in self.index.items():
			d = self.histcmp_intersect(features, queryFeatures)
			results[k] = d
 
		key_max = max(results.keys(), key=(lambda k: results[k]))
		return (key_max, results[key_max])
		
	def chi2_distance(self, histA, histB, eps = 1e-10):
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])
 
		return d
	
	def histcmp_intersect(self, histA, histB):
		return cv2.compareHist(histA,histB,cv2.HISTCMP_INTERSECT)
