from flask import Flask, render_template,request
import pymysql
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
	return render_template('t3_index1.html', \
		title = 'Form Sample(get)', \
		message = 'Where do you want to go?')


def getConnection():
	return pymysql.connect(
		host='localhost',
		db='first_db',
		user='testuser',
		password='password',
		charset='utf8',
		cursorclass=pymysql.cursors.DictCursor
		)


@app.route('/', methods=['POST'])
def select_sql():
	connection = getConnection()
	message = "test"
	names = request.form.getlist('checkbox')

	list1s=[]
	for name in names:

		cursor = connection.cursor()
		sql = "select Country, Agency, email from tb3 where Country=%s";
		cursor.execute(sql, (name,))
		
		list1 = cursor.fetchall()
		list1s.append(list1)
		

	cursor.close()
	connection.close()
	
	print(list1s)
	

	return render_template( 'index2.html', list1s = list1s)

if __name__ == '__main__':
	app.run()
