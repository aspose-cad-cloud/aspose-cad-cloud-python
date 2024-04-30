#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="runner.py">
#    Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
#  </copyright>
#  <summary>
#    Permission is hereby granted, free of charge, to any person obtaining a
#   copy  of this software and associated documentation files (the "Software"),
#   to deal  in the Software without restriction, including without limitation
#   the rights  to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell  copies of the Software, and to permit persons to whom the
#   Software is  furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all  copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM,  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#  </summary>
#  ----------------------------------------------------------------------------

import argparse
import os
import sys
from distutils.util import strtobool

import six
import xmlrunner

import test

if six.PY2:
    import unittest2 as unittest
else:
    import unittest

# runner works with one optional argument - directory to save test results
parser = argparse.ArgumentParser(
    description='Test Aspose CAD Cloud SDK Python')
parser.add_argument(
    '-o', '--output_directory', default=None, required=False,
    help='Directory to save test results. '
         'Test result are not saved by default.')
args = parser.parse_args()

# set EXTENDED_TEST from env
if os.environ.get('ExtendedTests'):
    test.api_tester.ApiTester.EXTENDED_TEST = bool(
        strtobool((os.environ.get('ExtendedTests'))))

# get test categories from env
test_categories = None
if os.environ.get('TestCategories'):
    test_categories = os.environ.get('TestCategories')

# Test categories can't be managed by framework so they should be collected
# here manually
loader = unittest.TestLoader()
suites_dict = {}

# TODO: move test discovery to lambda to discovery only required categories?

save_as_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_save_as_api']))
suites_dict['SaveAs'] = save_as_suite

resize_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_resize_api']))
suites_dict['Resize'] = resize_suite

rotate_flip_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_rotate_flip_api']))
suites_dict['RotateFlip'] = rotate_flip_suite

cad_suit = unittest.TestSuite(
    [resize_suite, rotate_flip_suite, save_as_suite])
suites_dict['CAD'] = cad_suit

v3_suite = unittest.TestSuite(
    [resize_suite, rotate_flip_suite, save_as_suite])
suites_dict['v3.0'] = v3_suite

suite = unittest.TestSuite()
if test_categories:
    for category in test_categories.split():
        suite.addTests(suites_dict[category])
else:
    suite.addTests(loader.loadTestsFromModule(sys.modules['test']))

if args.output_directory:
    runner = xmlrunner.XMLTestRunner(output=args.output_directory, verbosity=2)
else:
    runner = unittest.TextTestRunner(verbosity=2)

result = not runner.run(suite).wasSuccessful()
sys.exit(result)
