import mailSender
import salesNotifierModel

from flask import request
from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/send-email-to-everyone')
def sendEmailToEveryone():
    htmlMessage = salesNotifierModel.buildEmailMessage()

    if htmlMessage is None:
        return('There are no games on sale')

    receiversAddress = salesNotifierModel.getReceiversAddressList()

    for email in receiversAddress:
        mailSender.sendMail(htmlMessage, email['Address'])

    return('Execution finished')


@app.route('/send-individual-email')
def sendIndividualEmail():
    email = request.args.get('email')
    successMessage = ""
    errorMessage = ""
    if email is not "":
        htmlMessage = salesNotifierModel.buildEmailMessage()

        if htmlMessage == None:
            return('There are no games on sale')

        mailSender.sendMail(htmlMessage, email)
        successMessage = "Mail sent!"
    else:
        errorMessage = "There was an error sending the email"
    return render_template('index.html', message=successMessage, error=errorMessage)


@app.route('/add-email-to-list')
def addEmailToList():
    return "addEmailToList: TODO"


@app.route('/remove-email-from-list')
def removeEmailFromList():
    return "removeEmailFromList: TODO"


if __name__ == '__main__':
    app.run()
