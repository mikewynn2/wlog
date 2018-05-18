from flask import Flask
from flask import request
from flask import jsonify, redirect
from db import DBEngine


app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/post')


@app.route('/user/<int:user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    return jsonify({'user': DBEngine().get_user(user_id)}), 200


@app.route('/user/', methods=['GET'], strict_slashes=False)
def get_users():
    return jsonify({'users': DBEngine().get_users()}), 200


@app.route('/post/<int:post_id>/delete', methods=['GET'], strict_slashes=False)
def delete_post(post_id):
    DBEngine().delete_post(post_id)
    return '', 200


@app.route('/user/<int:user_id>/delete', methods=['GET'], strict_slashes=False)
def delete_user(user_id):
    DBEngine().delete_user(user_id)
    return '', 200


@app.route('/comment/<int:comment_id>/delete', methods=['GET'], strict_slashes=False)
def delete_comment(comment_id):
    DBEngine().delete_comment(comment_id)
    return '', 200


@app.route('/user/', methods=['POST'], strict_slashes=False)
def create_user():
    username = request.form['username']
    email = request.form['email']
    return jsonify({'user': DBEngine().create_user(username, email)}), 201


@app.route('/post/', methods=['POST'], strict_slashes=False)
def create_post():
    author = request.form['author']
    title = request.form['title']
    content = request.form['content']
    return jsonify({'post': DBEngine().create_post(author, title, content)}), 201


@app.route('/comment/post/<int:post_id>', methods=['POST', 'GET'], strict_slashes=False)
def get_comments_or_create_comment(post_id):
    if request.method == 'POST':
        author = request.form['author']
        content = request.form['content']
        return jsonify({'comment': DBEngine().create_comment(author, post_id, content)}), 201

    return jsonify({'comments': DBEngine().get_comments(post_id)}), 200


@app.route('/post/<int:post_id>', methods=['GET'], strict_slashes=False)
def get_post(post_id):
    return jsonify({'post': DBEngine().get_post(post_id)}), 200


@app.route('/post/', methods=['GET'], strict_slashes=False)
def get_posts():
    return jsonify({'post': DBEngine().get_posts()}), 200


@app.route('/comment/<int:comment_id>', methods=['GET'], strict_slashes=False)
def get_comment(comment_id):
    return jsonify({'comment': DBEngine().get_comment(comment_id)}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
