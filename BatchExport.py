#!/usr/bin/env python
# encoding: utf-8
'''
@author: Wanghan
@contact: panda@cug.edu.cn
@software: Pycharm
@file: BatchExport.py
@time: 2018/8/3 10:08
@desc:
'''
import arcpy
JD_Dict ={"DLJD":"大浪街道","FCJD":"福城街道","GHJD":"观湖街道","GLJD":"观澜街道","LHJD":"龙华街道","MZJD":"民治街道"}
mxd_list= ["DLJD","FCJD","GHJD","GLJD","LHJD","MZJD"]
Pic_dict ={"润城":"GHJD","观城":"GHJD","松元厦":"GHJD","新田":"GHJD","樟坑径":"GHJD","鹭湖":"GHJD",
"民治":"MZJD","民新":"MZJD","民乐":"MZJD","上芬":"MZJD","龙塘":"MZJD","新牛":"MZJD","北站":"MZJD","民强":"MZJD","大岭":"MZJD","樟坑":"MZJD","白石龙":"MZJD","民泰":"MZJD",
"景龙":"LHJD","龙园":"LHJD","华联":"LHJD","玉翠":"LHJD","三联":"LHJD","清湖":"LHJD","清华":"LHJD","油松":"LHJD","松和":"LHJD","富康":"LHJD", "大浪":"DLJD","浪口":"DLJD",
"龙胜":"DLJD","龙平":"DLJD","新石":"DLJD","同胜":"DLJD","高峰":"DLJD","福民":"FCJD","大水坑":"FCJD","章阁":"FCJD","茜坑":"FCJD","桔塘":"FCJD","新澜":"GLJD","大水田":"GLJD",
"桂花":"GLJD","库坑":"GLJD","黎光":"GLJD","大富":"GLJD","牛湖":"GLJD","广培":"GLJD","桂香":"GLJD","君子布":"GLJD"}

for mxd_path in  mxd_list:
    print
    #mxd = arcpy.mapping.MapDocument("C:\Users\lenovo\Desktop\外事制图\出图\分街道"+"\\"+mxd_path+".mxd")
    #mxd = arcpy.mapping.MapDocument("E:\Export" + "\\" + mxd_path+ ".mxd")
    mxd = arcpy.mapping.MapDocument("E:\Export" + "\DS\\" + mxd_path + ".mxd")
    jiedao =""
    for pic in  Pic_dict:
        if str(Pic_dict[pic])==mxd_path:
            print "即将导出：" +JD_Dict[mxd_path] +"  " +pic + " 社区 "
            pageID = mxd.dataDrivenPages.getPageIDFromName(str(pic))
            mxd.dataDrivenPages.currentPageID = pageID
            print "Exporting page {0} of {1}".format(str(mxd.dataDrivenPages.currentPageID), str(mxd.dataDrivenPages.pageCount))
            #arcpy.mapping.ExportToPNG(mxd, "E:\Export\OutPng" +"\\" +JD_Dict[mxd_path] +"_"+str(pic) + ".png",resolution=72,background_color="transparent_color")#####a300 600
            arcpy.mapping.ExportToPNG(mxd, "E:\Export\OutPngDS" + "\\" + JD_Dict[mxd_path] + "_" + str(pic) + ".png",
                                      resolution=300, background_color="transparent_color")  #####a300 600
        else:
            continue
    del mxd