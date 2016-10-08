#!/usr/bin/env python2.7

import os, uuid, json,flask

from flask import Flask, request, render_template, g, redirect, Response


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)



@app.route('/')
def main():
    return render_template('first.html')

@app.route('/submitFirstForm', methods=['POST'])
def addFirstForm():
  #userid = os.urandom(24)
  '''
  formDict = dict()
  mysql_dao.createNewUser(dbcon,,d)
  user = User(name,passwrd,True);
  login_user(user)
  next = flask.request.args.get('next')
        # next_is_valid should check if the user has valid
        # permission to access the `next` url
  
  formDict['FirstName'] = str(request.form['FNAME'])
  formDict['LastName'] = str(request.form['LNAME'])
  formDict['DOB'] = str(request.form['DATEOFBIRTH'])
  formDict['Email'] = str(request.form['EMAIL'])
  formDict['AlternativeEmail'] = str(request.form['ALTERNATIVE_EMAIL'])
  formDict['Phone'] = str(request.form['PERMANENT_PHONE'])
  formDict['PermStreetAdr1'] = str(request.form['PERMANENT_ADDRESS1'])
  formDict['PermStreetAdr2'] = str(request.form['PERMANENT_ADDRESS2'])
  formDict['PermanentCity'] = str(request.form['PERMANENT_CITY'])
  formDict['PermanentState'] = str(request.form['PERMANENT_STATE'])
  formDict['PermanentZipCode'] = str(request.form['PERMANENT_ZIP'])
  formDict['CampusAdr1'] = str(request.form['SCHOOL_ADDRESS1'])
  formDict['CampusAdr2'] = str(request.form['SCHOOL_ADDRESS2'])
  formDict['CampusCity'] = str(request.form['CAMPUS_CITY'])
  formDict['CampusState'] = str(request.form['CAMPUS_STATE'])
  formDict['CampusZipCode'] = str(request.form['CAMPUS_ZIP'])
  formDict['HomeCity'] = str(request.form['HOMECITY'])
  formDict['UserId'] = str(request.form['HOMESTATE'])

  formDict['Ethnicity'] = str(request.form['userid'])
  formDict['CitizenshipStatus'] = str(request.form['userid'])

  formDict['MotherDegree'] = str(request.form['MOTHERDEGREE'])
  formDict['FatherDegree'] = str(request.form['FATHERDEGREE'])

  formDict['ClassCompletedSpring'] = str(request.form['CLASSCOMPLETE'])

  formDict['GraduationMonth'] = str(request.form['userid'])
  formDict['GraduationYear'] = str(request.form['userid'])
  formDict['CumulativeGPA'] = str(request.form['userid'])
  formDict['AdvancedDegreeObjective'] = str(request.form['userid'])
  formDict['IsUndergraduateResearchProgramOffered'] = str(request.form['userid'])
  formDict['HowDidYouHear'] = str(request.form['userid'])
  formDict['AnyOtherAmgenScholarsSite'] = str(request.form['userid'])
  formDict['YesOtherAmgenScholarsSite'] = str(request.form['userid'])
  formDict['PastAmgenScholarParticipation'] = str(request.form['userid'])
  formDict['OriginalResearchPerformed'] = str(request.form['userid'])
  formDict['CanArriveAtColumbiaMemorialDay'] = str(request.form['userid'])
  formDict['ArriveAtColumbiaComments'] = str(request.form['userid'])
  formDict['CurrentlyAttendingUniversity'] = str(request.form['userid'])
  formDict['Major'] = str(request.form['userid'])
  formDict['DateSpringSemesterEnds'] = str(request.form['userid'])

  formDict['Gender'] = str(request.form['GENDER'])
  
  print(str(request.form['INDIAN']))
  print(str(request.form['BLACK']))
  print(str(request.form['PACIFIC']))
  print(str(request.form['MEXICAN']))
  print(str(request.form['INDIAN']))
  print(str(request.form['MIDDLE']))
  print(str(request.form['WHITE']))
  print(str(request.form['other']))
  print(str(request.form['decline']))
  
  #print(str(request.form['ethinicity']))
  if request.form.get('AMGENSITE'):
    print(str(request.form.get('AMGENSITE')))
  
  if request.form.get('UNIVERSITYSITE'):
    print(str(request.form.get('UNIVERSITYSITE')))
  if request.form.get('UNIVERSITYSITENAME'):
    print(str(request.form.get('UNIVERSITYSITENAME')))
  if request.form.get('EMAILANNOUNCEMENT'):
    print(str(request.form.get('EMAILANNOUNCEMENT')))
  '''
  print("Inside")
  if request.form['submitBut'] == 'Next':
    print("Next")
  elif request.form['submitBut'] == 'Back':
    print("Back")
  return flask.render_template('first.html')



if __name__ == "__main__":
  app.run()
