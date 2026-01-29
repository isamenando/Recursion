# This function lists all file paths in a nested directory structure.
# For example, given the input
# {"dir1": {
#     "file1.txt": None,
#     "subdir1": {
#         "file2.txt": None
#     }
# }},
# the function should return
# ["/dir1/file1.txt", "/dir1/subdir1/file2.txt"]
def list_files(parent_directory, current_filepath=""):
    file_paths = []
    for key in parent_directory:
        new_file_path = current_filepath + "/" + key
        val = parent_directory[key]
        if val is None:
            file_paths.append(new_file_path)
        else:
            file_paths.extend(list_files(val, new_file_path))
    return file_paths