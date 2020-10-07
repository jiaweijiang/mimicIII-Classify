import os
import pandas as pd
from enum import Enum

from data_process_handler import data_process_handler
from common_fun import CommonFun


class InfoSystem(Enum):
	CAREVUE = 0
	METAVISION = 1


class FirstLine(Enum):
	FEATURELIST = 0
	DATALABEL = 1

class RunProcess:
	def __init__(self, time_length, size):
		self.workfolder = './'
		self.make_data_folder()
		self.carevue_data_path = './carevue_hadmid_icustayid.csv'
		self.meta_data_path = './meta_hadmid_icustayid.csv'
		self.data_process = data_process_handler
		self.time_length = time_length
		self.size = size
        self.common_fun = CommonFun(time_length=self.time_length)

		self.data_folder = self.common_fun.get_data_folder()
		self.raw_data_folder = self.common_fun.get_raw_data_folder()
		self.raw_full_data_folder = self.common_fun.get_raw_full_data_folder()
		self.heatmap_folder = self.common_fun.get_heatmap_folder()
		self.resize_heatmap_folder = self.common_fun.get_resize_heatmap_folder()

	def run(self):
		# get carevue raw data
		icustayid_list = pd.read_csv(self.carevue_data_path).ICUSTAY_ID.tolist()
		icustayid_list_checked = self.data_process.check_file(icustayid_list, self.raw_data_folder)
		for icustayid in icustayid_list_checked:
			raw_data = self.data_process.get_raw_data(icustayid, self.time_length, InfoSystem.CAREVUE.value)
			self.data_process.write_data_to_csv(FirstLine.FEATURELIST.value, raw_data, self.raw_data_folder)

		self.common_fun.press_any_key_continue('press any key to continue...')

		# get metavision raw data
		icustayid_list = pd.read_csv(self.meta_data_path).ICUSTAY_ID.tolist()
		icustayid_list_checked = self.data_process.check_file(icustayid_list, self.raw_data_folder)
		for icustayid in icustayid_list_checked:
			raw_data = self.data_process.get_raw_data(icustayid, self.time_length, InfoSystem.METAVISION.value)
			self.data_process.write_data_to_csv(FirstLine.FEATURELIST.value, raw_data, self.raw_data_folder)

		self.common_fun.press_any_key_continue('press any key to continue...')

		# handle missing value
		files = os.listdir(self.raw_data_folder)
		for file in files:
			if file.split('.')[1] == 'csv':
				raw_data_path = os.path.join(self.raw_data_folder, file)
				save_data_path = os.path.join(self.raw_full_data_folder, file)
				full_data = self.data_process.handle_missing_data(raw_data_path)
				self.data_process.write_data_to_csv(FirstLine.FEATURELIST.value, full_data, save_data_path)

		self.common_fun.press_any_key_continue('press any key to continue...')

		# get data label
		data_label_save_path = os.path.join(self.data_folder, 'data_label.csv')
		data_label = self.data_process.get_data_label(self.raw_full_data_folder)
		self.data_process.write_data_to_csv(FirstLine.DATALABEL.value, data_label, data_label_save_path)

		self.common_fun.press_any_key_continue('press any key to continue...')

		# data to heatmap
		files = os.listdir(self.raw_full_data_folder)
		for file in files:
			if file.split('.')[1] == 'csv':
				data_file_path = os.path.join(self.raw_full_data_folder, file)
				save_path = oa.path.join(self.heatmap_folder, file.split('.')[0]+'.png')
				self.data_process.data2image(data_file_path, save_path)

		self.common_fun.press_any_key_continue('press any key to continue...')

		# resize heatmap
		img_files= os.listdir(self.heatmap_folder)
		for img_file in img_files:
			if img_file.split('.')[1] == 'png':
				img_file_path = os.path.join(self.heatmap_folder, img_file)
				save_img_path = os.path.join(self.resize_heatmap_folder, img_file)
				self.data_process.resize_heatmap(img_file_path, save_img_path, self.size)

		self.common_fun.press_any_key_continue('press any key to continue...')
		print('data process is ok!')


if __name__ == '__main__':
    # TIMELENGTH: 提取病人数据的时间长度
    # SIZE: 最终热力图的大小
	TIMELENGTH = 24
	SIZE = (256, 256)

	run = RunProcess(TIMELENGTH, SIZE)
	run.run()
				






