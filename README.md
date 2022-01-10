# Bookmarker
## FastAPI + Ormar + Alembic
```
#Install dependencies in virtual environment 
pipenv install

#Initialize database with migrations
alembic upgrade head

#Run app
uvicorn bookmarker.main:app --reload

#Create migration
alembic revision --autogenerate -m "message"
```

## Color Scheme
```
https://coolors.co/003049-d62828-f77f00-fcbf49-eae2b7

/* CSS HEX */
--prussian-blue: #003049ff;
--maximum-red: #d62828ff;
--orange: #f77f00ff;
--maximum-yellow-red: #fcbf49ff;
--lemon-meringue: #eae2b7ff;

/* CSS HSL */
--prussian-blue: hsla(201, 100%, 14%, 1);
--maximum-red: hsla(0, 69%, 50%, 1);
--orange: hsla(31, 100%, 48%, 1);
--maximum-yellow-red: hsla(40, 97%, 64%, 1);
--lemon-meringue: hsla(51, 55%, 82%, 1);

/* SCSS HEX */
$prussian-blue: #003049ff;
$maximum-red: #d62828ff;
$orange: #f77f00ff;
$maximum-yellow-red: #fcbf49ff;
$lemon-meringue: #eae2b7ff;

/* SCSS HSL */
$prussian-blue: hsla(201, 100%, 14%, 1);
$maximum-red: hsla(0, 69%, 50%, 1);
$orange: hsla(31, 100%, 48%, 1);
$maximum-yellow-red: hsla(40, 97%, 64%, 1);
$lemon-meringue: hsla(51, 55%, 82%, 1);

/* SCSS RGB */
$prussian-blue: rgba(0, 48, 73, 1);
$maximum-red: rgba(214, 40, 40, 1);
$orange: rgba(247, 127, 0, 1);
$maximum-yellow-red: rgba(252, 191, 73, 1);
$lemon-meringue: rgba(234, 226, 183, 1);

/* SCSS Gradient */
$gradient-top: linear-gradient(0deg, #003049ff, #d62828ff, #f77f00ff, #fcbf49ff, #eae2b7ff);
$gradient-right: linear-gradient(90deg, #003049ff, #d62828ff, #f77f00ff, #fcbf49ff, #eae2b7ff);
$gradient-bottom: linear-gradient(180deg, #003049ff, #d62828ff, #f77f00ff, #fcbf49ff, #eae2b7ff);
$gradient-left: linear-gradient(270deg, #003049ff, #d62828ff, #f77f00ff, #fcbf49ff, #eae2b7ff);
$gradient-top-right: linear-gradient(45deg, #003049ff, #d62828ff, #f77f00ff, #fcbf49ff, #eae2b7ff);
$gradient-bottom-right: linear-gradient(135deg, #003049ff, #d62828ff, #f77f00ff, #fcbf49ff, #eae2b7ff);
$gradient-top-left: linear-gradient(225deg, #003049ff, #d62828ff, #f77f00ff, #fcbf49ff, #eae2b7ff);
$gradient-bottom-left: linear-gradient(315deg, #003049ff, #d62828ff, #f77f00ff, #fcbf49ff, #eae2b7ff);
$gradient-radial: radial-gradient(#003049ff, #d62828ff, #f77f00ff, #fcbf49ff, #eae2b7ff);
```
