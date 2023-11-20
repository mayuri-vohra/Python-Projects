import random
when=['A few years ago','Yesterday','Last night','A long time ago','On 20th Jan']
who=['a rabbit','an elephant','a mouse','a turtle','a cat']
namee=['Ali','Mariam','Daniel','Houck','Starwalker']
residence=['Barcelona','India','Germany','London','England']
went=['cinema','university','seminar','school','laundary']
happened=['made a lot of friends','eats a burger','found a secret key','solved a mystery','wrote a book']
print(random.choice(when)+','+random.choice(namee)+'that lived in'+ random.choice(residence)+', went to the'+random.choice(went)+'and'+random.choice(happened))