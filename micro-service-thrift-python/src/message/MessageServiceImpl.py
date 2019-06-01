# coding: utf-8
from src.message.api import MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '18202417075@163.com'
authcode = 'winter123'
class MessageServiceHandler:
    def sendMobileMessage(self, mobile, message):
        print("send mobile message, mobile: {}, message: {}".format(mobile, message))
        return True

    def sendEmailMessage(self, email, message):
        print("send email message, email: {}, message: {}".format(email, message))
        messageObj = MIMEText(message, "plain", "utf-8")
        messageObj['From'] = sender
        messageObj['To'] = email
        messageObj['Subject'] = Header('kepler test', 'utf-8')
        try:
            smtpObj = smtplib.SMTP('smtp.163.com')
            smtpObj.login(sender, authcode)
            smtpObj.sendmail(sender, [email], messageObj.as_string())
            print('send mail succcess')
            return True
        except smtplib.SMTPException as ex:
            print("send error!!")
            print(ex)
            return False

if __name__ == '__main__':
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.TServerSocket("localhost", "9090")
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("python thrift server start")
    server.serve()
    print("python thrift server exit")


