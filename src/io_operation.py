import shutil
import os
    
def copy_recursive(src, dst):
    list_dir = os.listdir(src)
    for file_name in list_dir:
        src_path = os.path.join(src, file_name)
        dst_path = os.path.join(dst, file_name)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        elif os.path.isdir(src_path):
            os.mkdir(dst_path)
            copy_recursive(src_path, dst_path)



def delete_directory_dst(dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    


