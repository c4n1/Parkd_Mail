import scrape
import send_email
import get_config # Getting config from .ini

def main():
	#Get Dict of trucks today
	Trucks_Dict = scrape.main()

	#Get Addresses to deliver mail to
	to = ['CurtinParkd@gmail.com', 'oliver.hills@r-group.com.au']

	#Get Gmail config from .ini
	gmail_config = get_config.get_config_gmail('config.ini')

	#Send the emails
	send_email.Send_Mail(gmail_config['Gmail_User'], gmail_config['Gmail_Pass'], to, Trucks_Dict)

if __name__ == "__main__":
    main()
