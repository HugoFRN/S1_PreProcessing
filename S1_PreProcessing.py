import os
import glob
import tqdm
import subprocess
import argparse
import sys


# gpt_path = '/media/hfr/Donnees/Data/S1Processing/snap/bin/gpt'
def main(gpt_path, graph_path, path, OUT, verbose):
    '''
    Batch processing for Sentinel-1 images.
    Apply the operations described in the graph (produced by SNAP) to all the directories of the input
    :param gpt_path : Path to the gpt program
    :param graph_path: Path to the graph (.xml format)
    :param path: Path to the directory containing all the inputs (format .SAFE)
    :param OUT: Path to where the output is saved (with the same name as the input but in .data format)
    :return:
    '''

    # Find the input in the .SAFE format
    input_files = glob.glob(os.path.join(path, '*.SAFE'))

    # Find the input that has not been processed (allow to stop and restart the script without re-doing the previous
    # processing.
    sorted_files = []
    for f in input_files:
        output_file = os.path.join(OUT, os.path.basename(f)).replace('.SAFE', '.dim')
        if not os.path.exists(output_file):
            sorted_files.append(f)

    # Process each image
    for f in tqdm.tqdm(sorted_files, total=len(sorted_files)):
        output_file = os.path.join(OUT, os.path.basename(f)).replace('.SAFE', '.dim')
        if not os.path.exists(output_file):
            try:
                if not verbose:
                    with open(os.devnull, 'wb') as devnull:
                        # Use the gpt program from SNAP to execute the operations described in the graph
                        subprocess.call(gpt_path + ' %s -t %s -c 20G -q 12 %s' % (graph_path,
                            output_file.replace('.dim', ''), f), stdout=devnull, stderr=subprocess.STDOUT, shell=True)
                else:
                    os.system(gpt_path + ' %s -t %s -c 20G -q 12 %s' % (graph_path,
                                                                              output_file.replace('.dim', ''), f))
            except OSError:
                pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Batch processing for Sentinel-1 images')
    parser.add_argument('input_folder', action='store', help='Input directory')
    parser.add_argument('output_folder', action='store', help='Output directory')
    parser.add_argument('-g', metavar='graph_path', action='store', default='./myGraph_gpt.xml', help='Graph path')
    parser.add_argument('-snap', metavar='snap_path', action='store', default='./gpt', help='Snap install path')
    parser.add_argument('-v', action='store_true', help='Print logs')
    args = parser.parse_args()
    input_dir = args.input_folder
    output_dir = args.o
    graph_path = args.g
    gpt_path = args.snap
    gpt_path = os.path.join(gpt_path, 'bin', 'gpt')
    verbose = args.v

    # Check the arguments
    if not os.path.exists(input_dir):
        print('Error : Input folder don\'t exists')
    if not os.path.exists(output_dir):
        print('Error : Output folder don\'t exists')
    if not os.path.exists(gpt_path):
        print('Error : Cannot find gpt.')
        sys.exit(0)
    if not os.path.exists(graph_path):
        print('Error : Cannot find graph.')
        sys.exit()

    main(gpt_path, graph_path, input_dir, output_dir, verbose)
