# Software License Agreement (BSD License)
#
# Copyright (c) 2012, Fraunhofer FKIE/US, Alexander Tiderko
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of I Heart Engineering nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from PySide import QtGui

class WarningMessageBox(QtGui.QMessageBox):
  def __init__(self, icon, title, text, detailed_text="", buttons=QtGui.QMessageBox.Ok):
    QtGui.QMessageBox.__init__(self, icon, title, text, buttons)
    if detailed_text:
      self.setDetailedText(detailed_text)
#            self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
#            self.setSizeGripEnabled(True)
      horizontalSpacer = QtGui.QSpacerItem(480, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
      layout = self.layout()
      layout.addItem(horizontalSpacer, layout.rowCount(), 0, 1, layout.columnCount())
    self.setEscapeButton(QtGui.QMessageBox.Ok)

#        def resizeEvent(self, e):
##            result = QtGui.QMessageBox.event(self, e)
#    
#            self.setMinimumHeight(0)
#            self.setMaximumHeight(16777215)
#            self.setMinimumWidth(0)
#            self.setMaximumWidth(16777215)
#            self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
#    
#            textEdit = self.findChild(QtGui.QTextEdit)
#            if textEdit != None :
#                textEdit.setMinimumHeight(0)
#                textEdit.setMaximumHeight(16777215)
#                textEdit.setMinimumWidth(0)
#                textEdit.setMaximumWidth(16777215)
#                textEdit.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
#            e.accept()
#            return result
#        def event(self, event):
#  
#          result = super(MyMessageBox, self).resizeEvent(event)
#          self.setMinimumSize(event.size())
#          self.setMaximumSize(QtCore.QSize(16777215, 16777215))
#          details_box = self.findChild(QtGui.QTextEdit)
#          # 'is not' is better style than '!=' for None
#          if details_box is not None:
#              details_box.setFixedSize(details_box.sizeHint())
#          #event.accept()
#          return result
