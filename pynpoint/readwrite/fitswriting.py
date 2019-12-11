"""
<<<<<<< HEAD
Module for writing data as FITS file.
"""

import os
import sys
=======
Module for exporting a dataset from the HDF5 database to a FITS file.
"""

import os
>>>>>>> upstream/master
import warnings

from typing import Tuple

from astropy.io import fits
from typeguard import typechecked

<<<<<<< HEAD
from pynpoint.core.processing import WritingModule
=======
import numpy as np

from pynpoint.core.processing import WritingModule
from pynpoint.util.module import memory_frames
>>>>>>> upstream/master


class FitsWritingModule(WritingModule):
    """
<<<<<<< HEAD
    Module for writing a data set of the central HDF5 database as FITS file. The data and all
    attached attributes will be saved. Besides typical image stacks it is possible to export for
    example non-static header information. To choose the data set from the database its tag
    / key has to be specified. FitsWritingModule is a Writing Module and supports to use the
    Pypeline default output directory as well as a own location. See
    :class:`pynpoint.core.processing.WritingModule` for more information. Note that per default
    this module will overwrite an existing FITS file with the same filename.
    """

=======
    Module for writing a dataset from the central HDF5 database to a FITS file. The static
    attributes will be stored as header information. The dataset is selected from the database
    by its tag name. :class:`~pynpoint.readwrite.fitswriting.FitsWritingModule` is a
    :class:`~pynpoint.core.processing.WritingModule` and uses either the default output directory
    of a :class:`~pynpoint.core.pypeline.Pypeline` or a specified location to store the FITS data.
    """

    __author__ = 'Markus Bonse, Tomas Stolker'

>>>>>>> upstream/master
    @typechecked
    def __init__(self,
                 name_in: str,
                 data_tag: str,
                 file_name: str,
                 output_dir: str = None,
                 data_range: Tuple[int, int] = None,
<<<<<<< HEAD
                 overwrite: bool = True) -> None:
=======
                 overwrite: bool = True,
                 subset_size: int = None) -> None:
>>>>>>> upstream/master
        """
        Parameters
        ----------
        name_in : str
            Unique name of the module instance.
        data_tag : str
<<<<<<< HEAD
            Tag of the database entry the module has to export as FITS file.
=======
            Tag of the database entry that has to be exported to a FITS file.
>>>>>>> upstream/master
        file_name : str
            Name of the FITS output file. Requires the FITS extension.
        output_dir : str, None
            Output directory where the FITS file will be stored. If no folder is specified the
            Pypeline default is chosen.
        data_range : tuple, None
            A two element tuple which specifies a begin and end frame of the export. This can be
<<<<<<< HEAD
            used to save a subsets of huge dataset. If None the whole dataset will be exported.
        overwrite : bool
            Overwrite existing FITS file with identical filename.
=======
            used to save a subsets of a large dataset. The whole dataset will be exported if set
            to None.
        overwrite : bool, None
            Overwrite an existing FITS file with an identical filename.
        subset_size : int, None
            Size of the subsets that are created when storing the data. This can be useful if the
            dataset contains a large number of images. An increasing index value is appended to
            the FITS file names. All images are written to a single FITS file if set to None.
>>>>>>> upstream/master

        Returns
        -------
        NoneType
            None
        """

        super(FitsWritingModule, self).__init__(name_in=name_in, output_dir=output_dir)

        if not file_name.endswith('.fits'):
            raise ValueError('Output \'file_name\' requires the FITS extension.')

        self.m_file_name = file_name
        self.m_data_port = self.add_input_port(data_tag)
        self.m_range = data_range
        self.m_overwrite = overwrite
<<<<<<< HEAD
=======
        self.m_subset_size = subset_size
>>>>>>> upstream/master

    @typechecked
    def run(self) -> None:
        """
<<<<<<< HEAD
        Run method of the module. Creates a FITS file and saves the data as well as the
        corresponding attributes.
=======
        Run method of the module. Creates a FITS file and stores the data and the corresponding
        static attributes.
>>>>>>> upstream/master

        Returns
        -------
        NoneType
            None
        """

        out_name = os.path.join(self.m_output_location, self.m_file_name)

<<<<<<< HEAD
        sys.stdout.write('Running FitsWritingModule...')
        sys.stdout.flush()
=======
        print('Writing FITS file...', end='')
>>>>>>> upstream/master

        if os.path.isfile(out_name) and not self.m_overwrite:
            warnings.warn('Filename already present. Use overwrite=True to overwrite an existing '
                          'FITS file.')

        else:
<<<<<<< HEAD
            prihdr = fits.Header()
=======
            header = fits.Header()
>>>>>>> upstream/master
            attributes = self.m_data_port.get_all_static_attributes()

            for attr in attributes:

                if len(attr) > 8:

                    # Check if the header keyword together with its value is
                    # too long for the FITS format. If that is the case, raise
                    # a warning and truncate the value to avoid a ValueError.
                    key = 'hierarch ' + attr
                    value = str(attributes[attr])
                    max_val_len = 75 - len(key)

                    if len(key + value) > 75:
                        warnings.warn(f'Key \'{key}\' with value \'{value}\' is too long for '
                                      f'the FITS format. To avoid an error, the value was '
                                      f'truncated to \'{value[:max_val_len]}\'.')

<<<<<<< HEAD
                    prihdr[key] = value[:max_val_len]

                else:
                    prihdr[attr] = attributes[attr]

            if self.m_range is None:
                hdu = fits.PrimaryHDU(self.m_data_port.get_all(),
                                      header=prihdr)
            else:
                hdu = fits.PrimaryHDU(self.m_data_port[self.m_range[0]:self.m_range[1], ],
                                      header=prihdr)

            hdulist = fits.HDUList([hdu])
            hdulist.writeto(out_name, overwrite=self.m_overwrite)

            sys.stdout.write(' [DONE]\n')
            sys.stdout.flush()
=======
                    header[key] = value[:max_val_len]

                else:
                    header[attr] = attributes[attr]

            if self.m_subset_size is None:
                if self.m_range is None:
                    frames = [0, self.m_data_port.get_shape()[0]]

                else:
                    frames = [self.m_range[0], self.m_range[1]]

            else:
                if self.m_range is None:
                    nimages = self.m_data_port.get_shape()[0]
                    frames = memory_frames(self.m_subset_size, nimages)

                else:
                    nimages = self.m_range[1] - self.m_range[0]
                    frames = memory_frames(self.m_subset_size, nimages)
                    frames = np.asarray(frames) + self.m_range[0]

            for i, item in enumerate(frames[:-1]):
                data_select = self.m_data_port[frames[i]:frames[i+1], ]

                if len(frames) == 2:
                    fits.writeto(out_name, data_select, header, overwrite=self.m_overwrite)

                else:
                    filename = f'{out_name[:-5]}{i:03d}.fits'
                    fits.writeto(filename, data_select, header, overwrite=self.m_overwrite)

            print(' [DONE]')
>>>>>>> upstream/master

        self.m_data_port.close_port()
