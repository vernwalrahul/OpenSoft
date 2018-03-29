import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
thresh = 10
font_size = 0.65
thickness = 1
def clear_image(img, co_ord, text_size):
	w, h = text_size[0]
	print("text_size = ",text_size[0])
	print("co_ord = ", co_ord)
	print("h, w = ",h,w)
	x1 = max(0, co_ord[0]-thresh)
	x2 = min(co_ord[0]+w+thresh, img.shape[1]-1)
	y1 = max(0, co_ord[1]-h-thresh)
	y2 = min(img.shape[0]-1, co_ord[1]+thresh)
	print(x1, x2, y1, y2)
	for i in range(x1, x2):
		for j in range(y1, y2):
			# print("i,j = ",i,j)
			img[j][i] = 255
	# cv2.imshow("cleared_img", img)		



def write_it(img, co_ord, text):
	text_size = cv2.getTextSize(text, font, font_size, 2)
	clear_image( img, co_ord, text_size)
	cv2.putText(img, text, co_ord, font, font_size, 0, thickness, cv2.LINE_AA)

def write(img, co_ords, texts):
	s = len(co_ords)
	for i in range(s):
		write_it(img, (co_ords[i][1],co_ords[i][0]), texts[i])

def main(img_path, co_ords, texts):
	print("img_path = ",img_path)
	img = cv2.imread(img_path, 0)
	cv2.imshow("original",img)
	write(img, co_ords, texts)
	cv2.imwrite("images/final.jpg",img)
	# cv2.imshow("final",img)
	# cv2.waitKey(0)		

if __name__=='__main__':
	img_path = "images/image23.jpg"
	co_ords = [(100,200),(140,200),(180,200),(220,200)]
	texts = ["medicine 1","medicine 2","medicine 3","medicine 4"]
	main(img_path, co_ords, texts)