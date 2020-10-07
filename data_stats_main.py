import os
import json
import pandas as pd

from common_fun import common_fun
from data_stats_handler import data_stats_handler

class RunDataStats:
	def __init__(self):
		self.workfolder = './'
		self.data_stats_folder = common_fun.get_data_stats_folder()
		self.raw_full_data_folder = common_fun.get_raw_full_data_folder()
		self.data_folder = common_fun.get_data_folder()

	def run(self):
		# num of patients imaging
		file_path = oa.path.join(self.workfolder, 'jjw_hadmid_gender_age_ad1.csv')
		data_stats_handler.makePicBarh(file_path)
		# feature stats
		file_folder = self.raw_full_data_folder
		icuid_ad_file = os.path.join(self.data_folder, 'data_label.csv')
		save_path = os.path.join(self.data_stats_folder, 'feature_stats.json')
		
		feature_res = data_stats_handler.feature_statc(file_folder, icuid_ad_file)
		json.dump(feature_res, save_path)
		# missing value check

		# SVM, KNN, MLP, RF model result