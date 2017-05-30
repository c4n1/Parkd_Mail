import scrape
import send_email
import get_config # Getting config from .ini
import get_email_addresses


Area = "Tech Park"
#Area = "Hexagon" #Can be useful to test multiple truck conditions

def main():
	#Set area to look at
	Area = "Tech Park"
	#Area = "Hexagon" #Can be useful to test multiple truck conditions

	#Get Dict of trucks today
	Trucks_Dict = scrape.return_trucks(Area)

	#Get Addresses to deliver mail to
	to = get_email_addresses.read_emails('emails.txt')
	#to = ['CurtinParkd@gmail.com', 'oliver.hills@r-group.com.au']

	#Get Gmail config from .ini
	gmail_config = get_config.get_config_gmail('config.ini')

	#Send the emails
	send_email.Send_Mail(gmail_config['Gmail_User'], gmail_config['Gmail_Pass'], to, Trucks_Dict)

if __name__ == "__main__":
    main()
