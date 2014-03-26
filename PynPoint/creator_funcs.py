        
#import external functions:
import pyfits
import pylab as pl
import glob
import time
import h5py
import numpy as np
import os

#import extra PynPoint functions:
import Util
from Mask import mask
#import PynPoint_v1_5 as PynPoint


#Images class:
# class pynpoint_parent:
#     """Object for dealing with the images that need to be analysed"""
    # 
    # def __init__(self):
    #     """
    #     Initialise an instance of the images class. The result is simple and
    #     almost empty (in terms of attributes)
    #     
    #     """
    #     self.obj_type = 'PynPoint_parent'
    #     

# def temp_func():
#     print('!!!!!!!HI!!!!!!!')
#     

# @staticmethod
def pynpoint_create_restore(obj,filename):
    """
    Creates an instance of the images class using a previously
    saved file. The file should have been stored as an HDF5 file
    
    :param filename: name of the inputfile 
    
    """
    #obj = pynpoint_parent()
    Util.restore_data(obj,filename)
    #return obj

# @staticmethod
def pynpoint_create_wdir(obj,dir_in,ran_sub=False,force_reload=False,prep_data=True,**kwargs):
    """
    Creates an instance of the images class using dir_in, which is the
    name of a directory containing the input fits files. 
    As well as its input parameters, this function can pass the keyword
    options used by prep_data method. 
    
    :param dir_in: name of the directory with fits files
    :param ran_sub: if a number (N) is passed then a random subset of filessize is selected 
    
    """
    
    ##convert to hdf5
    assert (os.path.isdir(dir_in)), 'Error: Input directory does not exist - input requested: %s'%dir_in
    file_hdf5 = Util.filename4mdir(dir_in)
    assert os.path.isfile(file_hdf5), 'Error: No fits files found in the directory: %s, %s' %dir_in %file_hdf5
    if (force_reload is True) or (not os.path.isfile(file_hdf5)):
        Util.conv_dirfits2hdf5(dir_in,outputfile = file_hdf5)
    # obj = pynpoint_parent.create_whdf5input(file_hdf5,ran_sub=False,**kwargs)
    pynpoint_create_whdf5input(obj,file_hdf5,ran_sub=False,**kwargs)
    #return obj

# @staticmethod
def pynpoint_create_whdf5input(obj,file_in,ran_sub=False,prep_data=True,**kwargs):
    """
    Creates an instance of the images class using dir_in, which is the
    name of a directory containing the input fits files. 
    As well as its input parameters, this function can pass the keyword
    options used by prep_data method. 
    
    :param dir_in: name of the directory with fits files
    :param ran_sub: if a number (N) is passed then a random subset of filessize is selected 
    
    """
    #pynpoint_parent.__init__(obj)
    #obj = pynpoint_parent()
    assert (os.path.isfile(file_in)), 'Error: Input file does not exist - input requested: %s'%file_in    
    obj_type = obj.obj_type
    Util.restore_data(obj,file_in,checktype='raw_data')
    obj.obj_type = obj_type #'PynPoint_images' # restate since this is replaced in the restore_data
    #use the ran_subset keyword
    if prep_data is True:
        Util.prep_data(obj,**kwargs)                    

    #return obj

# @staticmethod
def pynpoint_create_wfitsfiles(obj,files,ran_sub=False,prep_data=True,**kwargs):
    """
    Creates an instance of the images class using a list of fits file names. 
    As well as its input parameters, this function can pass the keyword
    options used by prep_data method. 
    
    :param files: list with with fits file names
    :param ran_sub: if a number (N) is passed then a random subset of filessize is selected 
    
    """
    #obj = pynpoint_parent()
    num_files = np.size(files)            # number of files
    assert (num_files >0),'Error: No files inputs, e.g.: %s' %files[0]
    assert os.path.isfile(files[0]),'Error: No files inputs, e.g.: %s' %files[0]
    obj.files = files
    obj.num_files = num_files
    Util.rd_fits(obj)#,avesub=False,para_sort=para_sort,inner_pix=inner_pix)
    if prep_data is True:
        Util.prep_data(obj,**kwargs)
        
 