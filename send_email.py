import smtplib # Sending Emails
import get_config # Getting config from .ini
from email.mime.multipart import MIMEMultipart # Crafting emails
from email.mime.text import MIMEText # Crafting emails


# http://stackabuse.com/how-to-send-emails-with-gmail-using-python/
# https://docs.python.org/2/library/email-examples.html

def Send_Mail (user, password, to, Trucks_Dict):



    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Parkd Trucks Today"
    msg['From'] = user
    msg['To'] = ", ".join(to)

    truck_body_text = ""
    truck_body_html = ""
    for Truck in Trucks_Dict:
        truck_body_text = truck_body_text + "\n %s - %s" % (Truck, Trucks_Dict[Truck])
        truck_body_html = truck_body_html + '<br><a href="%s">%s</a>' % (Trucks_Dict[Truck], Truck)

    text = truck_body_text

    html = """\
    <html>
        <head></head>
        <body>
            <p>
                Hi!<br>
                Your Curtin Parkd trucks today are:-<br>
                %s
                <br><br> More info can be found on the <a href="http://news.curtin.edu.au/events/parkd-curtin/">Curtin Parkd website</a>

            </p>
        </body>
    </html>
    """ % (truck_body_html)

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    
    msg.attach(part1)
    msg.attach(part2)

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, to, msg.as_string())
        server.close()

        print('Email sent!')
    except:  
        print ('Something went wrong...')


def main():
    #Pull config from file
    gmail_config = get_config.get_config_gmail('config.ini')

    #Create some dummy imputs for testing 
    to = ['CurtinParkd@gmail.com', 'oliver.hills@r-group.com.au']
    Trucks_Dict = {' Pauly K’s Kitchen': 'https://www.facebook.com/paulykskitchen', ' Miss Lucy Delicious Foods': 'https://www.facebook.com/misslucybaravanthevintagecaravan', ' Braised Bros': 'https://www.facebook.com/braisedbros', ' Treacle Treat': 'https://www.facebook.com/TreacleTreat'}

    #Send emails
    Send_Mail(gmail_config['Gmail_User'], gmail_config['Gmail_Pass'], to, Trucks_Dict)


if __name__ == "__main__":
    main()
