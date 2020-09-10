from server import *
# aqui se importarian los modelos



if __name__ == "__main__":
	app.run(port=config["PORTAPI"], debug=config['DEBUG'])
 