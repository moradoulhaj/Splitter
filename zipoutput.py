import shutil
import os


def zip_directory(directory_path, zip_name):
	shutil.make_archive(zip_name, 'zip', directory_path)


# Example usage:
directory_to_zip = './output'  # Replace with your directory
zip_name = './zippedOutput/output'

zip_directory(directory_to_zip, zip_name)
