# -*- coding:UTF-8 -*-

import xml.etree.ElementTree as elmTree
import xml.dom.minidom as minidom

'''
  @author: 忧里修斯 @2010-4-20
  http://www.jb51.net/article/115659.htm
  Python实现对象转换为xml的方法示例
'''

class convXml(object):

    root = None #根节点

    def __init__(self):
        pass

    @staticmethod # 创建根节点
    def createRoot(rootTag):
        root = elmTree.Element(rootTag)
        return root

    @staticmethod # 根据节点返回格式化的xml字符串
    def getXmlString(element, cset='utf-8'):
        try:
            str0 = elmTree.tostring(element, cset)
            reparsed = minidom.parseString(str0)
            return reparsed.toprettyxml(indent=" ", encoding=cset)
        except:
            print('getXmlString: Error Node, Cant NOT convert to xml')
            return ''
    
    @staticmethod # 根据传入的对象的实例，根据对象的属性生成节点，返回由节点组成的列表
    def classToElements(classobj, rootTag=None):

        attrs = None #保存对象的属性集
        elelist = [] #节点列表

        try:
            attrs = classobj.__dict__.keys()#获取该对象的所有属性(即成员变量)
        except:
            print('classToElements: Error object, Can NOT get the attribute.')
        if attrs != None and len(attrs) > 0:#属性存在
            for attr in attrs:
                attrvalue = getattr(classobj, attr)#属性值
                #属性节点
                attrE = elmTree.Element(attr)
                attrE.text = attrvalue

                #加入节点列表
                elelist.append(attrE)
        return elelist
    
    @staticmethod # Python自定义模型类转换成xml，转换成功返回的是xml根节点，否则返回None
    def classToXML(classobj, rootTag=None):
        try:
            classname = classobj.__class__.__name__ #类名
            if rootTag != None:
                root = convXml.createRoot(rootTag)
            else:
                root = convXml.createRoot(classname)

            if type(classobj)==int or type(classobj)==str:
                root.text = str(classobj)
                return root

            elelist = convXml.collectionToXML(classobj, rootTag) 
            for ele in elelist:
                root.append(ele)

            return root
        except:
            print('classToXML: Error Convert, Error object.')
            return None

    @staticmethod # 集合（列表、元组、字典）转换为xml，转换成功返回的是xml根节点，否则返回None
    def collectionToXML(listobj, rootTag='root'):
        try:
            classname = listobj.__class__.__name__ #类名
            root = convXml.createRoot(rootTag)
            if isinstance(listobj, list) or isinstance(listobj, tuple):#列表或元组
                if len(listobj) >= 0:
                    for obj in listobj:#迭代列表中的对象
                        itemE = convXml.classToXML(obj)
                        root.append(itemE)
            elif isinstance(listobj, dict):#字典
                if len(listobj) >= 0:
                    for key in listobj:#迭代字典中的对象
                        obj = listobj[key]
                        itemE = convXml.classToXML(obj, key)
                        root.append(itemE)
            else:
                print('listToXML: Convert Error, '+classname+' NOT collection type.')
            return root
        except:
            print('collectionToXML: Convert Error, collection convert to xml fail.')
            return None

