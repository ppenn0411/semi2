import os
import pandas as pd

# 루트 데이터 폴더 경로 지정
root_data_dir = r"D:\semi2\Data"

# 분할 대상: train, val, test
splits = ['train', 'val', 'test']
labels = ['NORMAL', 'PNEUMONIA']

for split in splits:
    data_dir = os.path.join(root_data_dir, split)
    metadata = []

    for label in labels:
        label_dir = os.path.join(data_dir, label)
        for filename in os.listdir(label_dir):
            if filename.lower().endswith(('.jpeg', '.jpg', '.png')):
                metadata.append({
                    'filename': filename,
                    'label': label,
                    'label_normal': 1 if label == 'NORMAL' else 0,
                    'label_pneumonia': 1 if label == 'PNEUMONIA' else 0
                })

    df = pd.DataFrame(metadata)
    save_path = os.path.join(root_data_dir, f"{split}_metadata.csv")
    df.to_csv(save_path, index=False)
    print(f"[✓] {split}_metadata.csv saved to → {save_path}")
