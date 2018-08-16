#!/usr/bin/env python
# encoding: utf-8
'''
@author: Wanghan
@contact: panda@cug.edu.cn
@software: Pycharm
@file: AutoSetPage.py
@time: 2018/8/1 20:06
@desc:
'''

import arcpy

class AutoSetLayout(object):
    __mxd = None
    __df=None
    __lyr =None
    __currentObExtent =None
    __outFolder =r'E:\OutPut'
    __currentRow =None
    def __init__(self,Mxd_File,dfName,lyrName):
        self.__mxd =arcpy.mapping.MapDocument(Mxd_File)
        self.__df = arcpy.mapping.ListDataFrames(self.__mxd,dfName)[0]
        self.__lyr = arcpy.mapping.ListDataFrames(self.__mxd,lyrName,self.__dfNameMain)[0]
    #根据唯一值字段筛选要素，返回要素记录
    def GetGeoObject(self,Filed,FiledValue):
        rows = arcpy.SearchCursor(self.__lyr,self.__df)
        for row in rows:
            fv = str(row.getValue(Filed))
            if FiledValue == fv :
                self.__currentRow = row
            else :
                self.__currentRow=None
                continue

    def ExportToJpeg(self,NameField):
        if self.__currentRow !=None:
            self.__currentObExtent = self.__currentRow.shape.extent
            self.__df.panToExtent(self.__currentObExtent)
            outFile = self.__outFolder +u"\\" + self.__currentRow.getValue(NameField) + ".jpeg"
            arcpy.mapping.ExportToJPEG(self.__mxd,outFile,self.__df,resolution=300)
            arcpy.RefreshActiveView()
            arcpy.RefreshTOC()
