#! / usr / bin / env python
# - * - kodlama: UTF-8 - * -

dan  urllib2  ithalat  Request , urlopen , UrlError , httpError

def  Boşluk ( j ):
	i  =  0
	ise  i <= j :
		 "" yazdır ,
		i + = 1


def  findAdmin ():
	f  =  open ( "link.txt" , "r" );
	link  =  raw_input ( "Site Adresini Giriniz \ n (ör: ornek.com veya www.ornek.com):" )
	print  " \ n \ n Tespit Edilen Linkler: \ n "
	 True iken :
		sub_link  =  f . readline ()
		eğer  değil  sub_link :
			kırmak
		req_link  =  "http: //" + bağlantı + "/" + alt_link
		req  =  İstek ( req_link )
		dene :
			yanıtı  =  urlopen ( req )
		 e olarak HTTPError  dışında : 
			devam et
		hariç  UrlError  olarak  e :
			devam et
		başka :
			yazdırmak  "Tamam =>" , req_link

def  Kredi ():
	
Boşluk ( 9 ); baskı  "| <<<<<<<<<<<<<<<< | >>>>>>>>>>>>>>>>>> |"
Boşluk ( 9 ); yazdır  "| +++ Yönetici Paneli Bulucu v | +++ |"
Boşluk ( 9 ); print  "| Kodlayan TurKLoJeN |"
Boşluk ( 9 ); print  "| Türk Pentester |"
Boşluk ( 9 ); baskı  "| <<<<<<<<<<<<<<<< | >>>>>>>>>>>>>>>>>> |"
    
Kredi ()
findAdmin ()

