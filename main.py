import \
	hashlib
import os
import sys

class File:
	FileID: str
	FileHash: str
	FilePath: str
	def __init__(self, FilePath):
		self.FilePath = FilePath
		self.FileID = os.popen(fr"fsutil file queryfileid 'C:\Users\User\Desktop\Copier\test' ").read()
		self.FileHash = self.get_file_hash()

	def get_file_ID(self, FilePath):
		return os.popen(fr"fsutil file queryfileid {FilePath}").read().split(' ')[-1].replace('\n', '')

	def get_file_hash(self):
		hash_md5 = hashlib.md5()
		with open(self.FilePath, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hash_md5.update(chunk)
		return hash_md5.hexdigest()


OldHashedList = []
NewHashedList = []
while True:
	if OldHashedList == []: # Populate the list for the first time
		for file in os.listdir(r"C:\Users\User\Desktop\Copier\test"):
			OldHashedList.append(File.get_file_hash())