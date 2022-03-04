# Labrecipipe

Remote controller for labrecorder.

starts, sets the filename, load configuration files and record via python. Interfacing through UDP.

# Requirements

The software is meant to control labrecorder. Since it interfaces through UDP there is no need to install any external libraries.

## Installation (automatic)

`pip install labrecipipe`

## Installation for psychopy

- Download the .zip release from github (right of the page)
- Go to `psychopy/Lib/site-packages/`
- extract the folder labrecipipe in there
- test the installation from your psychopy code `import labrecipipe`

## Installation (manual)

`conda create --name labrecipipe python=3.6.6`



## Usage

### Get a LSL stream running first

GitHub: `https://github.com/brain-products/LSL-BrainAmpSeries`

Click on the "Release" button on the right and select the installer

By default the BrainAmpSeries lsl-linker installs itself in `C:\Vision\LSL-Apps\BrainAmpSeries\bin\BrainAmpSeries.exe` 

Tinkering with the configuration file will help define the channels

### Record it via labrecorder

Github: `https://github.com/labstreaminglayer/App-LabRecorder` 

Please note that labrecorder is a bit greedy and will select all streams available on the network. However, unless new streams are defined in the configuration files, they won't be added when discovered. The `force_restart=True` parameter ensures that all stream discovered are recorded

```
from labrecipipe import LabRecorderHandler
importr time

path_to_labrecorder = r'C:/LabRecorder/LabRecorder.exe'

# (Option 1)Call labrecorder with default BrainAmpSeries parameters
lrh = LabRecorderHandler(path_to_labrecorder_exe=path_to_labrecorder,
list_required_streams=LabRecorderHandler.BRAINAMP_STREAMS)
'''
# (Option 2) Use a custom configuration file
lrh = LabRecorderHandler(path_to_labrecorder_exe=r'./LabRecorder/LabRecorder.exe',
labrecorder_cfg=r'./LabRecorder/LabRecorder.cfg')

# (Option 3) Define the stream names and hosts by hand, using none default to the computer's hostname
lrh = LabRecorderHandler(path_to_labrecorder_exe=DEFAULT_PATH_EXE,
list_required_streams=[('LiveAmpSN-100709-0788', None),
('LiveAmpSN-100709-0788-DeviceTrigger', 'localhost')])
'''
lrh.start_lab_recorder()

# Start recording for 10 seconds
lrh.start_recording(output_eeg_path=r'./test.eeg',  # change the output filename
force_restart=True)  # force to restart labrecorder to update streams
time.sleep(10)

lrh.update_lsl()

time.sleep(10)

# stop recording
lrh.stop_recording()
# close labrecorder (kills the process)
lrh.close()
```

Make sure when defining a target file ()

### (optional) Define mandatory streams

By modifying the configuration file `lab_rec_brainamp_placeholders.cfg` you ensure that the software warns you if a stream is missing. 

You can add any stream. The default syntax is `"RequiredExample (PC-HOSTNAME)"` , but if you leave `_PLACEHOLDER_HOSTNAME_` the software automatically uses your hostname as reference.

  

# Self notes

# deploy pypi

```
# install the executables
python setup.py build bdist bdist_wheel

# upload to PyPI
cd dist
twine upload *


# test the program
from labrecipipe import LabRecorderHandler
```

