## Installation

The software requires a JAVA installation (J2SE 1.8 JDK) in order to use SNAP.
SNAP and the Sentinel-1 toolbox (S1TBX) can be found here: http://step.esa.int/main/download/ 
When installing SNAP, select the S1TBX to be installed with SNAP and save the path installation path for later use.

The tqdm python library is also required to lunch the script. It can easily be installed using pip:
$ pip install tqdm

## Execution

usage: S1_PreProcessing.py [-h] [-g graph_path] [-snap snap_path] [-v]
                           input_folder output_folder

Batch processing for Sentinel-1 images

positional arguments:
  input_folder     Input directory
  output_folder    Output directory

optional arguments:
  -h, --help       show this help message and exit
  -g graph_path    Graph path
  -snap snap_path  Snap install path
  -v               Print logs

## Example

$ python3 S1_PreProcessing.py -snap /usr/local/snap/ -g ./myGraph_gpt.xml input/ output/
Will process every input in the input/ folder and output the results in the output/ folder. 
The –snap argument give the path to the SNAP installation and the –g argument give the path to the graph defining the necessary operations (see 3.1)
