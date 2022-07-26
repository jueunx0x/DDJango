# -*- coding: cp949 -*-
import tensorflow as tf
import cv2
import glob

#경로
model_path = '/Users/sinjueun/Downloads/?????/trash_classifier'#모델 경로
image_path = '/Users/sinjueun/Downloads/?????/for_test/캔.jpg'#이미지 경로

def prediction(image_path):
	# 사진 사이즈 맞추기
	img = cv2.imread(image_path)

	img = img/255

	#모델 input 맞추주기
	tensor_img = tf.convert_to_tensor(img,dtype=tf.float32)
	tensor_img = tf.image.resize(tensor_img,[224,224])
	tensor_img = tensor_img[tf.newaxis,...,]

	class_names = {0:'종이',1:'유리',2:'캔',3:'종이',4:'플라스틱',5:'일반쓰레기'}

	#모델로 예측하기
	return class_names[model.predict(tensor_img).argmax()]

if __name__ == '__main__':


	#모델 불러오기
	model = tf.keras.models.load_model(model_path)

	#이미지 로딩
	img = cv2.imread(image_path)

	#예측한 결과 프린트
	print('prediction for {} is :'.format(image_path.split('/')[-1]),end=' ')
	print(prediction(img))
