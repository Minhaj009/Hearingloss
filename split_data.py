from pathlib import Path
import random
import shutil

random.seed(9)

SRC = Path("data/subjects") # created from build_subject_files.py 

train_path = Path("data/train")
val_path = Path("data/val")
test_path = Path("data/test")

# create directories
train_path.mkdir(parents=True, exist_ok=True)
val_path.mkdir(parents=True, exist_ok=True)
test_path.mkdir(parents=True, exist_ok=True)

subjects = sorted(SRC.glob("*.csv"))
random.shuffle(subjects)

# split subjects into 70% train, 15% val, 15% test
n_tot = len(subjects)
n_train = 37
n_val = 8
n_test = 8

train_subjects = subjects[:n_train]
val_subjects = subjects[n_train:n_train + n_val]
test_subjects = subjects[n_train + n_val:]

# copy files to directory (copy because entire dataset also needed)

#small copy function
def copy_files(subjects_file, dir):
    for f in subjects_file:
        shutil.copy(f, dir / f.name) #keep same name

copy_files(train_subjects, train_path)
copy_files(val_subjects, val_path)
copy_files(test_subjects, test_path)

print(f"Train: {len(train_subjects)} subjects, Val: {len(val_subjects)} subjects, Test: {len(test_subjects)} subjects") 
