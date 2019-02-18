from flask import render_template,request,redirect,url_for,abort
from ..models import User,Blog,Comment
from .forms import UpdateProfile,BlogForm,CommentForm,SubscriberForm
from . import main
from .. import db,photos
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Subscriber
from datetime import datetime
from ..email import mail_message


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user) 

#a view function that will handle an update request
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)


#routing to display admins profile picture
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

#routing for may food blog/saving and displaying/2.for the user to receive an email each time a new blog is posted
@main.route('/food', methods=['GET','POST'])
@login_required
def food():
    blog_form=BlogForm()
    if blog_form.validate_on_submit():        
        food = Blog(category=blog_form.category.data,title = blog_form.title.data)
        db.session.add(food)
        db.session.commit()
    subscribers = Subscriber.query.all()
    for email in subscribers:
        mail_message("Hey Welcome To My Blog ","email/welcome_post",email.email,subscribers=subscribers)
    return render_template('food.html',blog_form=blog_form) 

#routing for subscribers/receive email after subscription
@main.route('/', methods=['GET','POST'])
def subscriber():
    subscriber_form=SubscriberForm()
    if subscriber_form.validate_on_submit():
        subscriber= Subscriber(email=subscriber_form.email.data,title = subscriber_form.title.data)
        db.session.add(subscriber)
        db.session.commit()
        mail_message("Hey Welcome To My Blog ","email/welcome_subscriber",subscriber.email,subscriber=subscriber)
    subscriber = Blog.query.all()
    food = Blog.query.all()
    return render_template('index.html',subscriber=subscriber,subscriber_form=subscriber_form,food=food) 

#routing for the comments to display for each blog
@main.route('/comments/<int:id>', methods=['GET','POST'])
def comment(id):
    comment_form=CommentForm()
    if comment_form.validate_on_submit():
        new_comment = Comment(description=comment_form.description.data,blog_id=id)
        db.session.add(new_comment)
        db.session.commit()
    comments = Comment.query.filter_by(blog_id=id)
    return render_template('comment.html',comment_form=comment_form,comments=comments)    

#deleting each blog only if each user is authenticated
@main.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    try:
        if current_user.is_authenticated:
            blog = Blog.query.filter_by(id=id).all()
            for blogs in blog: 
                db.session.delete(blogs)
                db.session.commit()
            return redirect(url_for('main.food'))
        return ''
    except Exception as e:
        return(str(e))    

#deleting a comment by the admin
@main.route('/delete1/<int:id>', methods=['GET','POST'])
def delete1(id):
    try:
        if current_user.is_authenticated:
            comment_form=CommentForm()
            comment = Comment.query.filter_by(comment_id=id).first()
            for comments in comment: 
                db.session.delete(comment)
                db.session.commit()
            return redirect(url_for('main.comment'))
        return ''
    except Exception as e:
        return(str(e))    




# @app.route('/delete', methods=['DELETE'])
# def delete_entry(postID):
#     if not session.get('logged_in'):
#         abort(401)
#     g.db.execute('delete from entries WHERE id = ?', [postID])
#     flash('Entry was deleted')
#     return redirect(url_for('show_entries'))           








