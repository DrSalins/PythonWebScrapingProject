# Python Web Scraping Project

Python Web Scraping Project is a simple project which I created to teach a student how to make use of Beautiful Soup and Python with some programming concepts to scrape quotes from a website.

# Explanation
```bash 
scrape.py
```
Scrape.py is a .py file in which Selenium is used with BS4 to scrape an HTML page that has been added as a variable, which then shows an introduction to how to use the different methods available in BS4. 
```bash 
project.py
```
project.py is a .py file that uses BS4 to scrape [Quotes To Scrape](http://quotes.toscrape.com/). This makes use of its main tool HTML.parser. 

Using a While Loop to start with, we created a For Loop inside this loop to find all div tags on the webpage with a class with "quote" and then within those tags find another class called "text" and within an additional span tag to find a class called "author".
We then print the results and then head to the next page by finding the class "next" in order to head to the next page.

## Usage

If you would like to try out this simple scraping project, or create a new version of it simply clone it to your computer, using the below command

```bash
git clone git@github.com:DrSalins/PythonWebScrapingProject.git
```


## Skills Used To Create

<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py" />
  </a>
</p>

## Running The Project

Clone the repository, 
open it in VS Code or any other IDE and then 
navigate to either of the files you want to 
try and then click the Run Button on your IDE

## License

[Siddarth_Salins_Mudaliar]
