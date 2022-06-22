from flask import Flask, abort, jsonify
app = Flask(__name__)

films = {1: {'nom1', 'date de création1', 'description1'}, 2: {'nom2', 'date de création2', 'description2'}, 3: {'nom3', 'date de création3', 'description3'}}

@app.route('/moovies/<id>')
def get_id_moovie(id):
    try:
        print(int(id))
    except:
        abort(406)
    try:
        return "%s" % (films[int(id)])
    except:
        abort(404)
    #return id
@app.route('/moovies/')
def get_all_moovies():
    return "%s" % (films.values())
    

if __name__ == '__main__':
    app.run(host="0.0.0.0")
