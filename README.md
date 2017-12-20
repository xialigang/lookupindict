
## Description

This little tool is actually like a dictionary. It is to look up a word  or a phrase from dict.cn .

## How to get it ?

    git clone https://github.com/xialigang/lookupindict
	cd lookupindict
	source install.sh

## How to use it?

- Look up a word

        lookupindict python
        

- Look up a phrase

        lookupindict look_up
	   

- Look up a word/phrase and save it to a directory, the default path is './dir_lookupindict'.

        lookupindict python -s
        
- You can specify the directory with the option [-l/--localpath].

        lookupindict python -s -l where-I-like
        

If you have specified the directory, the tool will look up the word/phrase locally and then look it up from dict.cn .

## An Example 

	Here are the results from dict.cn .
	python
	['paɪθən]
	['paɪθɑːn]
	n.大蟒；巨蟒
	1. A giant python sure gave these folks a scare.这条巨蟒足以让村民大吃一惊。
	2. An old woman narrowly escaped a python that attacked her in her bathroom.一名老妇人在浴室受到一条巨蟒的攻击，老妇人侥幸逃过攻击。


## Contact and other information

    Ligang Xia, <ligang.xia@cern.ch>

## Free to use it and have a good time!
    


