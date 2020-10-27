# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""
    Kubernetes
    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501
    The version of the OpenAPI document: release-1.16
    Generated by: https://openapi-generator.tech
"""
import sys,os
import multiprocessing
from docx2pdf import convert
from PIL import Image

class DeleteHandler:
""" This class provides utility functions"""

   def __init__(self, path):
        """Deletes placeholder for input"""
        self.path = path
        files_to_pdf(self)

   def delete_files(self): 
        """Deletes placeholder for input"""
        for filename in os.listdir(self.path):
            if filename != PDF_OUTPUT_NAME:
                os.remove(path + "\\" + filename)
