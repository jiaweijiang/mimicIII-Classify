import os
import csv

import cv2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from database_wrapper import database_wrapper

class DataProcessHandler:
	def __init__(self):
		self.database_wrapper = database_wrapper()
		self.carevue_itemid_list = [678, 52, 211, 618, 780, 837, 829, 813, 1127, 198]
		self.meta_itemid_list = [223761, 220052, 220045, 220210, 223830, 220645, 227442, 220545, 220546, 226755]
		self.feature_list_first_line = ['Temperature', 'Blood-pressure', 'Heart-rate', 'Respiration-rate', 'PH', 'Na+', 'K+', 'Hematocrit', 'WBC','GCS']
		self.data_label_first_line = ['ICUSTAY_ID', 'HOSPITAL_EXPIRE_FLAG']

	def get_raw_data(self, icustayid, time_length, info_system):
		if info_system == 0:
			itemid_list = self.carevue_itemid_list
		if info_system == 1:
			itemid_list = self.meta_itemid_list
		else:
			raise ValueError('info_system mast be 0 or 1')

		for itemid in itemid_list:
			res = self.database_wrapper.query_raw_data(icustayid, itemid)
			res_list = [list(i) for i in res]

			if len(res_list) == 0:
				res_list = [''] * time_length

			if len(res_list) < time_length:
				res_list = res_list.extend([''] * (time_length - len(res_list)))

			if len(res_list) > time_length:
				res_list = res_list[:time_length-1]

			raw_data.append(res_list)

		raw_data_transposition = []
		for i in range(len(raw_data[0])):
			temp_list = []
			for j in range(len(raw_data)):
				temp_list.append(raw_data[j][i])
			raw_data_transposition.append(temp_list)

		return raw_data_transposition				

	def get_data_label(self, data_without_missing_value_folder):
		icustayid_list = []
		data_label = []
		for file in os.listdir(data_without_missing_value_folder):
			if file.split('.')[1] == 'csv':
				icustayid_list.append(file.split('.')[0])

		for icustayid in icustayid_list:
			res = self.database_wrapper.query_data_label(icustayid)
			if len(res) == 0:
				data_label.append([icustayid, '-1'])
			else:
				data_label.append([icustayid, str(res[0])])

		return data_label	

	def data2image(self, data_file_path, save_path):
		try:
			data = pd.read_csv(file_path)
			data = data.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))

			fig = plt.figure()
			sns.heatmap(data, xticklabels='', yticklabels='', cbar=False)
			plt.savefig(save_path)
			print('{} is ok'.format(file.split('.')[0]))
		except Exception as e:
			print(e)
		finally:
			pass
		
	def check_file(self, icustayid_list, check_folder):
	files = os.listdir(check_folder)
	icustayidHas_list = []

	if len(files) == 0:
		print('files is null')
		return icustayid_list

	if len(files) > 0:
		print('files is not null')
		for file in files:
			filePath = os.path.join(check_folder, file)	
			if os.path.isfile(filePath):
				try:
					icustayidHas_list.append(file.split('.')[0])
				except:
					pass
		for icustayid in icustayidHas_list:
			if icustayid in icustayid_list:
				icustayid_list.remove(i)
		return icustayid_list

	def resize_heatmap(self, raw_image_path, save_img_path, size):
		img = cv2.imread(raw_image_path)
		img1 = cv2.resize(img, size)
		cv2.imwrite(save_img_path, img1)

	def write_data_to_csv(self, first_line_num, data, save_path, data):
		if first_line_num == 0:
			first_line = self.feature_list_first_line
		if first_line_num == 1:
			first_line = self.data_label_first_line
		else:
			raise ValueError('first_line_num mast be 0 or 1')

		with open(save_path, 'w', encoding='utf-8', newline='') as f:
			csv_writer = csv.writer(f)
			try:
				csv_writer.writerow(first_line)
				for i in data:
					csv_writer.writerow(i)
			except Exception as e:
				print(e)

	def handle_missing_data(self, raw_data_path):
		data = pd.read_csv(raw_data_path)
		data.fillna(data.mean(),inplace=True)
		data.fillna(0,inplace=True)
		return data


data_process_handler = DataProcessHandler()


