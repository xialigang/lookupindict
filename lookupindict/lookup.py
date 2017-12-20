# -*- coding: utf-8 -*-
import lxml
import os
import re
import shutil

from subprocess import Popen
#from six import string_types
#from six.moves import configparser
import requests
from bs4 import BeautifulSoup
import re



class Lookup(object):

    WORD = ''
    localpath = ''

    #content = BeautifulSoup()

    prons = []
    meanings = []
    sentences = []

    exist_locally = False

    def __init__(self, word, **kwargs):
        """ Configures this converter. Available ``args`` are:
            - ``word``: word file or directory path
            Available ``kwargs`` are:
            - ``output_file``: path to html or PDF destination file
            - ``theme``: path to the theme to use for this presentation
        """
        self.output_dir = kwargs.get('output_dir', 'dir_lookupindict')
        self.save = kwargs.get('save', False)
        self.logger = kwargs.get('logger', None)

        self.word = word
        
        if '_' in word:
            self.WORD = word.replace('_', '')
        else:
            self.WORD = word

        path = os.getcwd()

        if not os.path.isdir(self.output_dir) and self.save:
            print 'Make the directory to save words :', self.output_dir
            os.mkdir(os.path.join(path, self.output_dir))

        self.localpath = os.path.join(self.output_dir, word)
        
        if os.path.isfile(self.localpath):
            self.exist_locally = True

        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
        headers = { 'User-Agent' : user_agent}

        #获取html
        f = requests.get('http://dict.cn/'+self.WORD, headers=headers).text
        #用BS解析html
        self.content = BeautifulSoup(f,'lxml')


    #@property
    def clear_tag(self, line):
        maxlen = len(line)
        pos1 = line.find('<', 0, maxlen)
        pos2 = line.find('>', pos1, maxlen)
        if pos1> -1 and pos2> -1:
            return self.clear_tag(line[0:pos1]+line[pos2+1:maxlen])
        else:
            return line

    def get_prons(self):
        prons0 = self.content.find_all(name='div', class_ = 'phonetic')[0]
        prons = prons0.find_all(name='bdo', lang = 'EN-US')
        for pron in prons:
            a = str(pron)
            a = self.clear_tag(a)
            self.prons.append(a+'\n')
        return
    def get_meanings(self):
        meanings0 = self.content.find_all(name='ul', class_ = 'dict-basic-ul')[0]
        meanings = meanings0.find_all('li')
        #print meanings
        #print 'len of meanings =', len(meanings)
        for m in meanings:
            m = str(m).strip()
            if 'strong' not in m:
                continue
            m = m.replace('\t', '')
            m = m.replace('\n', '')
            m = self.clear_tag(m)
            self.meanings.append(m+'\n')
        return
    def get_sentences(self):
        sentences0 = self.content.find_all(name='div', class_ = 'section sent')[0]
        sentences = sentences0.find_all('div', class_ = 'layout sort')[0].find_all('li')
        #print sentences
        #print 'len of sentences =', len(sentences)
        i_sent = 0
        for m in sentences:
            i_sent += 1
            m = str(m).strip()
            m = m.replace('\t', '')
            m = m.replace('\n', '')
            m = self.clear_tag(m)
            self.sentences.append(str(i_sent)+'. '+m+'\n')
        return
    def get_local(self):
        if not self.exist_locally:
            print 'Not found locally!'
            return
        print 'Found locally!'
        with open(self.localpath, 'r') as f:
            while 1:
                line = f.readline()
                if line == '':
                    break
                print line.strip()
        return
    def save_to_local(self):
        if self.exist_locally:
            print 'Exist locally and delete it!'
            os.remove(self.localpath)

        with open(self.localpath, 'w') as f:
            f.write(self.WORD+'\n')
            s = self.prons+self.meanings+self.sentences
            for a in s:
                f.write(a)
        print 'Save it locally to ', self.localpath,'!'
        return
    def get_from_dictcn(self):
        self.get_prons()
        self.get_meanings()
        self.get_sentences()
        s = self.prons+self.meanings+self.sentences
        print self.word
        for a in s:
            print a.strip()

    def execute(self):
        if self.exist_locally:
            self.get_local()
        print 'Here are the results from dict.cn .'
        self.get_from_dictcn()
        if self.save:
            self.save_to_local()
     
    
