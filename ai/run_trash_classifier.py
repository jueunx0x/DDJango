# -*- coding: cp949 -*-
import tensorflow as tf
import cv2
import glob

#���
model_path = '/Users/sinjueun/Downloads/?????/trash_classifier'#�� ���
image_path = '/Users/sinjueun/Downloads/?????/for_test/ĵ.jpg'#�̹��� ���

def prediction(image_path):
	# ���� ������ ���߱�
	img = cv2.imread(image_path)

	img = img/255

	#�� input �����ֱ�
	tensor_img = tf.convert_to_tensor(img,dtype=tf.float32)
	tensor_img = tf.image.resize(tensor_img,[224,224])
	tensor_img = tensor_img[tf.newaxis,...,]

	class_names = {0:'����',1:'����',2:'ĵ',3:'����',4:'�ö�ƽ',5:'�Ϲݾ�����'}

	#�𵨷� �����ϱ�
	return class_names[model.predict(tensor_img).argmax()]

if __name__ == '__main__':


	#�� �ҷ�����
	model = tf.keras.models.load_model(model_path)

	#�̹��� �ε�
	img = cv2.imread(image_path)

	#������ ��� ����Ʈ
	print('prediction for {} is :'.format(image_path.split('/')[-1]),end=' ')
	print(prediction(img))
