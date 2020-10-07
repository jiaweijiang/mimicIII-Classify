import sys
import os
import termios


class CommonFun:
   def __init__(self, time_length):
      self.workfolder = './'
      self.time_length = time_length
      self.make_data_folder()

   def press_any_key_continue(self, msg):
      # 获取标准输入的描述符
      fd = sys.stdin.fileno()
  
		# 获取标准输入(终端)的设置
      old_ttyinfo = termios.tcgetattr(fd)
  
   	# 配置终端
      new_ttyinfo = old_ttyinfo[:]
  
   	# 使用非规范模式(索引3是c_lflag 也就是本地模式)
      new_ttyinfo[3] &= ~termios.ICANON
   	# 关闭回显(输入不会被显示)
      new_ttyinfo[3] &= ~termios.ECHO
  
   	# 输出信息
      sys.stdout.write(msg+'\n')
      sys.stdout.flush()
   	# 使设置生效
      termios.tcsetattr(fd, termios.TCSANOW, new_ttyinfo)
   	# 从终端读取
      os.read(fd, 7)
  
   	# 还原终端设置
      termios.tcsetattr(fd, termios.TCSANOW, old_ttyinfo)

   def make_data_folder(self):
      data_folder = os.path.join(self.workfolder, 'data_process')
      if not os.path.isdir(data_folder):
         os.makedirs(data_folder)
      
      raw_data_folder = os.path.join(data_folder, 'raw_data')
      if not os.path.isdir(raw_data_folder):
         os.makedirs(raw_data_folder)

      raw_full_data_folder = os.path.join(data_folder, 'raw_full_data')
      if not os.path.isdir(raw_full_data_folder):
         os.makedirs(raw_full_data_folder)

      heatmap_folder = os.path.join(data_folder, 'heatmap', '{}_hours'.format(str(self.time_length)))
      if not os.path.isdir(heatmap_folder):
         os.makedirs(heatmap_folder)

      resize_heatmap_folder = os.path.join(data_folder, 'resize_heatmap', '{}_hours'.format(str(self.time_length)))
      if not os.path.isdir(resize_heatmap_folder):
         os.makedirs(resize_heatmap_folder)

      data_stats_folder = os.path.join(self.workfolder, 'data_stats')
      if not os.path.isdir(data_stats_folder):
         os.makedirs(data_stats_folder)

      self.data_folder = data_folder
      self.raw_data_folder = raw_data_folder
      self.raw_full_data_folder = raw_full_data_folder
      self.heatmap_folder = heatmap_folder
      self.resize_heatmap_folder = resize_heatmap_folder
      self.data_stats_folder = data_stats_folder

   def get_workfolder(self):
      return self.workfolder

   def get_data_folder(self):
      return self.data_folder

   def get_raw_data_folder(self):
      return self.raw_data_folder

   def get_raw_full_data_folder(self):
      return self.raw_full_data_folder

   def get_heatmap_folder(self):
      return self.heatmap_folder

   def get_resize_heatmap_folder(self):
      return self.resize_heatmap_folder

   def get_data_stats_folder(self):
      return self.data_stats_folder


if __name__ == '__main__':
   TIMELENGTH = 24
   common_fun = CommonFun(time_length=TIMELENGTH)
   common_fun.press_any_key_continue('press press_any_key_continue...')
   print('program exit!')


