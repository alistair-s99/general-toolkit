import pandas as pd 
import glob 

"""
The purpose of this script is to 
collate a series of csv files that share the 
same headers into a single output
"""

def Collate_Files(search_folder, output_file):
    
    # Using * will ignore file names and retrieve all csv's 
    # in the search folder
    target_files = glob.glob(search_folder + '/*.csv')

    # Next we loop through the target files and write them to the 
    # output frame using an intermediate DataFrame
    # Note - an exception will raise if any file has a different schema from the others
    for file in target_files:
        try:
            df = pd.read_csv(file)
            out_frame = pd.concat([out_frame, df], ignore_index = True)
        except Exception as e:
            print(f'Error handling file: {file} - {e}')

    # Finally try writing the output frame to a csv
    try:
        out_frame.to_csv(output_file, index = False)
    except Exception as e:
        print(f'Error writing output to: {output_file} - {e}')
