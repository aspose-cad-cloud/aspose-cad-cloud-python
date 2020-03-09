# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="PutDrawingGifRequest.py">
#   Copyright (c) 2018 Aspose.CAD Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# --------------------------------------------------------------------------------


class PutDrawingGifRequest(object):
    """
    Request model for put_drawing_gif operation.
    Initializes a new instance.
    :param drawing_data Input drawing
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/GifOptionsDTO model definition.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, export_options=None, out_path=None, storage=None):
        self.drawing_data = drawing_data
        self.export_options = export_options
        self.out_path = out_path
        self.storage = storage
