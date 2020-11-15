from astroquery.gaia import Gaia
import sys
import pandas as pd
import numpy as np


def gaiadata(a, b, c = 0.083):
    
    ra=str(a)
    dec=str(b)
    rad=str(c)  #in degrees
    query = "SELECT ra, dec, ra_error, dec_error, parallax, parallax_error, pmra, pmra_error, pmdec, pmdec_error, phot_g_mean_mag, bp_rp, r_est, r_lo, r_hi FROM external.gaiadr2_geometric_distance JOIN gaiadr2.gaia_source USING (source_id) WHERE CONTAINS(POINT('ICRS',ra,dec), CIRCLE('ICRS',"+ra+","+dec+","+rad+"))=1"
    job = Gaia.launch_job_async(query, output_file='data.csv',output_format='csv',dump_to_file=True)
    
    Data=pd.read_csv('data.csv')
    Data.rename(columns={'ra': 'RA_ICRS', 'dec': 'DE_ICRS', 'parallax': 'Plx', 'pmra': 'pmRA', 'pmdec': 'pmDE', 'phot_g_mean_mag': 'Gmag','bp_rp': 'BP_RP'},inplace=True)
    Data.to_csv('data.csv',index=False)
    