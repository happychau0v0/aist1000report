# aist1000 report code

Code borrowed from https://github.com/mohaimenz/acdnet

#### A.1 Prerequisits
1. Create `python 3.7+` development environment 
2. Install `torch 1.7.1` or higher.
2. Install `wavio 0.0.4` python library
3. Install `wget` for downloading ESC-50 over HTTP
4. Install `FFmpeg` for downsampling and upsampling audio recordings

##### Note
* This version of ACDNet is tested on Fedora 36.*

#### A.2 Dataset preparation
1. Download/clone the repository.
2. Go to the root of directory using the terminal.
3. To download and process ESC-50 dataset, run: ```python common/prepare_dataset.py```
4. Prepare the validation data, run: ```python common/val_generator.py```

*All the required data of ESC-50 for processing `20kHz` are now ready at `datasets/esc50` directory*

#### A.3 Training ACDNet (PyTorch)
*The experimented models is in `model/trained_fold1.pt` that can be used instead of training a new model.*

However, to conduct the training of a brand new ACDNet, run: ```python torch/trainer.py```