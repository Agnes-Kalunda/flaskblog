from flask import Flask,render_template , url_for,request,redirect
from . import main
from flask_login import login_required,current_user
from app.models import User,Post,Comment
from .. import db,photos
# import forms
# import models

@main.route('/')
def home():


    return render_template('display_posts.html')

@main.route('/display_all', methods= ['POST','GET'])
def displayposts():
     posts = Post.query.all()
     return render_template('display_posts.html',posts=posts)


@main.route('/about')
def about():
    return render_template('about.html',title='About')
@main.route('/subscribe')
def subscribe():
    return render_template('subcription.html',title='Subscribe')
@main.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username = username).first()
    return render_template('profile.html',title='Profile',user=user)

@main.route('/write_post/new',methods= ['POST','GET'])
@login_required
def write_post():
    if request.method == 'POST':
        form = request.form
        title = form.get("title")
        content = form.get("content")
        category= form.get("category")

        if  title==None or content==None :
            error = "Post must have some content and title"
            return render_template('write_post.html', error=error)
        else:
            post = Post( title=title,content=content,category=category,author = current_user.username, user_id= current_user.id)
            post.save_post()
            return redirect(url_for("main.displayposts"))            
    return render_template('write_post.html',title='Write')



@main.route('/<username>/update/pic', methods = ['POST'])
@login_required
def update_profile_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_img = path
        db.session.commit()

    return redirect(url_for('main.profile', username = username))

@main.route('/display_all/update_post/<int:post_id>')
@login_required
def update_post(post_id):


    return redirect(url_for('main.displayposts'))

@main.route('/delete_post/<int:post_id>',methods= ['POST','GET'])
@login_required
def delete_post(post_id):
    post= Post.query.filter_by(id = post_id).first()
    post.delete_post()


    return redirect(url_for('main.displayposts'))

@main.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)