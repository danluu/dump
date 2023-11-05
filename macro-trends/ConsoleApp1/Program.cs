using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace webscraping {
    class Program
    {
        static void Main(string[] args)
        {   
            ChromeOptions options = new ChromeOptions();
            options.AddArgument("--disable-blink-features=AutomationControlled");

            IWebDriver driver = new ChromeDriver(options);

            driver.Navigate().GoToUrl("https://macrotrends.net/stocks/charts/DDOG/datadog/gross-margin");

            
            // Get all links on page
            IList<IWebElement> allLinks = driver.FindElements(By.XPath("//a[@href]"));
            // Print out all links
            Console.WriteLine("All links on page: ");
            foreach (IWebElement link in allLinks)
            {   
                Console.WriteLine(link.GetAttribute("href"));
                if (link.GetAttribute("href").Contains("gross-margin")) {
                    Console.WriteLine(link.GetAttribute("href"));
                }
            }

            // Print out all text with a dollar sign
            Console.WriteLine("All text with a dollar sign: ");
            IList<IWebElement> allDollars = driver.FindElements(By.XPath("//*[contains(text(), '$')]"));
            foreach (IWebElement text in allDollars)
            {
                Console.WriteLine(text.Text);
            }

            // Print out all text with a percent sign.
            Console.WriteLine("All text with a percent sign: ");
            IList<IWebElement> allPercents = driver.FindElements(By.XPath("//*[contains(text(), '%')]"));
            foreach (IWebElement text in allPercents)
            {
                Console.WriteLine(text.Text);
            }
            

            // Print out all text with a counter showing index of element.
            Console.WriteLine("All text with a counter showing index of element: ");
            
            // Retry in loop case we get OpenQA.Selenium.StaleElementReferenceException due to page not being loaded yet.
            IList<IWebElement> allText = null;
            while (allText == null) {
                try {
                    allText = driver.FindElements(By.XPath("//*[not(child::*) and text()]"));
                } catch (OpenQA.Selenium.StaleElementReferenceException) {
                    Console.WriteLine("StaleElementReferenceException");
                    Thread.Sleep(1000);
                }
            }

            int counter = 0;
            foreach (IWebElement text in allText)
            {
                Console.WriteLine(counter + ": " + text.Text);
                counter++;
            }

        }
    }
}
