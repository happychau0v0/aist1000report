import sys
import os
import subprocess

import glob
import numpy as np
import wavio


def main():
    mainDir = os.getcwd();
    esc50_path = os.path.join(mainDir, 'datasets/esc50');

    if not os.path.exists:
        os.mkdir(esc50_path)

    subprocess.call('wget -P {} https://github.com/karoldvl/ESC-50/archive/master.zip'.format(esc50_path), shell=True)
    subprocess.call('unzip -d {} {}'.format(esc50_path, os.path.join(esc50_path, 'master.zip')), shell=True)
    os.remove(os.path.join(esc50_path, 'master.zip'))

    sr = 20000
    convert_sr(os.path.join(esc50_path, 'ESC-50-master', 'audio'), os.path.join(esc50_path, 'wav20'), sr);

    src_path = os.path.join(esc50_path, 'wav20')
    create_dataset(src_path, os.path.join(esc50_path, 'wav20.npz'))

def convert_sr(src_path, dst_path, sr):
    print('* {} -> {}'.format(src_path, dst_path))

    if not os.path.exists(dst_path):
        os.mkdir(dst_path)

    for src_file in sorted(glob.glob(os.path.join(src_path, '*.wav'))):
        dst_file = src_file.replace(src_path, dst_path)
        subprocess.call('ffmpeg -i {} -ac 1 -ar 20000 -loglevel error -y {}'.format(
            src_file, dst_file), shell=True)

def create_dataset(src_path, esc50_dst_path):
    print('* {} -> {}'.format(src_path, esc50_dst_path))
    esc50_dataset = {}

    for fold in range(1, 6):
        esc50_dataset['fold{}'.format(fold)] = {}
        esc50_sounds = []
        esc50_labels = []

        for wav_file in sorted(glob.glob(os.path.join(src_path, '{}-*.wav'.format(fold)))):
            sound = wavio.read(wav_file).data.T[0]
            start = sound.nonzero()[0].min()
            end = sound.nonzero()[0].max()
            sound = sound[start: end + 1]
            label = int(os.path.splitext(wav_file)[0].split('-')[-1])
            esc50_sounds.append(sound)
            esc50_labels.append(label)

        esc50_dataset['fold{}'.format(fold)]['sounds'] = esc50_sounds
        esc50_dataset['fold{}'.format(fold)]['labels'] = esc50_labels

    np.savez(esc50_dst_path, **esc50_dataset)


if __name__ == '__main__':
    main()
