import os
import sys

import win32file, win32con

def get_file_id_info_pywin32(path: str):
	h = win32file.CreateFile(
		path,
		win32con.FILE_READ_ATTRIBUTES,
		win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
		None,
		win32con.OPEN_EXISTING,
		win32con.FILE_FLAG_BACKUP_SEMANTICS,
		None,
	)
	try:
		info = win32file.GetFileInformationByHandleEx(h, win32file.FileIdInfo)
		# info is a dict with 'VolumeSerialNumber' and 'FileId' (16-byte buffer)
		fid_bytes = bytes(info["FileId"])
		return {
			"volume_serial": info["VolumeSerialNumber"],
			"file_id_hex": fid_bytes.hex(),
			"file_id_int": int.from_bytes(fid_bytes, "little"),
		}
	finally:
		h.Close()

class File:
	FileID: str
	FileHash: str
	FilePath: str
	def __init__(self, FilePath):
		self.FilePath = FilePath
		self.FileID = os.popen(fr"fsutil file queryfileid 'C:\Users\User\Desktop\Copier\test' ").read()

	def get_file_ID(self, FilePath):
		return os.popen(fr"fsutil file queryfileid {FilePath}]").read().split(' ')[-1].replace('\n', '')



print(get_file_id_info_pywin32(r'C:\Users\User\Desktop\Copier\README.md'))
sys.exit(1)

WorkingDirectory = os.path.abspath(os.getcwd())
AuthToken = "Auth"
print(os.listdir(WorkingDirectory))
print(WorkingDirectory)
input("Press Enter to exit.")
sys.exit(1)