import tarfile
import glob
import os
import os.path

index = 0
for f in glob.glob('*/layer.tar'):
    tf = tarfile.open(f)
    tf.extractall('.')
    tf.close()
    if os.path.exists('app/egg.png'):
        os.rename('app/egg.png', f'app/egg_{index}.png')
    index += 1
    
