# Szkielet na potrzeby warsztatów. #
## 1. Najważniejsze informacje: ##
* Model User znajduje się w pliku models.py
* Model Messages należy tam dopisać istnieje pusta klasa Message, która po zaimplementowaniu method:
  * `_create_object`, która powinna zwracać Instancje modelu
  * `save`, która powinna aktualizować model w bazie danych lub tworzyć nowy wpis.
  * i inne methody, które zostały wymienione w scenariuszu warsztatów.
* plik **main.py** posiada całą niezbędną logikę do zweryfikowania jaka opcja jest teraz wykonywana, wykorzystuje do 
tego OptionHandler, który posiada odpowiednie gettery, zwracające wartości `True` albo `False`
* Istnieje pomocniczy szkielet do rozwiązania obiektowego, **dispacher.py**, o wykorzystaniu poniżej.
* Każdy warunek loficzny w pliku **main.py** podpowie wam jaka akcja jest oczekiwana. 
# 2. Sposoby wykorzystania szkieletu. #
## 2.a Z wykorzystaniem Dispachera ##
* Dispacher posiada szereg pustych method, które mają podpowiadać strukturę kodu, każda metoda to mniej więcej jedna 
funkcjonalność z scenariusza warsztatów.
* A potem wystarczy wywołać methody w odpowiednich warunkach logicznych `if`, które znajdują się w pliku **main.py**.
## 2.b Rozwiązanie bez dispachera. ##
Polega tylko na napisaniu całej logiki każdej operacji w odpowiednim bloku warunkowym `if`, który znajduje się w pliku **main.py**