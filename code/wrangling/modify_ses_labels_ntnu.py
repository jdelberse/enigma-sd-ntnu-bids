import os
import glob
import pandas as pd

# Load, add sub-labels, set sub as index
tsv = pd.read_csv("participants.tsv", sep="\t")
tsv.set_index('participant_id', inplace=True)

demo = pd.read_excel(
    "sourcedata/NTNU_ENIGMA_sleep.xlsx", sheet_name="participant_list")

for sub in tsv.index:
    subnum = int(sub.replace("sub-",""))
    rand = int(demo.loc[demo.ID == subnum, "randomization"].item())

    if rand == 1:
        ses_labs = {"ses-T2" : "ses-b9", "ses-T3" : "ses-sd9"}
    else:
        ses_labs = {"ses-T3" : "ses-b9", "ses-T4" : "ses-sd9"}
    
    for ses in ses_labs.keys():
        for f in glob.glob(f"{sub}/{ses_labs[ses]}/*/{sub}_{ses}*"):
            old_scan = f
            new_scan = f.replace(f"{sub}_{ses}",f"{sub}_{ses_labs[ses]}")
        
            if os.path.exists(old_scan) and not os.path.exists(new_scan):
                print(f"{old_scan} >>> {new_scan}")
                os.rename(old_scan, new_scan)
            else:
                print(f"{new_scan} exists. Skipping...")
        
        old_dir = f"{sub}/{ses}"
        new_dir = f"{sub}/{ses_labs[ses]}"

        if os.path.exists(old_dir) and not os.path.exists(new_dir):
            print(f"{old_dir} >>> {new_dir}")
            os.rename(old_dir, new_dir)
        else:
            print(f"{new_dir} exists. Skipping...")

