import webapp2
import jinja2
import os
import calendar
from random import randint

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

weekday = {
#31
'1':{'1':'J. Edgar Hoover',
     '2':'Isaac Asimov',
     '3':'Mel Gibson',
     '4':'Marilyn Manson',
     '5':'Diane Keaton',
     '6':'Norman Reedus',
     '7':'Nicolas Cage',
     '8':'Elvis Presley',
     '9':'Richard M. Nixon',
     '10':'Rod Stewart',
     '11':'Rod Taylor',
     '12':'Howard Stern',
     '13':'Julia Louis-Dreyfus',
     '14':'Benedict Arnold',
     '15':'Martin Luther King Jr.',
     '16':'Andre Michelin',
     '17':'Benjamin Franklin',
     '18':'A.A. Milne',
     '19':'Edgar Allen Poe',
     '20':'Deforrest Kelley',
     '21':'Thomas "Stonewall" Jackson',
     '22':'Bill Bixby',
     '23':'John Hancock',
     '24':'Neil Diamond',
     '25':'Alicia Keys',
     '26':'Douglas MaCarthur',
     '27':'Lewis Carroll',
     '28':'Alan Alda',
     '29':'William McKinley',
     '30':'Franklin D. Roosevelt',
     '31':' Justin Timberlake'
},
#29
'2':{'1':'Sherman Hemsley',
     '2':'Tommy Smothers',
     '3':'Joey Bishop',
     '4':'Clyde Tombaugh',
     '5':'John Jeffries',
     '6':'Ronald Reagan',
     '7':'Charles Dickens',
     '8':'Jules Verne',
     '9':'William Henry Harrison',
     '10':'Robert Wagner',
     '11':'Jennifer Aniston',
     '12':'Abraham "Abe" Lincoln,',
     '13':'Jerry Springer',
     '14':'George Washington Gale Ferris',
     '15':'Susan B. Anthony',
     '16':'Ice-T',
     '17':'Michael Jordan',
     '18':'John Travolta',
     '19':'Nicolas Copernicus',
     '20':'Avana Trump',
     '21':'Rue McClanahan',
     '22':'George Washington',
     '23':'Patricia Richardon',
     '24':'Steven Jobs',
     '25':'George Harrsion',
     '26':'Levi Strauss',
     '27':'John Steinbeck',
     '28':'Charles Durnin',
     '29':'Dinah Shore'
},
#31
'3':{'1':'Mark-Paul Gosselaar',
    '2':'Jon Bon Jovi',
    '3':'Jackie Joiner-Kersee',
    '4':'Len Wiseman',
    '5':'Eva Mendes',
    '6':'Connie Britton',
    '7':'Rachel Weisz',
    '8':'Aidan Quinn',
    '9':'Emmanuel Lewis',
    '10':'Carrie Underwood',
    '11':'Sam Donaldson',
    '12':'James Taylor',
    '13':'Neil Sedaka',
    '14':'Billy Crystal',
    '15':'Andrew Jackson',
    '16':'James Madison',
    '17':'Rob Lowe',
    '18':'Queen Latifah',
    '19':'Bruce Willis',
    '20':'Spike Lee',
    '21':"Rosie O'Donnell",
    '22':'Reese Witherspoon',
    '23':'Keri Russell ',
    '24':'Jessica Chastain ',
    '25':' Elton John',
    '26':' Keira Knightley',
    '27':'Mariah Carey',
    '28':'Laddy Gaga',
    '29':'Ed Skrein',
    '30':'Celine Dion',
    '31':'Ewan McGregor'
},
#30
'4':{'1':'Asa Butterfield',
    '2':'Michael Fassbender',
    '3':'Alec Baldwin',
    '4':'Robert Downey Jr.',
    '5':'Pharrell Williams',
    '6':'Paul Rudd',
    '7':'Jackie Chan',
    '8':'Robin Wright ',
    '9':'Kristen Stewart',
    '10':'Mandy Moore',
    '11':' Bill Irwin',
    '12':'Claire Danes',
    '13':'Ron Perlman',
    '14':'Abigail Breslin',
    '15':'Emma Watson',
    '16':'Selena Quintanilla',
    '17':'Victoria Addams',
    '18':"Conan O'Brien",
    '19':'Kate Hudson',
    '20':'Carmen Electra',
    '21':'Don Mattingly',
    '22':'Peter Frampton',
    '23':'George Lopez',
    '24':'Kelly Clarkson',
    '25':'Renee Zellweger',
    '26':'Bobby Rydell',
    '27':'Sheena Easton',
    '28':'Jay Leno',
    '29':'Uma Thurman',
    '30':'Kirsten Dunst'
},
#31
'5':{'1':'Tim McGraw',
     '2':'Baron Von Richtofen',
     '3':'Christopher Cross',
     '4':'Randy Travis',
     '5':'Michael Murphy',
     '6':'George Clooney',
     '7':'Johnny Unitas',
     '8':'Harry S. Truman - 33rd U.S President (1945-1953)',
     '9':'Sir James M. Barrie',
     '10':'John Wilkes Booth',
     '11':'Richard Feynman',
     '12':'Steve Winwood',
     '13':'Stevie Wonder - Singer, Musician',
     '14':'George Lucas - filmmaker',
     '15':'George Brett',
     '16':'Pierce Brosnan',
     '17':"Maureen O'Sullivan",
     '18':'Pope John Paul II (Karol Wojtyla)',
     '19':'Malcolm X',
     '20':'Dolley Madison',
     '21':'Peggy Cass',
     '22':'Sir Arthur Conan Doyle',
     '23':'Marvelous Marvin Hagler',
     '24':'Bob Dylan',
     '25':'Gene Tunney',
     '26':'Hank Williams Jr.',
     '27':'Hubert H. Humphrey',
     '28':'Rudolph Giuliani',
     '29':'John F. Kennedy - 35th U.S. President',
     '30':'Fred Allen',
     '31':'Clint Eastwood'
},
#30
'6':{'1':'Marilyn Monroe',
     '2':'Martha Washington',
     '3':'Anderson Cooper',
     '4':'King George III',
     '5':'Francisco "Pancho" Villa',
     '6':'The Dalai Lama',
     '7':"'Prince'",
     '8':'Barbara Bush',
     '9':'Johnny Depp',
     '10':'Judy Garland',
     '11':'Jeannette Rankin',
     '12':'George H. W. Bush',
     '13':'Tim Allen',
     '14':'Donald Trump',
     '15':'Ice Cube',
     '16':'Roberto Duran',
     '17':'Dan Jansen',
     '18':'Paul McCartney',
     '19':'Moe Howard',
     '20':'Cyndi Lauper',
     '21':'Michael Gross',
     '22':'Meryl Streep',
     '23':'Clarence Thomas',
     '24':"Ellison Onizuka",
     '25':"Rose O'Neill",
     '26':'Abner Doubleday',
     '27':'H. Ross Perot',
     '28':'Richard Rodger',
     '29':'George W. Goethals',
     '30':'John Cusack'
},
#31
'7':{'1':'Princess Diana',
     '2':'Thurgood Marshall',
     '3':'Tom Cruise',
     '4':'Calvin Coolidge - 30th U.S. President',
     '5':'Henry Cabot Lodge Jr',
     '6':'George W. Bush - 43rd U.S. President',
     '7':'Michelle Kwan',
     '8':'Kevin Bacon',
     '9':'O. J. Simpson',
     '10':'Jessica Simpson',
     '11':'John Quincy Adams - 6th  U.S. President',
     '12':'Julius Caesar',
     '13':'Harrison Ford',
     '14':'Gerald Ford - 38th U.S.President',
     '15':'Jesse Ventura',
     '16':'Will Ferrell',
     '17':'David Hasselhoff',
     '18':'Malcolm "Steve" Forbes Jr.',
     '19':'George McGovern',
     '20':'Carlos Santana',
     '21':'Robin Williams',
     '22':'Rose Kennedy',
     '23':'Monica Lewinsky',
     '24':'Jennifer Lopez',
     '25':'Walter Payton',
     '26':'Sandra Bullock',
     '27':'Peggy Fleming',
     '28':'Jim Davis',
     '29':'Benito Mussolini',
     '30':'Henry Ford',
     '31':'Arnold Schwarznegger'
},
#31
'8':{'1':'William Clark',
     '2':"Carroll O'Connor",
     '3':'Tom Brady',
     '4':'Louis Armstrong',
     '5':'Neil Armstrong',
     '6':'Sir Alexander Fleming',
     '7':'Charlize Theron',
     '8':'Donny Most',
     '9':'Gillian Anderson',
     '10':'Herbert Hoover',
     '11':'Stephen Wozniak',
     '12':'George Hamilton',
     '13':'Fidel Castro',
     '14':'Ervin (Magic) Johnson',
     '15':'Napoleon Bonaparte',
     '16':'Madonna',
     '17':'Robert De Niro',
     '18':'Meriwether Lewis',
     '19':'Bill Clinton',
     '20':'Benjamin Harrison',
     '21':'Wilt Chamberlain',
     '22':'Howie Dorough',
     '23':'King Louis XVI',
     '24':'Cal Ripken Jr',
     '25':'Walt Kelly',
     '26':'Geraldine Ferraro',
     '27':'Lyndon B. Johnson',
     '28':'Scott Hamilton',
     '29':'John Locke',
     '30':'Cameron Diaz',
     '31':'Frank Robinson'
},
#30
'9':{'1':'Zendaya',
    '2':'Salma Hayek',
    '3':'Charlie Sheen',
    '4':'Beyonce Knowles',
    '5':'John Cage',
    '6':'Jennifer Tilly',
    '7':'Corbin Bernsen',
    '8':'Jonathan Taylor Thomas',
    '9':'Adam Sandler',
    '10':'Ryan Phillippe',
    '11':'Harry Connick Jr',
    '12':'Ruben Studdard',
    '13':'Ben Savage',
    '14':'Faith Ford',
    '15':'Prince Harry',
    '16':'Molly Shannon',
    '17':'John Ritter',
    '18':' Lance Armstrong',
    '19':'Jimmy Fallon',
    '20':'Kristen Johnston',
    '21':'Stephen King',
    '22':'Bonnie Hunt',
    '23':'Julio Iglesias',
    '24':'Phil Hartman',
    '25':'Will Smith',
    '26':' Olivia Newton',
    '27':'Shaun Cassidy',
    '28':'Gwyneth Paltrow',
    '29':'Emily Lloyd',
    '30':'Dominique Moceanu'
},
#31
'10':{'1':'Julie Andrews',
    '2':'Kelly Ripa',
    '3':'Gwen Stefani',
    '4':'Alicia Silverstone',
    '5':'Kate Winslet',
    '6':' Elisabeth Shue',
    '7':' Simon Cowel',
    '8':' Matt Damon',
    '9':'John Lennon',
    '10':'Dale Earnhardt Jr',
    '11':'Luke Perry',
    '12':'Marion Jones',
    '13':'Ashanti',
    '14':'Usher',
    '15':'Dominic Sandoval',
    '16':'Tim Robbins',
    '17':'Eminem',
    '18':'Zac Effron',
    '19':'Evander Holyfield',
    '20':'Snoop Dogg',
    '21':'Carrie Fisher',
    '22':'Catherine Deneuve',
    '23':'Pele',
    '24':'Kevin Kline',
    '25':'Pablo Picasso',
    '26':'Hillary Rodham Clinton',
    '27':' Bill Gates',
    '28':'Winon Ryder',
    '29':'John Adams',
    '30':'Ivanka Trump',
    '31':'Vanilla Ice'
},
#30
'11':{'1':'Toni Collette',
    '2':' David Schwimmer',
    '3':' Dolph Lundgren',
    '4':'Matthew McConaughey',
    '5':'Famke Janssen',
    '6':'Emma Stone',
    '7':'Adam DeVine',
    '8':'Parker Posey',
    '9':'Lou Ferrigno',
    '10':'Tracy Morgan',
    '11':'Leonardo DiCaprio',
    '12':'Ryan Gosling',
    '13':'Gerard Butler',
    '14':'Josh Duhamel',
    '15':'Shailene Woodley',
    '16':'Maggie Gyllenhaal',
    '17':'Rachel McAdams',
    '18':'Owen Wilson',
    '19':'Jodie Foster',
    '20':'Joel McHale',
    '21':'Jena Malone',
    '22':'Scarlett Johansson',
    '23':'Miley Cyrus',
    '24':'Paul Tagliabue',
    '25':'Andrew Carnegie',
    '26':'Andrew Carnegie',
    '27':'Bill Nye',
    '28':'Ed Harris',
    '29':'Anna Faris',
    '30':'Ben Stiller'
},
#31
'12':{'1':'Zoe Kravitz',
    '2':'Lucy Liu',
    '3':'Amanda Seyfried',
    '4':'Tyra Banks',
    '5':'Frankie Muniz',
    '6':'Andrew Cuomo',
    '7':'Edd Hall',
    '8':'Ian Somerhalder',
    '9':'Donny Osmond',
    '10':' Susan Dey',
    '11':'Jermaine Jackson',
    '12':'Sheila Escoveda',
    '13':'Ted Nugent',
    '14':'Patty Duke',
    '15':'Garrett Wang',
    '16':' Hallee Hirsh',
    '17':'Bill Pullman',
    '18':'Christina Aguilera',
    '19':'Alyssa Milano',
    '20':'Kiefer Sutherland',
    '21':'Florence Griffith Joyner',
    '22':'Jan Stephenson',
    '23':'Susan Lucci,',
    '24':'Ricky Martin',
    '25':'Dido',
    '26':'Jared Leto',
    '27':'Cokie Roberts',
    '28':'Malcolm Gets',
    '29':'Ted Danson',
    '30':'Tiger Woods',
    '31':'Nicholas Sparks'
},


}

class MainHandler(webapp2.RequestHandler):

    def get(self):

        template = jinja_environment.get_template('templates/main.html')
        self.response.write(template.render())

    def post(self):
        template = jinja_environment.get_template('templates/result.html')
        day1 = self.request.get('day')
        month1 = self.request.get('month')


        self.response.write(weekday[month1][day1])
        self.response.out.write(template.render())

        #month1 = self.request.get('r_month')
        #day1 = self.request.get('r_day')
        #self.response.write(day)
        images = ["https://s-media-cache-ak0.pinimg.com/736x/04/b8/3c/04b83ced6ccdbbb25411e05fe8d3476a--zodiac-signs-aries-aries-horoscope.jpg",
            "https://s-media-cache-ak0.pinimg.com/236x/57/ca/ca/57caca0dee0b86be863c2990200e8582--zodiac-signs-taurus-taurus-horoscope.jpg",
            "https://thumb7.shutterstock.com/thumb_large/1006391/319554695/stock-vector-zodiac-signs-gemini-319554695.jpg",
            "http://dellgogreen.com/wp-content/uploads/2017/07/cancer-zodiac-sign-wallpaper-5-200x150.jpg",
            "http://www.horoscopemonthly.net/wp-content/uploads/2015/06/Leo-300x235.jpg",
            "http://horoscopezodiacpro.com/wp-content/uploads/2017/01/horoscopezodiacpro_virgo-277x300.gif",
            "https://d.wattpad.com/story_parts/23/images/1402265225c94acb.jpg",
            "https://s-media-cache-ak0.pinimg.com/236x/bc/8c/c4/bc8cc47487a3da20e42063e60eef2c4b--leo-horoscope-gemini.jpg",
            "http://paintthetownbodyart.com/wp-content/uploads/Sagittarius-And-The-Zodiac-Sign-Horoscope-Circle-Tattoo-Design-3.jpg",
            "http://www.stampettes.com/stamp-images/zodiac_capricorn-navy.png",
            "https://3.bp.blogspot.com/-0JvODuef3D8/WEcDC2NO4WI/AAAAAAAAGlE/_-ItQRJPooAZJlNAlt-W3JKPAHO0oEw1QCK4B/s320/11-kova-burcu-gunluk-burc-yorumu.png",
            "http://www.topinspired.com/wp-content/uploads/2017/03/PISCES-YEARLY-300x230.png"
        ]

        if((int(month1)==3 and int(day1)>= 21)or (int(month1)==4 and int(day1)<=19)):
            image = "<img src='" + images[0] + "' />"
            self.response.write(image);
            self.response.write('<br><strong> Zodiac Sign: Aries </strong>')
        if((int(month1)==4 and int(day1)>=20 )or (int(month1)==5 and int(day1)<=20)):
            image = "<img src='" + images[1] + "' />"
            self.response.write(image);
            self.response.write('<br><strong> Zodiac Sign: Taurus </strong>')
        if((int(month1)==5 and int(day1)>=21 )or (int(month1)==6 and int(day1)<=20)):
            image = "<img src='" + images[2] + "' />"
            self.response.write(image);
            self.response.write('<br><strong> Zodiac Sign: Gemini </strong>')
        if((int(month1)==6 and int(day1)>=21 )or (int(month1)==7 and int(day1)<=22)):
            image = "<img src='" + images[3] + "' />"
            self.response.write(image);
            self.response.write('<b><strong> Zodiac Sign: Cancer </strong>')
        if((int(month1)==7 and int(day1)>=22 )or (int(month1)==8 and int(day1)<=22)):
            image = "<img src='" + images[4] + "' />"
            self.response.write(image);
            self.response.write('<br><strong> Zodiac Sign: Leo </strong>')
        if((int(month1)==8 and int(day1)>=23 )or (int(month1)==9 and int(day1)<=22)):
            image = "<img src='" + images[5] + "' />"
            self.response.write(image);
            self.response.write('<br><strong> Zodiac Sign: Virgo </strong>')
        if((int(month1)==9 and int(day1)>=23 )or (int(month1)==10 and int(day1)<=22)):
            image = "<img src='" + images[6] + "' />"
            self.response.write(image);
            self.response.write('<br><strong> Zodiac Sign: Libra </strong>')
        if((int(month1)==10 and int(day1)>=23 )or (int(month1)==11 and int(day1)<=21)):
            image = "<img src='" + images[7] + "' />"
            self.response.write(image);
            self.response.write('<br><strong> Zodiac Sign: Scorpio </strong>')
        if((int(month1)==11 and int(day1)>=22 )or (int(month1)==12 and int(day1)<=21)):
            image = "<img src='" + images[8] + "' />"
            self.response.write(image);
            self.response.write('<br><strong> Zodiac Sign: Sagittarius </strong>')
        if((int(month1)==12 and int(day1)>=22 )or (int(month1)==1 and int(day1)<=19)):
            image = "<img src='" + images[9] + "' />"
            self.response.write(image);
            self.response.write('<br><strong> Zodiac Sign: Capricorn </strong>')
        if((int(month1)==1 and int(day1)>=20 )or (int(month1)==2 and int(day1)<=18)):
            image = "<img src='" + images[10] + "' />"
            self.response.write(image);
            self.response.write('<br><strong> Zodiac Sign: Aquarius </strong>')
        if((int(month1)==2 and int(day1)>=19 )or (int(month1)==3 and int(day1)<=20)):
            image = "<img src='" + images[11] + "' />"
            self.response.write(image);
            self.response.write('<br><strong> Zodiac Sign: Pisces </strong>')

        horoscope=['Today will be a great day to start something new.' ,
            'Nothing is too hard if you set your mind to it.',
            'Everything will work out as long as you keep your goals in mind.',
            'Remember that the best success comes from the hardest work.',
            'Failure is in your future, everything  you think you know will turn out to be lies.',
            'Nothing is the way that it seems.',
            "Remember that it's not about the destination, but the adventure.",
            'All good things are worth waiting for.',
            'Success is in your future.',
            'Nothing lasts forever, be ready to let go.',
            "Dreams show one's true desire.",
            "Don't be afraid to be yourself.",
            "Don't take things for granted, your may regret it",
            "There's no such thing as imposssible.",
            "If you're too comfortable, maybe its time for a change.",
            "Change doesn't always have to be hard."]

        horoscope[randint(0,15)]

        self.response.write('<br><strong>Your horoscope for today is: </strong>')
        self.response.write(horoscope[randint(0,15)])


app = webapp2.WSGIApplication([
    ('/', MainHandler)

], debug=True)
