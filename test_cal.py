import os
import pytest
import shutil
import calc

class TestCal(object):

    @classmethod
    def setup_class(cls):
        cls.cal = calc.Cal()
        cls.test_dir = '/tmp/test_dir'
        cls.test_file_name = 'test1.txt'

    def teardown_class(cls):
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(self.test_dir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    def test_add_num_and_double(self, csv_file):
        print(csv_file)
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')


