from flask import Flask
from flask import jsonify, redirect
from db import DBEngine


app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/user')


@app.route('/user/<int:user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    return jsonify(DBEngine().get_user(user_id)), 200


@app.route('/user/', methods=['GET'], strict_slashes=False)
def get_users():
    return jsonify({'users': DBEngine().get_users()}), 200


@app.route('/post/<int:post_id>', methods=['GET'], strict_slashes=False)
def delete_post(post_id):
    return jsonify({DBEngine().delete_post(post_id)}), 200


@app.route('/user/<int:user_id>', methods=['GET'], strict_slashes=False)
def delete_user(user_id):
    return jsonify({DBEngine().delete_user(user_id)}), 200


@app.route('/comment/<int:comment_id>', methods=['GET'], strict_slashes=False)
def delete_comment(comment_id):
    return jsonify({DBEngine().delete_comment(comment_id)}), 200


@app.route('/user/', methods=['POST'], strict_slashes=False)
def create_user():
    username = 'stupid'
    email = 'mike@dumb.com'
    return jsonify({DBEngine().create_user(username, email)}), 201


@app.route('/post/', methods=['POST'], strict_slashes=False)
def create_post():
    author = 1
    title = 'this is a title'
    content = 'this is some content'
    return jsonify({DBEngine().create_post(author, title, content)}), 201


@app.route('/comment/post/<int:post_id>', methods=['POST'], strict_slashes=False)
def create_comment():
    author = 1
    post_id = 1
    content = 'this is bullshit'
    return jsonify({DBEngine().create_user(author, post_id, content)}), 201


@app.route('/post/<int:post_id>', methods=['GET'], strict_slashes=False)
def get_post(post_id):
    return jsonify({DBEngine().get_post(post_id)}), 200


@app.route('/post/', methods=['GET'], strict_slashes=False)
def get_posts():
    return jsonify({'posts': DBEngine().get_posts()}), 200


@app.route('/comment/<int:comment_id>', methods=['GET'], strict_slashes=False)
def get_comment(comment_id):
    return jsonify({DBEngine().get_comment(comment_id)}), 200


@app.route('/comment/post/<int:post_id>', methods=['GET'], strict_slashes=False)
def get_comments(post_id):
    return jsonify({'comments': DBEngine().get_comments(post_id)}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
