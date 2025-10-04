import os
import sys

class File:
	FileID: str
	FileHash: str
	FilePath: str
	def __init__(self, FilePath):
		self.FilePath = FilePath
		self.FileID = os.popen(fr"fsutil file queryfileid 'C:\Users\User\Desktop\Copier\test' ").read()

	def get_file_ID(self, FilePath):
		return os.popen(fr"fsutil file queryfileid {FilePath}").read().split(' ')[-1].replace('\n', '')


while True:
	if 