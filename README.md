
## 


## Start the project

* create virtual environment

```shell
python3.11 -m venv myvenv
```

* activate virtual environment

```shell
source myvenv/bin/activate
```

## Download chrome driver

* Find web browser version. In this case go to the next link
```
chrome://version/
```
You can see <something like this:
 *Google Chrome: 126.0.6478.114 (Official Build) (64-bit)*

In some cases when you install `selenium` this automatically install a web browser. So take this version provided


* Download web driver
Go to the next link, search the file with match with your web browser version and download it
```
https://chromedriver.storage.googleapis.com/index.html
```
If your internet browser does not appear in the list, search for it in the following link.
```
https://web.archive.org/web/20240628173315/https://googlechromelabs.github.io/chrome-for-testing/#stable
```

* Extract the content and copy the `chromedriver` file in the path `/usr/local/bin/` or `/usr/bin/`

```shell
sudo cp chromedriver /usr/bin/
```

* Run the project, and should it works :)


---

## Run the project con Docker Compose

```shell
docker-compose -f dev.yml up
```