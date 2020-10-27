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
from docx2pdf import convert
from PyPDF2 import PdfFileMerger
from PIL import Image
from tkinter import messagebox

class ConvertHandler:
""" This class provides utility functions"""

   MESSAGEBOX_TITLE = "INFO"
   SUCCESS_MESSAGE = "All files have been compiled into a pdf - Philip"
   PDF_OUTPUT_NAME = "output.pdf"

   def __init__(self):
        """Deletes placeholder for input"""
        print_contents(self)
        path = self.contents.get()

        # and split into a list of lines:
        update_progressbar(10)
        files_to_pdf(self)
        update_progressbar(30)
        merge_files(self)
        update_progressbar(50)
        delete_files(self)
        update_progressbar(0)

   def update_progressbar(value):
       """Deletes placeholder for input"""
       self.progress['value'] = value
       self.progress.update()

   def files_to_pdf(self): 
       """Deletes placeholder for input"""
        try:
            for filename in os.listdir(path):
                if filename.endswith(".docx") or filename.endswith(".doc"):
                    convert(path + "\\" + filename)
                    continue
                elif filename.endswith(".jpg") or filename.endswith(".PNG")  or filename.endswith(".png"):
                    image1 = Image.open(path + "\\" + filename)
                    im1 = image1.convert('RGB')
                    im1.save(path + "\\" + filename + ".pdf")
                    continue
                else:
                    continue
        except Exception as e:
            messagebox.showerror("Info", "Error" + str(e))
 
    def merge_files(self):
        """Deletes placeholder for input"""
        open_pdf = []
        x = [a for a in os.listdir(path) if a.endswith(".pdf")]
        merger = PdfFileMerger()

        for pdf in x:
            f = open(path + "\\"+ pdf, 'rb')
            open_pdf.append(f)
            merger.append(f)

        with open(path + "\\"+ PDF_OUTPUT_NAME, "wb") as fout:
            merger.write(fout)

        for pdf in open_pdf:
            pdf.close()
            merger.close()

    def delete_files(self):
        """Deletes placeholder for input"""
        for filename in os.listdir(path):
            if filename != PDF_OUTPUT_NAME:
                os.remove(path + "\\" + filename)

        update_progressbar(100)
        messagebox.showinfo(MESSAGEBOX_TITLE, SUCCESS_MESSAGE)
  
