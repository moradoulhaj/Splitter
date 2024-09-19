import shutil
import os

def zip_directory(directory_path, zip_name):
	shutil.make_archive(zip_name, 'zip', directory_path)