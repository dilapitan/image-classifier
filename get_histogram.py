import cv2 as cv
import glob

subfolder = "Cajanus sp" # subject to change
directory = "pollimac_photos/" + subfolder

images = glob.glob(directory + "/*.jpg") # 'reads' all jpg files
images = sorted(images) # sort images

file = open("histograms.txt", "w") 

all_hist = [] # all histograms of 60 images per species
count_hist = 1
for image in images:

	file_name = image
	img = cv.imread(image, 0)	# read image
	temp_hist = cv.calcHist([img], [0], None, [256], [0,256]) # get histogram	

	# putting histogram to string histogram
	hist = []
	hist_len = 256 # range of histogram

	for i in range(0, hist_len):
		hist.append(temp_hist[i][0])
		
	all_hist.append(hist)

	# counter for histogram
	print(count_hist)
	count_hist += 1

	break

# writing all histograms of an images to file 
file.write(str(all_hist)) # converts array(histograms) to string

file.close()


