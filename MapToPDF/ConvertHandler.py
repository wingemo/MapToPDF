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
from PyPDF2 import PdfFileMerger
from PIL import Image
from tkinter import messagebox
from FileConverter import *
from FileMerger import *
from FileDestroyer import *

class MergeHandler():
   """ This class provides utility functions"""

   def __init__(self, self_object, path, progress):
        """Deletes placeholder for input"""
        self.self = self_object
        self.progress = progress
        self.path = path

        if(messagebox.askquestion("Merge files", path + ", Are You Sure?", icon='warning')):
            # and split into a list of lines:
            self.progress['maximum'] = 100
            self.update_progressbar(10)
            self.files_to_pdf(self.path)
            self.update_progressbar(30)
            self.merge_files(self.path)
            self.update_progressbar(50)
            self.delete_files(self.path)
            self.update_progressbar(100)
            self.update_progressbar(0)
        else:
            messagebox.showerror("Info", "You interrupted!")

   def update_progressbar(self, procent):
        self.progress['value'] = procent
        self.progress.update()

   def files_to_pdf(self, path):
        """Deletes placeholder for input"""
        try:
            FileConverter(path)
        except Exception as e:
            messagebox.showerror("Info", "Error" + str(e))

   def merge_files(self, path):
        """Deletes placeholder for input"""
        try:
            FileMerger(path)
        except Exception as e:
            messagebox.showerror("Info", "Error" + str(e))

   def delete_files(self, path):
        """Deletes placeholder for input"""
        try:
            FileDestroyer(path)
        except Exception as e:
            messagebox.showerror("Info", "Error" + str(e))

        messagebox.showinfo("INFO", "All files have been compiled")
  
