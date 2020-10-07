import os
import pandas as pd


class DataStatsHanlder:

	def __init__(self):
		self.save_dir = self.make_save_dirs()

	def makePicBarh(self, file_path):
		'''
		get row data 
		'''
		data = pd.read_csv(file_path)



		'''
		总体患者统计参数说明
		totalNum - icu患者总人数 
		maleNum - icu患者男性人数
		famaleNum - icu患者女性人数
		ageDistribution - 年龄分布，即每一个年龄对应的人数
		ageDistributionOfM - 男性年龄分布，即每一个年龄对应的男性人数
		ageDistributionOfF - 女性年龄分布，即每一个年龄对应的女性人数
		'''
		dataAge = data[data['AGE'] < 300 ]
		dataAge = dataAge[dataAge['AGE'] > 0]
		gender = data.GENDER.value_counts()

		maleNum = gender.M
		famaleNum = gender.F
		totalNum = maleNum + famaleNum
		ageDistribution = dataAge.AGE.value_counts()
		ageDistributionOfM = dataAge[dataAge['GENDER'] == 'M'].AGE.value_counts()
		#ageDistributionOfM = np.random.normal(loc=0.0,scale=1.0,size=1000)
		ageDistributionOfF = dataAge[dataAge['GENDER'] == 'F'].AGE.value_counts()
		ageMean = dataAge['AGE'].mean()
		'''
		生存患者统计参数说明
		aliveNum - icu患者活着的人数
		maleNumOfAlive - icu活着的男性人数
		famaleNumOfAlive - icu活着的女性人数
		ageDistributionOfAlive - 幸存者年龄分布，即每一个年龄对应的活着的人数
		'''
		dataOfAlive = data[data['HOSPITAL_EXPIRE_FLAG'] == 0]
		genderOfAlive = dataOfAlive.GENDER.value_counts()

		maleNumOfAlive = genderOfAlive.M
		famaleNumOfAlive = genderOfAlive.F
		aliveNum = maleNumOfAlive + famaleNumOfAlive

		dataAgeOfAlive = dataOfAlive[dataOfAlive['AGE'] < 300]
		dataAgeOfAlive = dataAgeOfAlive[dataAgeOfAlive['AGE'] > 0]

		ageDistributionOfAlive = dataAgeOfAlive.AGE.value_counts()
		ageDistributionOfAliveM = dataAgeOfAlive[dataAgeOfAlive['GENDER'] == 'M'].AGE.value_counts()
		ageDistributionOfAliveF = dataAgeOfAlive[dataAgeOfAlive['GENDER'] == 'F'].AGE.value_counts()
		ageOfAliveMean = dataAgeOfAlive['AGE'].mean()

		'''
		死亡患者统计参数说明
		deathNum - icu患者死亡人数
		maleNumOfDeath - icu死亡的男性人数
		famaleNumOfDeath - icu死亡的女性人数
		ageDistributionOfDeath - 死亡者年龄分布，即每一个年龄对应的死亡的人数
		'''
		dataOfDeath = data[data['HOSPITAL_EXPIRE_FLAG'] == 1]
		genderOfDeath = dataOfDeath.GENDER.value_counts()

		maleNumOfDeath = genderOfDeath.M
		famaleNumOfDeath = genderOfDeath.F
		deathNum = maleNumOfDeath + famaleNumOfDeath

		dataAgeOfDeath = dataOfDeath[dataOfDeath['AGE'] < 300]
		dataAgeOfDeath = dataAgeOfDeath[dataAgeOfDeath['AGE'] > 0]

		ageDistributionOfDeath = dataAgeOfDeath.AGE.value_counts()
		ageDistributionOfDeathM = dataAgeOfDeath[dataAgeOfDeath['GENDER'] == 'M'].AGE.value_counts()
		ageDistributionOfDeathF = dataAgeOfDeath[dataAgeOfDeath['GENDER'] == 'F'].AGE.value_counts()
		ageOfDeathMean = dataAgeOfDeath['AGE'].mean()

		y = ['Famale', 'Male']
		width = [famaleNum, maleNum]
		widthAlive = [famaleNumOfAlive,maleNumOfAlive]
		widthDeath = [famaleNumOfDeath,maleNumOfDeath]
		color = ['red', 'green','blue']
		plt.style.use('ggplot')
		fig = plt.figure(constrained_layout=True,figsize=(10,6))
		pic = fig.add_gridspec(4, 4)
		#图一
		fig_ax1 = fig.add_subplot(pic[:2, :])
		fig_ax1.set_title('Statistics for Male and Famale')
		#p0 = fig_ax1.barh(y[0],width[0],height=0.3,color=color[0])
		p0 = fig_ax1.barh(y[0],widthAlive[0],height=0.3,color=color[1])
		p1 = fig_ax1.barh(y[0],widthDeath[0],left=widthAlive[0],height=0.3,color=color[2])
		fig_ax1.text(12467-1200,0.2,'12467',fontsize=12)
		fig_ax1.text(14345-1200,0.2,'1878',fontsize=12)
		fig_ax1.text(0,0.2,'14345',fontsize=12)


		#p1 = fig_ax1.barh(y[1],width[1],height=0.3,color=color[0])
		p3 = fig_ax1.barh(y[1],widthAlive[1],height=0.3,color=color[1])
		p4 = fig_ax1.barh(y[1],widthDeath[1],left=widthAlive[1],height=0.3,color=color[2])
		fig_ax1.text(15612-1200,1.2,'15612',fontsize=12)
		fig_ax1.text(17965-1200,1.2,'2353',fontsize=12)
		fig_ax1.text(0,1.2,'17965',fontsize=12)
		p5 = fig_ax1.barh(0,0)
		p6 = fig_ax1.barh(1,0)

		#fig_ax1.annotate('{}'.format(width[0]),xy=(width[0]-2,y[0]))
		#fig_ax1.annotate('{}'.format(width[1]),xy=(width[1]-2,y[1]))
		#fig_ax1.legend(('red','green','blue'),('Total','Alive','Death'),loc='lower right')
		#图二
		x = np.arange(80)
		width = 0.2
		fig_ax2 = fig.add_subplot(pic[2:4, :2])
		fig_ax2.set_title('Overall Age Distribution')
		q0 = fig_ax2.bar(ageDistribution.index.tolist(),ageDistribution.values,color=color[0])
		fig_ax2.bar(ageDistributionOfAlive.index.tolist(),ageDistributionOfAlive.values,color=color[1])
		fig_ax2.bar(ageDistributionOfDeath.index.tolist(),ageDistributionOfDeath.values,color=color[2])
		fig_ax2.text(20,600,'Average age : {:.2f}'.format(dataAge.AGE.mean()))
		fig_ax2.vlines(dataAge.AGE.mean(),0,700,color='black',linestyles='--')
		#图三
		fig_ax3 = fig.add_subplot(pic[2, 2:])
		fig_ax3.set_title('Age Distribution for Male and Famale')
		fig_ax3.bar(ageDistributionOfM.index.tolist(),ageDistributionOfM.values,color=color[0])
		fig_ax3.bar(ageDistributionOfAliveM.index.tolist(),ageDistributionOfAliveM.values,color=color[1])
		fig_ax3.bar(ageDistributionOfDeathM.index.tolist(),ageDistributionOfDeathM.values,color=color[2])
		fig_ax3.text(15,300,'Average age for male : {:.2f}'.format(dataAge[dataAge['GENDER'] == 'M'].AGE.mean()))
		fig_ax3.vlines(dataAge[dataAge['GENDER'] == 'M'].AGE.mean(),0,400,color='black',linestyles='--')
		#图四
		fig_ax4 = fig.add_subplot(pic[3, 2:])
		fig_ax4.bar(ageDistributionOfF.index.tolist(),ageDistributionOfF.values,color=color[0])
		fig_ax4.bar(ageDistributionOfAliveF.index.tolist(),ageDistributionOfAliveF.values,color=color[1])
		fig_ax4.bar(ageDistributionOfDeathF.index.tolist(),ageDistributionOfDeathF.values,color=color[2])
		fig_ax4.text(15,300,'Average age for famale : {:.2f}'.format(dataAge[dataAge['GENDER'] == 'F'].AGE.mean()))
		fig_ax4.vlines(dataAge[dataAge['GENDER'] == 'F'].AGE.mean(),0,400,color='black',linestyles='--')

		save_path = os.path.join(self.save_dir, 'patients_statc.png')
		plt.savefig(save_path, dpi=200)

	def feature_statc(self, file_folder, icuid__ad_file):
		feature_list = ['Temperature','Blood-pressure','Heart-rate','Respiration-rate','PH','Na+','K+','Hematocrit','WBC','GCS']
		filespath = '../data/data_every_fulldata'
		result_list = {}
		icuidData = pd.read_csv('../data/icuid_ad1.csv')
		icuid_0 = icuidData[icuidData['HOSPITAL_EXPIRE_FLAG']==0].ICUSTAY_ID.values.tolist()
		icuid_1 = icuidData[icuidData['HOSPITAL_EXPIRE_FLAG']==1].ICUSTAY_ID.values.tolist()

		for feature in feature_list:
			temp_list = []
			for icuid in icuid_0:
				filepath = os.path.join(filespath,'{}.csv'.format(icuid))
				data = pd.read_csv(filepath)
				temp_list.extend(data[feature].values.tolist())

			temp_list_checked = [i for i in temp_list if i >= 0]
			min_value = str(np.min(temp_list_checked))
			max_value = str(np.max(temp_list_checked))
			median_value = str(np.median(temp_list_checked))
			result_list[feature] = [min_value, max_value, median_value]

		return result_list

	def missing_value_check(self):



data_stats_handler = DataStatsHanlder()


if __name__ == '__main__':
	pass







