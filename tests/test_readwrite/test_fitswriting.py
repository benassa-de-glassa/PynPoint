import os
import warnings

import pytest
import numpy as np

from pynpoint.core.pypeline import Pypeline
from pynpoint.readwrite.fitsreading import FitsReadingModule
from pynpoint.readwrite.fitswriting import FitsWritingModule
from pynpoint.util.tests import create_config, create_star_data, remove_test_data

warnings.simplefilter('always')

limit = 1e-10


class TestFitsWritingModule:

    def setup_class(self):

        self.test_dir = os.path.dirname(__file__) + '/'

        create_star_data(path=self.test_dir+'fits')
        create_config(self.test_dir+'PynPoint_config.ini')

        self.pipeline = Pypeline(self.test_dir, self.test_dir, self.test_dir)

    def teardown_class(self):
<<<<<<< HEAD

        remove_test_data(self.test_dir, folders=['fits'], files=['test.fits'])

    def test_fits_reading(self):

        read = FitsReadingModule(name_in='read',
                                 input_dir=self.test_dir+'fits',
                                 image_tag='images',
                                 overwrite=True,
                                 check=True)

        self.pipeline.add_module(read)
=======
        files = ['test.fits', 'test000.fits', 'test001.fits', 'test002.fits', 'test003.fits']
        remove_test_data(self.test_dir, folders=['fits'], files=files)

    def test_fits_reading(self):

        module = FitsReadingModule(name_in='read',
                                   input_dir=self.test_dir+'fits',
                                   image_tag='images',
                                   overwrite=True,
                                   check=True)

        self.pipeline.add_module(module)
>>>>>>> upstream/master
        self.pipeline.run_module('read')

        data = self.pipeline.get_data('images')
        assert np.allclose(data[0, 50, 50], 0.09798413502193704, rtol=limit, atol=0.)
        assert np.allclose(np.mean(data), 0.00010029494781738066, rtol=limit, atol=0.)
        assert data.shape == (40, 100, 100)

    def test_fits_writing(self):

<<<<<<< HEAD
        write = FitsWritingModule(file_name='test.fits',
                                  name_in='write1',
                                  output_dir=None,
                                  data_tag='images',
                                  data_range=None,
                                  overwrite=True)

        self.pipeline.add_module(write)
=======
        module = FitsWritingModule(file_name='test.fits',
                                   name_in='write1',
                                   output_dir=None,
                                   data_tag='images',
                                   data_range=None,
                                   overwrite=True)

        self.pipeline.add_module(module)
>>>>>>> upstream/master
        self.pipeline.run_module('write1')

    def test_filename_extension(self):

        with pytest.raises(ValueError) as error:
            FitsWritingModule(file_name='test.dat',
                              name_in='write3',
                              output_dir=None,
                              data_tag='images',
                              data_range=None,
<<<<<<< HEAD
                              overwrite=True)
=======
                              overwrite=True,
                              subset_size=None)
>>>>>>> upstream/master

        assert str(error.value) == 'Output \'file_name\' requires the FITS extension.'

    def test_data_range(self):

<<<<<<< HEAD
        write = FitsWritingModule(file_name='test.fits',
                                  name_in='write4',
                                  output_dir=None,
                                  data_tag='images',
                                  data_range=(0, 10),
                                  overwrite=True)

        self.pipeline.add_module(write)
=======
        module = FitsWritingModule(file_name='test.fits',
                                   name_in='write4',
                                   output_dir=None,
                                   data_tag='images',
                                   data_range=(0, 10),
                                   overwrite=True,
                                   subset_size=None)

        self.pipeline.add_module(module)
>>>>>>> upstream/master
        self.pipeline.run_module('write4')

    def test_not_overwritten(self):

<<<<<<< HEAD
        write = FitsWritingModule(file_name='test.fits',
                                  name_in='write5',
                                  output_dir=None,
                                  data_tag='images',
                                  data_range=None,
                                  overwrite=False)

        self.pipeline.add_module(write)
=======
        module = FitsWritingModule(file_name='test.fits',
                                   name_in='write5',
                                   output_dir=None,
                                   data_tag='images',
                                   data_range=None,
                                   overwrite=False,
                                   subset_size=None)

        self.pipeline.add_module(module)
>>>>>>> upstream/master

        with pytest.warns(UserWarning) as warning:
            self.pipeline.run_module('write5')

        assert len(warning) == 1
        assert warning[0].message.args[0] == 'Filename already present. Use overwrite=True ' \
                                             'to overwrite an existing FITS file.'

<<<<<<< HEAD
=======
    def test_subset_size(self):

        module = FitsWritingModule(file_name='test.fits',
                                   name_in='write6',
                                   output_dir=None,
                                   data_tag='images',
                                   data_range=None,
                                   overwrite=True,
                                   subset_size=10)

        self.pipeline.add_module(module)
        self.pipeline.run_module('write6')

    def test_subset_size_data_range(self):

        module = FitsWritingModule(file_name='test.fits',
                                   name_in='write7',
                                   output_dir=None,
                                   data_tag='images',
                                   data_range=(8, 18),
                                   overwrite=True,
                                   subset_size=10)

        self.pipeline.add_module(module)
        self.pipeline.run_module('write7')

>>>>>>> upstream/master
    def test_attribute_length(self):

        text = 'long_text_long_text_long_text_long_text_long_text_long_text_long_text_long_text'

        self.pipeline.set_attribute('images', 'short', 'value', static=True)
        self.pipeline.set_attribute('images', 'longer_than_eight1', 'value', static=True)
        self.pipeline.set_attribute('images', 'longer_than_eight2', text, static=True)

<<<<<<< HEAD
        write = FitsWritingModule(file_name='test.fits',
                                  name_in='write6',
                                  output_dir=None,
                                  data_tag='images',
                                  data_range=None,
                                  overwrite=True)

        self.pipeline.add_module(write)

        with pytest.warns(UserWarning) as warning:
            self.pipeline.run_module('write6')
=======
        module = FitsWritingModule(file_name='test.fits',
                                   name_in='write8',
                                   output_dir=None,
                                   data_tag='images',
                                   data_range=None,
                                   overwrite=True,
                                   subset_size=None)

        self.pipeline.add_module(module)

        with pytest.warns(UserWarning) as warning:
            self.pipeline.run_module('write8')
>>>>>>> upstream/master

        assert len(warning) == 1
        assert warning[0].message.args[0] == 'Key \'hierarch longer_than_eight2\' with value ' \
                                             '\'long_text_long_text_long_text_long_text_long_' \
                                             'text_long_text_long_text_long_text\' is too ' \
                                             'long for the FITS format. To avoid an error, ' \
                                             'the value was truncated to \'long_text_long_text' \
                                             '_long_text_long_text_long_tex\'.'
