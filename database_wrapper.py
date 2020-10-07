import pymysql


class databaseInfo:
	def __init__(self, host, user, password, database):
		self.host = host
		self.user = user
		self.password = password
		self.database = database

	def connect_database(self):
		conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, database=self.database)
		cursor = conn.cursor()
		return cursor

	def close_connect(self):
		conn.close()


class database_wrapper:
	def __init__(self):
		database = databaseInfo(host='211.83.111.251', user='root', password='abcd1234!', database='mimiciii')
		cursor = database.connect_database()

	def query_raw_data(self, icustay_id, itemid):
		sql = 'SELECT ICUSTAY_ID, ITEMID, CHARTTIME, VALUENUM ' \
			  'FROM CHARTEVENTSA ' \
			  'WHERE ICUSTAY_ID = %s AND ITEMID = %s'

		res = cursor.execute(sql, (icustay_id, itemid))
		return res

	def get_data_label(self, icustay_id):
		sql = 'SELECT ICUSTAY_ID, HOSPITAL_EXPIRE_FLAG ' \
			  'FROM jjw_hadmid_gender_age_ad1 ' \
			  'WHERE ICUSTAY_ID = %s'

		res = cursor.execute(sql, (icustay_id))
		return res

if __name__ == '__main__':
	pass




