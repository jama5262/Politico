from app.api.v2.utils.validations.validation import validate
from app.api.v2.utils.validations.validation import checkIfValuesHaveFirstLetterUpperCase
from app.api.v2.utils.returnMessages import returnMessages
from app.api.database.schemaGenerator.schemaGenerator import SchemaGenerator
from app.api.database.database import Database
import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail
from flask_jwt_extended import create_access_token


class AuthModel():
    def __init__(self, data=None, id=None, token=None):
        self.tableName = "users"
        if data is not None:
            self.data = checkIfValuesHaveFirstLetterUpperCase(data)
        self.id = id
        self.token = token

    def registerUser(self):
        valid = validate(self.tableName, self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator(self.tableName, None, self.data).insterInto()
        db = Database(schema).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        return returnMessages.success(200, {
            "user": self.data,
            "msg": "Signup successfull"
        })

    def loginUser(self):
        valid = validate("userLogin", self.data)
        if valid["isValid"] is False:
            return valid["data"]
        schema = SchemaGenerator(self.tableName, None, self.data).userLogin()
        db = Database(schema, True).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 401,
                "error": "Wrong login credentials"
            }
        db["data"][0].pop("password")
        return returnMessages.success(200, {
            "user": db["data"][0],
            "msg": "Login successfull"
        })

    def sendResetEmail(self, user):
        try:
            fullName = user["first_name"] + " " + user["last_name"]
            link = ""
            print(self.token)
            sg = sendgrid.SendGridAPIClient(apikey="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")
            from_email = Email("politico-noreply@politico.com")
            to_email = Email("jama3137@gmail.com")
            subject = "Politico Password Reset"
            message = '''
                <!DOCTYPE html>
                <html>

                <head>
                <title>Password Reset</title>
                <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
                <meta content="width=device-width" name="viewport">
                <style type="text/css">
                    @font-face {
                    font-family: &#x27;
                    Postmates Std&#x27;
                    ;
                    font-weight: 600;
                    font-style: normal;
                    src: local(&#x27;
                    Postmates Std Bold&#x27;
                    ),
                    url(https://s3-us-west-1.amazonaws.com/buyer-static.postmates.com/assets/email/postmates-std-bold.woff) format(&#x27;
                    woff&#x27;
                    );
                    }

                    @font-face {
                    font-family: &#x27;
                    Postmates Std&#x27;
                    ;
                    font-weight: 500;
                    font-style: normal;
                    src: local(&#x27;
                    Postmates Std Medium&#x27;
                    ),
                    url(https://s3-us-west-1.amazonaws.com/buyer-static.postmates.com/assets/email/postmates-std-medium.woff) format(&#x27;
                    woff&#x27;
                    );
                    }

                    @font-face {
                    font-family: &#x27;
                    Postmates Std&#x27;
                    ;
                    font-weight: 400;
                    font-style: normal;
                    src: local(&#x27;
                    Postmates Std Regular&#x27;
                    ),
                    url(https://s3-us-west-1.amazonaws.com/buyer-static.postmates.com/assets/email/postmates-std-regular.woff) format(&#x27;
                    woff&#x27;
                    );
                    }
                </style>
                <style media="screen and (max-width: 680px)">
                    @media screen and (max-width: 680px) {
                    .page-center {
                        padding-left: 0 !important;
                        padding-right: 0 !important;
                    }

                    .footer-center {
                        padding-left: 20px !important;
                        padding-right: 20px !important;
                    }
                    }
                </style>
                </head>

                <body style="background-color: #f4f4f5;">
                <table cellpadding="0" cellspacing="0"
                    style="width: 100%; height: 100%; background-color: #f4f4f5; text-align: center;">
                    <tbody>
                    <tr>
                        <td style="text-align: center;">
                        <table align="center" cellpadding="0" cellspacing="0" id="body"
                            style="background-color: #fff; width: 100%; max-width: 680px; height: 100%;">
                            <tbody>
                            <tr>
                                <td>
                                <table align="center" cellpadding="0" cellspacing="0" class="page-center"
                                    style="text-align: left; padding-bottom: 88px; width: 100%; padding-left: 120px; padding-right: 120px;">
                                    <tbody>
                                    <tr>
                                        <td colspan="2"
                                        style="padding-top: 72px; -ms-text-size-adjust: 100%; -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: 100%; color: #F57C00; font-family: 'Postmates Std', 'Helvetica', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif; font-size: 48px; font-smoothing: always; font-style: normal; font-weight: 600; letter-spacing: -2.6px; line-height: 52px; mso-line-height-rule: exactly; text-decoration: none;">
                                        Politico Reset Password</td>
                                    </tr>
                                    <tr>
                                        <td style="padding-top: 48px; padding-bottom: 48px;">
                                        <table cellpadding="0" cellspacing="0" style="width: 100%">
                                            <tbody>
                                            <tr>
                                                <td
                                                style="width: 100%; height: 1px; max-height: 1px; background-color: #d9dbe0; opacity: 0.81">
                                                </td>
                                            </tr>
                                            </tbody>
                                        </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td
                                        style="-ms-text-size-adjust: 100%; -ms-text-size-adjust: 100%; -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: 100%; color: #9095a2; font-family: 'Postmates Std', 'Helvetica', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif; font-size: 16px; font-smoothing: always; font-style: normal; font-weight: 400; letter-spacing: -0.18px; line-height: 24px; mso-line-height-rule: exactly; text-decoration: none; vertical-align: top; width: 100%;">
                                        <h5>Hey, ''' + fullName + '''</h5>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td
                                        style="-ms-text-size-adjust: 100%; -ms-text-size-adjust: 100%; -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: 100%; color: #9095a2; font-family: 'Postmates Std', 'Helvetica', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif; font-size: 16px; font-smoothing: always; font-style: normal; font-weight: 400; letter-spacing: -0.18px; line-height: 24px; mso-line-height-rule: exactly; text-decoration: none; vertical-align: top; width: 100%;">
                                        You're receiving this e-mail because you requested a password reset for your Politico account.
                                        </td>
                                    </tr>
                                    <tr>
                                        <td
                                        style="padding-top: 24px; -ms-text-size-adjust: 100%; -ms-text-size-adjust: 100%; -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: 100%; color: #9095a2; font-family: 'Postmates Std', 'Helvetica', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif; font-size: 16px; font-smoothing: always; font-style: normal; font-weight: 400; letter-spacing: -0.18px; line-height: 24px; mso-line-height-rule: exactly; text-decoration: none; vertical-align: top; width: 100%;">
                                        Please click on the button below to reset your password.
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                        <a data-click-track-id="37" href="''' + link + '''"
                                            style="margin-top: 36px; -ms-text-size-adjust: 100%; -ms-text-size-adjust: 100%; -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: 100%; color: #ffffff; font-family: 'Postmates Std', 'Helvetica', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif; font-size: 12px; font-smoothing: always; font-style: normal; font-weight: 600; letter-spacing: 0.7px; line-height: 48px; mso-line-height-rule: exactly; text-decoration: none; vertical-align: top; width: 220px; background-color: #F57C00; border-radius: 28px; display: block; text-align: center; text-transform: uppercase"
                                            target="_blank">
                                            Reset Password
                                        </a>
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                        </td>
                    </tr>
                    </tbody>
                </table>
                </body>
                </html>
            '''
            content = Content("text/html", message)
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print("email sent")
        except:
            print("the was an error")

    def getSpecificUser(self):
        schema = SchemaGenerator(self.tableName, "email", None, "'" + self.id + "'").selectSpecific()
        db = Database(schema, True).executeQuery()
        if db["status"] == 400:
            return {
                "status": db["status"],
                "error": db["error"]
            }
        if not db["data"]:
            return {
                "status": 404,
                "error": "The user was not found"
            }
        if db["data"][0]["email"] == "admin@gmail.com":
            return {
                "status": 401,
                "error": "You are fobidden to reset admin account"
            }
        self.sendResetEmail(db["data"][0])
        return returnMessages.success(200, {
            "data": db["data"][0],
            "msg": db["data"][0]["email"]
        })
