import cv2
path = r'D:\tuana\My Folder\AILearn\QuangNinh\GitFaceReconigtion\Example5\data\1_NguyenVanAnh_10A\4.jpg'
frame = cv2.imread(path)
# data\1_NguyenVanAnh_10A\1.jpg
cv2.imshow('frame',frame)
cv2.waitKey()
cv2.destroyAllWindows()
