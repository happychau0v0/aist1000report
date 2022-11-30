# AIST1000 report code

Code borrowed from https://github.com/mohaimenz/acdnet

#### A.1 Prerequisits
1. Create `python 3.7+` development environment 
2. Install `torch 1.7.1` or higher.
2. Install `wavio 0.0.4` python library
3. Install `wget` for downloading ESC-50 over HTTP
4. Install `FFmpeg` for downsampling and upsampling audio recordings

##### Note
* This version of ACDNet is tested on Fedora 36.

#### A.2 Dataset preparation
1. Download/clone the repository.
2. Go to the root of directory using the terminal.
3. To download and process ESC-50 dataset, run: ```python prepare_dataset.py```
4. Prepare the validation data, run: ```python val_generator.py```

*All the required data of ESC-50 for processing `20kHz` are now ready at `datasets/esc50` directory

#### A.3 Training ACDNet
*The experimented models is in `model/trained_fold1.pt` that can be used instead of training a new model.

To retrain existing model or conduct the training of a brand new ACDNet, run: ```python trainer.py```

#### A.4 Testing models
Test any model by running ```python tester.py```
