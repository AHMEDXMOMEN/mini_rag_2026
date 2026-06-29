## note(1) ubuntu main path  
\\wsl$\Ubuntu\home\ahmedmomen\

## note(2) to see md file view 
ctrl > shift > V

## (mini-rag-app) ahmedmomen@DESKTOP-NMPL0DD:~/mini_rag_2026
$ pip install -r requirements.txt
for install req

# diroctores
## assits 
 assits fa dircetory / folder 3ayzo yzhar 3ala el git hib bs msh 3ayez elky gowa yzhar 3shan keda elt giwa hatkon sowar aw 7gat msh 3ayzha tet7at 3ala git hub 3shan matbata2esh el rebo / fe file esmo ,git keep da by7afez en el file yfdak mawgod fel rebo w yt3melo commit w howa asln fady 
#

##router /base.py
sho8lanet el router eno bs yb3at w yasta2bel http rquest aw ay request 3matan ama el route
fa a7san nefsel 3ano el logic ykon fe mkan tany 

## el src/ main.py
el a7san ykon bs bynade el route 3shan law 3malt gowa e route w kman 3malt gowa el logic haykbar w ykon m3a2ad fa a7san n2asem el route laa7dhom fe mkan w logic kol route fe mkan ba3den anadehom mn el logic 

```txt
main bystad3y routes ely 3azo fel example in base.py (route file) > base fe el route bystad3y el logic mn el logic file  
```
###

## MVC
Model-View-Controller
1- model gowa ay 7aga leha 3laka bel data 
2- view  da el nas betshofo hhtml ay ay 7aga tanyta 
3- controller el logic el asae ely bystad3y el 7gat de 
```txt
MVC (Model-View-Controller) is a software architecture pattern that organizes an application into three main components. The Model manages the data and business logic, the View is responsible for displaying information to the user, and the Controller receives user requests, coordinates with the Model, and returns the appropriate View. This separation of responsibilities makes applications easier to develop, maintain, test, and scale.
```
User
 │
 ▼
Controller
(get /users/5)
 │
 ▼
Model
(get user from DB)
 │
 ▼
Database
 │
 ▼
Model
 │
 ▼
Controller
 │
 ▼
View (JSON)
 │
 ▼
User

##Re-export __init__.py

```txt
#Re-export:
# 1- __init__.py howa Python file (module) bytetsha8al awel ma ta3mel import lel package, w momken t7ot gowah imports aw ay initialization 3ayzha tetnafaz.
# 2- in __init__.py >> from .users import User
# 3- from shop import User
#  insted of from shop.users import User
```
```txt
2. T3raf metadata bta3 el package

Momken t7ot ma3lomat 3an el package.

__version__ = "1.0.0"
__author__ = "Ahmed"

Ba3d keda:

import models

print(models.__version__)
```
```txt
3. Tanfiz code awel ma el package yet3mel import

Ay code gowa __init__.py bytnafaz awel ma t3mel:

import models

Example:

print("Models package loaded")

Output:

Models package loaded

Aw momken:

logging.basicConfig(...)

Aw:

load_dotenv()

Bas lazem tkoon 7azer, 3shan ay code hena hayetnafaz kol mara el package yet3mel import.
```
```txt
4. Ta3mel package API anzaf

Msh kol el files tb2a zahra lel user.

models/
    users.py
    admin.py
    helper.py
    __init__.py
# __init__.py
from .users import User

Elly byesta5dem el package:

from models import User

W may3rafsh aslan en fe helper.py aw admin.py.
```
```txt
5. T3raf eh elly yet3mel export b __all__
from .users import User
from .products import Product

__all__ = ["User", "Product"]

Da by2ol l Python en dol el official public API.

6. Te7ot initialization lel package

Example:

# __init__.py

from database import connect

connect()

Aw:

config = load_config()

Fa ay module gowa el package y2dar yesta5dem:

from . import config
7. T2assem package kbeer
shop/
    __init__.py
    users/
        __init__.py
        service.py
    orders/
        __init__.py
        service.py

Kol folder fih __init__.py yb2a package mosta2el.
```
# end of "____init____.py" Re-export