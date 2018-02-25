# -*- coding:UTF-8 -*-

'''
    convXml
'''


'''
  Created on 2010-4-20
  @author: 忧里修斯
  http://www.jb51.net/article/115659.htm
  Python实现对象转换为xml的方法示例
'''
import xml.etree.ElementTree as elmTree
import xml.dom.minidom as minidom

class convXml(object):
    '''
      实现Python对象与xml之间的相互转换
    '''
    root = None#根节点

    def __init__(self):
        pass

    @staticmethod
    def createRoot(rootTag):
        '''
          创建根节点
        '''
        root = elmTree.Element(rootTag)
        return root

    @staticmethod
    def getXmlString(element, cset='utf-8'):
        '''
          根据节点返回格式化的xml字符串
        '''
        try:
            str0 = elmTree.tostring(element, cset)
            #print(str0) 
            reparsed = minidom.parseString(str0)
            return reparsed.toprettyxml(indent=" ", encoding=cset)
        except:
            print('getXmlString:传入的节点不能正确转换为xml，请检查传入的节点是否正确')
            return ''
    
    @staticmethod
    def classToElements(classobj, rootTag=None):
        '''
          根据传入的对象的实例，根据对象的属性生成节点，返回由节点组成的列表
          classobj：对象的实例
          rootTag：根节点名称
        '''
        attrs = None #保存对象的属性集
        elelist = [] #节点列表
        try:
            attrs = classobj.__dict__.keys()#获取该对象的所有属性(即成员变量)
        except:
            print('classToElements:传入的对象非法，不能正确获取对象的属性')
        if attrs != None and len(attrs) > 0:#属性存在
            for attr in attrs:
                attrvalue = getattr(classobj, attr)#属性值
                #属性节点
                attrE = elmTree.Element(attr)
                attrE.text = attrvalue
                #加入节点列表
                elelist.append(attrE)
        return elelist
    
    @staticmethod
    def classToXML(classobj, rootTag=None):
        '''
          Python自定义模型类转换成xml，转换成功返回的是xml根节点，否则返回None
          classobj：对象的实例
          rootTag：根节点名称
        '''
        try:
            classname = classobj.__class__.__name__ #类名
            if rootTag != None:
                root = convXml.createRoot(rootTag)
            else:
                root = convXml.createRoot(classname)
                elelist = convXml.classToElements(classobj, rootTag)
            for ele in elelist:
                root.append(ele)
            return root
        except:
            print('classToXML:转换出错，请检查的传入的对象是否正确')
            return None
    
    @staticmethod
    def collectionToXML(listobj, rootTag='root'):
        '''
          集合（列表、元组、字典）转换为xml，转换成功返回的是xml根节点，否则返回None
        '''
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
                        itemE = convXml.classToXML(obj)
                        itemE.set('key', key)
                        root.append(itemE)
            else:
                print('listToXML：转换错误，传入的对象：'+classname+'不是集合类型')
            return root
        except:
            print('collectionToXML：转换错误，集合转换成xml失败')
            return None
