import log
import mailSender
import salesNotifierModel

from flask import request
from flask import render_template
from flask import Flask

app = Flask(__name__)

logger = log.setup_custom_logger('root')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/send-email-to-everyone')
def sendEmailToEveryone():
    htmlMessage = salesNotifierModel.buildEmailMessage()

    if htmlMessage == null:
        logger.info('There are no games on sale')
        return('There are no games on sale')

    logger.info('Getting address list')
    receiversAddress = salesNotifierModel.getReceiversAddressList()

    logger.info('Starting to send emails')
    for email in receiversAddress:
        logger.info('Sending mail to: ' + email['Address'])
        mailSender.sendMail(htmlMessage, email['Address'])
        logger.info('Mail to ' + email['Address'] + ' sent')

    logger.info('Execution finished')

    return('Execution finished')


@app.route('/send-individual-email')
def sendIndividualEmail():
    email = request.args.get('email')
    successMessage = ""
    errorMessage = ""
    if email is not "":
        htmlMessage = salesNotifierModel.buildEmailMessage()

        if htmlMessage == null:
            logger.info('There are no games on sale')
            return('There are no games on sale')

        mailSender.sendMail(htmlMessage, email)
        successMessage = "Mail sent!"
    else:
        errorMessage = "There was an error sending the email"
    return render_template('index.html', message=successMessage, error=errorMessage)

@app.route('/logs')
def printLogs():
    


@app.route('/add-email-to-list')
def addEmailToList():
    return "addEmailToList: TODO"


@app.route('/remove-email-from-list')
def removeEmailFromList():
    return "removeEmailFromList: TODO"


if __name__ == '__main__':
    app.run()
