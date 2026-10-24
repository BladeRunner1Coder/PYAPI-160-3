### Application gets your IP address through a request from <https://api.ipify.org/>, then gets your location (city) through a request from <https://ipinfo.io/>, and also creates a folder in your Yandex Disk (<https://360.yandex.ru/disk/>), where a JSON file with your IP address and location is created.

#### Application needs an OAuth token from <https://yandex.ru/dev/disk/poligon/>

#### This token should be placed in the variable "TOKEN" in module ".env" (as shown by the module "example.env").

#### The command "getip = GetIP()" creates an object "getip" of the "GetIP" class, which allows you to use its methods to get and use your IP address.

#### The command "address = GetAddress(getip.get_ip())" creates an object "address" of the "GetAddress" class, that takes your IP address (from the previous object) as a parameter, and allows you to use its methods to get and use your location.

#### The command "YD = YandexDisk(token)" creates an object "YD" of the "YandexDisk" class, that takes your Yandex Disk TOKEN as a parameter and allows you to use its methods to create the folder "Your IP city" (if there is no such folder) in your Yandex Disk and to create a JSON file with your IP address and your location in this folder.

#### Application informs you about successful (or not) execution of all important steps, and also illustrates the application progress by a graphic-and-numeric scale from 0 to 100%.
