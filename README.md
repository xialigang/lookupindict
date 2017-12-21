
## Description

This little tool is actually like a dictionary. It is to look up a word  or a phrase from dict.cn .

## How to get it ?

    git clone https://github.com/xialigang/lookupindict
	cd lookupindict
	source install.sh

## How to use it?

- Look up a word

        lookupindict python
        

- Look up a phrase ('\' is needed before a blank)

        lookupindict look\ up
	   

- Look up a word/phrase and save it to a directory, the default path is './dir_lookupindict'.

        lookupindict python -s
        
- You can specify the directory with the option [-l/--localpath].

        lookupindict python -s -l where-I-like
        

If you have specified the directory, the tool will look up the word/phrase locally and then look it up from dict.cn .

## An Example (`lookupindict python`) 

	Here are the results from dict.cn .
	python
	['paɪθən]
	['paɪθɑːn]
	n.大蟒；巨蟒
	1. A giant python sure gave these folks a scare.这条巨蟒足以让村民大吃一惊。
	2. An old woman narrowly escaped a python that attacked her in her bathroom.一名老妇人在浴室受到一条巨蟒的攻击，老妇人侥幸逃过攻击。

## Another Example (`lookupindict 科研`)

	Here are the results from dict.cn .
	科研
	1. 他为自己在科研方面所取得的巨大成就而自豪。He is proud of his great success in scientific researches.
	2. 他的传记就是一部科研记实。His biography is a saga of scientific research.
	3. 必须把滥竽充数的科研人员调到其他工作岗位上去。The scientific research personnel who held the post without qualification must be transferred to another post.
	4. 大学的任务是教学和科研。The mission of a university is teaching and research.

## Contact and other information

    Ligang Xia, <ligang.xia@cern.ch>

## Free to use it and have a good time!
    


