from flask import render_template, url_for, request, redirect, flash
from app.user.models import UserDAO
from app.user.forms import UpdateUser
class UserController():
    def __init__(self):
        pass 

    def get_user(self,username):
        user_details = UserDAO.get_user_by_username(username=username)
        return render_template('user/user_details.html',user_details=user_details,username=username)

    
    def update_user(self,username):
        form = UpdateUser()
        if form.validate_on_submit():
            firstname = form.data.get("firstname")
            lastname = form.data.get("lastname")

            data = {
                "firstname" : firstname,
                "lastname"  : lastname
            }
            update = UserDAO.update_user_details(username,data)
            if update.matched_count == 1 : 
                flash('Your profile is saved')
                return redirect(url_for('user.update_user_details',username=username))

            else : 
                flash('Not able to save your profile please try again')
        elif request.method == "GET" :
            user_details = UserDAO.get_user_by_username(username=username)
            form.username.data = user_details.get("username")
            form.firstname.data = user_details.get("firstname") 
            form.lastname.data = user_details.get("lastname") 
            form.email.data = user_details.get("email")
        return render_template('user/update_profile.html',form=form,username=username)
