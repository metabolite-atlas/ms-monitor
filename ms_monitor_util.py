import sys
import numpy as np

import os

from IPython.display import display

try:

    qgrid.set_grid_option('defaultColumnWidth', 200)

from datetime import datetime
import pandas as pd
import json

from matplotlib import pyplot as plt
import re


def get_rt_mz_tolerance_from_user():
    mz_tolerance = float(raw_input('Enter mz tolerance in ppm (ex "20"): ').replace('ppm',''))
    return mz_tolerance, rt_tolerance

def get_blank_qc_pos_neg_string():
    qc_widget = widgets.Text(description="QC ID: ",value='QC')
    return qc_widget, blank_widget, pos_widget, neg_widget

def get_files_for_experiment(experiment_name):
    files = metob.retrieve('LcmsRun',username='*',experiment=experiment_name)
    flist = []
    df = pd.DataFrame()
    for counter,f in enumerate(flist):
        df.loc[counter,'file'] = os.path.basename(f)
#    del df['index']   
    df.set_index('file', drop=True, append=False, inplace=True)
    #df.reset_index(drop=True,inplace=True)
    
    options = qgrid.grid.defaults.grid_options
    options['defaultColumnWidth'] = 600
    #mygrid = qgrid.show_grid(df, remote_js=True,grid_options = options)
    grid = qgrid.grid.QGridWidget(df=df,
    gui = widgets.Box([grid])
    display(gui)  
    return files

def get_recent_experiments(num_days):
    if not num_days:
        num_days = 5
    query = 'SELECT DISTINCT experiment,creation_time FROM lcmsruns where creation_time >= UNIX_TIMESTAMP(DATE_SUB(CURDATE(), INTERVAL %d DAY))'%num_days
    experiments = []
    experiments = np.unique(experiments)
    )
    display(experiment_widget)
    #files = get_files_for_experiment(experiment_widget.value)
    #def experiment_change(trait,value):
    #    files = get_files_for_experiment(value)
    #    return files
    #experiment_widget.on_trait_change(experiment_change,'value')

    return experiment_widget

def get_files_from_recent_experiment(num_days):
    if not num_days:
        num_days = 5
    query = 'SELECT DISTINCT experiment,creation_time,username FROM lcmsruns where creation_time >= UNIX_TIMESTAMP(DATE_SUB(CURDATE(), INTERVAL %d DAY))'%num_days
    #TODO: filter by unique experiment name
    #df.drop_duplicates(cols = 'experiment', inplace = True)
    df.groupby('experiment', group_keys=False)
    options = qgrid.grid.defaults.grid_options
    #mygrid = qgrid.show_grid(df, remote_js=True,)
    #print "Enter the experiment name here"
    #files = qgrid.get_selected_rows(mygrid)    
    #return files

def get_method_dropdown():

def get_ms_monitor_reference_data():
    json_key = json.load(open('/project/projectdirs/metatlas/projects/google_sheets_auth/ipython to sheets demo-9140f8697062.json'))
    return istd_qc_data, blank_data

def filter_istd_qc_by_method(method):
    istd_qc_data, blank_data = get_ms_monitor_reference_data()
    mz_ppm_tolerance = float(method.split('_')[3].replace('ppm',''))
    peak_height_minimum = float(method.split('_')[4].replace('counts',''))

    permanent_charge_index = []
                #df.loc[counter,'permanent_charge'] = compound[permanent_charge_index]

    istd_hilic = setup_atlas_values(istd_hilic,rt_minutes_tolerance,mz_ppm_tolerance)
    reference_data = {}
    reference_data['qc'] = qc_hilic
    reference_data['common'] = common_hilic
    reference_data['istd'] = istd_hilic
    reference_data['blank'] = istd_hilic
    reference_data['parameters'] = {}
    reference_data['parameters']['rt_minutes_tolerance'] = rt_minutes_tolerance
    reference_data['parameters']['mz_ppm_tolerance'] = mz_ppm_tolerance
    reference_data['parameters']['peak_height_minimum'] = peak_height_minimum


def setup_atlas_values(df,rt_minutes_tolerance,mz_ppm_tolerance):
        if temp_dict[compound_name]:
            df.loc[compound_name,'pos_mz'] = pos_mz



def construct_result_table_for_files(files,qc_str,blank_str,neg_str,pos_str,method,reference_data,experiment):
    df = pd.DataFrame()
                                df.loc[counter, 'method'] = method.value
    df.to_excel('%s_%s.xls'%( clean_string(experiment.value), clean_string(method.value) ) )
    df.to_excel('%s/%s_%s.xls'%( '/project/projectdirs/metatlas/projects/ms_monitor_tools/ms_monitor_logs', clean_string(experiment.value), clean_string(method.value) ) )

    f = make_compound_plots(df,'QC',pos_str.value,experiment,method)

    return df


def make_compound_plots(df,plot_type,polarity,experiment,method):
    if plot_type == 'QC':
    else:
        compound_names = df[df['name has QC'] == 0]['Compound name'].unique()
    if nRows > 0:
                sdf = df[(df['Compound name'] == cname) & df['filename'].str.contains(polarity) & (df['name has blank'] == 0)  & (df['name has QC'] == 1)]
            else:
                sdf = df[(df['Compound name'] == cname) & df['filename'].str.contains(polarity) & (df['name has blank'] == 0)  & (df['name has QC'] == 0)]
        f.savefig('/project/projectdirs/metatlas/projects/ms_monitor_tools/ms_monitor_logs/plot_summary_%s_%s_%s_%s.png'%( plot_type, polarity, clean_string(experiment.value), clean_string(method.value) ) )
        return f

# it takes too long to write to a sheet this way.  need to redo it with getting all cells, updating their values and then sending the data over as a large transfer
#import json